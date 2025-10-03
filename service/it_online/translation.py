from modeltranslation.translator import TranslationOptions, register
from .models import UserProfile, Category, SubCategory, Course, Lesson, Assignment, Exam, Review, Teacher, Student


@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = (
        "first_name",
        "last_name",
    )

@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = (
        "specialization",
        "bio",
    )

@register(Student)
class StudentleTranslationOptions(TranslationOptions):
    fields = (
        "progress",
        "bio",
    )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        "category_name",
    )

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = (
        "sub_category_name",
    )


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = (
        "course_name",
        "descriptions",
        "level",
        "language_course",
    )


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "content",
    )


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "questions",
    )


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = (
        "comment",
    )