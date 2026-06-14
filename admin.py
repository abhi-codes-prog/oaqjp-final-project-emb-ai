from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Enrollment, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionInline(admin.TabularInline):
    model = Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
