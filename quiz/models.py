from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Language(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, max_length=80)
    icon_class = models.CharField(
        max_length=120,
        default="fa-solid fa-code",
        help_text="Font Awesome class, e.g. fa-brands fa-python",
    )
    blurb = models.CharField(max_length=200, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Question(models.Model):
    class Difficulty(models.TextChoices):
        LOW = "low", "Low"
        MED = "med", "Medium"
        HIGH = "high", "High"

    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name="questions"
    )
    difficulty = models.CharField(
        max_length=8, choices=Difficulty.choices, db_index=True
    )
    text = models.TextField()
    choice_a = models.CharField(max_length=500)
    choice_b = models.CharField(max_length=500)
    choice_c = models.CharField(max_length=500)
    choice_d = models.CharField(max_length=500)
    correct = models.CharField(
        max_length=1,
        choices=[("a", "A"), ("b", "B"), ("c", "C"), ("d", "D")],
    )

    class Meta:
        ordering = ["language", "difficulty", "id"]

    def correct_text(self):
        return getattr(self, f"choice_{self.correct.lower()}", "")

    def __str__(self):
        return f"{self.language.name} ({self.difficulty}): {self.text[:50]}..."


class QuizAttempt(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="quiz_attempts",
    )
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=8, choices=Question.Difficulty.choices)
    score = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} — {self.language} {self.score}/{self.total}"
