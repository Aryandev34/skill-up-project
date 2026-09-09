from django.contrib import admin

from .models import Language, Question, QuizAttempt


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order", "icon_class")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text_short", "language", "difficulty", "correct")
    list_filter = ("language", "difficulty")

    @admin.display(description="Question")
    def text_short(self, obj):
        return obj.text[:60] + ("…" if len(obj.text) > 60 else "")


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "language", "difficulty", "score", "total", "created_at")
    list_filter = ("language", "difficulty")
