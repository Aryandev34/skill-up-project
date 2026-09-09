import random

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods

from .forms import SignUpForm
from .models import Language, Question, QuizAttempt

QUIZ_SIZE = 10
SESSION_QUIZ_KEY = "skillup_quiz"


def landing(request):
    if request.user.is_authenticated:
        return redirect("quiz:dashboard")
    languages = Language.objects.order_by("order", "name")
    return render(request, "quiz/landing.html", {"languages": languages})


def signup(request):
    if request.user.is_authenticated:
        return redirect("quiz:dashboard")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome to Skill up — pick a track and level up.")
            return redirect("quiz:dashboard")
    else:
        form = SignUpForm()
    return render(request, "quiz/signup.html", {"form": form})


class SkillUpLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True


class SkillUpLogoutView(LogoutView):
    next_page = reverse_lazy("quiz:landing")


@login_required
def dashboard(request):
    languages = Language.objects.annotate(
        q_count=Count("questions", distinct=True)
    ).order_by("order", "name")
    return render(request, "quiz/dashboard.html", {"languages": languages})


@login_required
def select_level(request, slug):
    language = get_object_or_404(Language, slug=slug)
    counts = (
        Question.objects.filter(language=language)
        .values("difficulty")
        .annotate(c=Count("id"))
    )
    by_diff = {row["difficulty"]: row["c"] for row in counts}
    level_rows = []
    for value, label in Question.Difficulty.choices:
        n = by_diff.get(value, 0)
        level_rows.append(
            {
                "value": value,
                "label": label,
                "count": n,
                "ready": n >= QUIZ_SIZE,
            }
        )
    return render(
        request,
        "quiz/select_level.html",
        {
            "language": language,
            "levels": level_rows,
            "min_needed": QUIZ_SIZE,
        },
    )


@login_required
@require_http_methods(["GET", "POST"])
def take_quiz(request, slug, difficulty):
    language = get_object_or_404(Language, slug=slug)
    valid = {c[0] for c in Question.Difficulty.choices}
    if difficulty not in valid:
        raise Http404()

    pool = list(
        Question.objects.filter(language=language, difficulty=difficulty).values_list(
            "id", flat=True
        )
    )
    if len(pool) < QUIZ_SIZE:
        messages.error(
            request,
            f"Not enough questions for {language.name} at this level yet. "
            f"Need {QUIZ_SIZE}, have {len(pool)}.",
        )
        return redirect("quiz:select_level", slug=slug)

    if request.method == "POST":
        data = request.session.get(SESSION_QUIZ_KEY)
        if not data or data.get("slug") != slug or data.get("difficulty") != difficulty:
            messages.error(request, "Session expired — start the quiz again.")
            return redirect("quiz:select_level", slug=slug)

        ids = data["question_ids"]
        questions = list(Question.objects.filter(id__in=ids))
        if len(questions) != len(ids):
            messages.error(request, "Something went wrong. Please retry.")
            del request.session[SESSION_QUIZ_KEY]
            return redirect("quiz:select_level", slug=slug)

        score = 0
        details = []
        for q in questions:
            key = f"q_{q.id}"
            picked = request.POST.get(key, "").strip().lower()
            ok = picked == q.correct.lower()
            if ok:
                score += 1
            details.append(
                {
                    "question": q,
                    "picked": picked or None,
                    "correct": ok,
                }
            )

        QuizAttempt.objects.create(
            user=request.user,
            language=language,
            difficulty=difficulty,
            score=score,
            total=QUIZ_SIZE,
        )
        del request.session[SESSION_QUIZ_KEY]

        random.shuffle(details)
        pct = round(100 * score / QUIZ_SIZE)
        return render(
            request,
            "quiz/results.html",
            {
                "language": language,
                "difficulty": difficulty,
                "difficulty_label": dict(Question.Difficulty.choices).get(
                    difficulty, difficulty
                ),
                "score": score,
                "total": QUIZ_SIZE,
                "percent": pct,
                "details": details,
            },
        )

    # GET — new attempt
    picked_ids = random.sample(pool, QUIZ_SIZE)
    request.session[SESSION_QUIZ_KEY] = {
        "slug": slug,
        "difficulty": difficulty,
        "question_ids": picked_ids,
    }
    questions = list(
        Question.objects.filter(id__in=picked_ids).order_by("id")
    )
    random.shuffle(questions)
    return render(
        request,
        "quiz/take_quiz.html",
        {
            "language": language,
            "difficulty": difficulty,
            "difficulty_label": dict(Question.Difficulty.choices).get(
                difficulty, difficulty
            ),
            "questions": questions,
            "quiz_size": QUIZ_SIZE,
        },
    )
