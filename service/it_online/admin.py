from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(UserProfile)
class UserProfileAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Teacher)
class TeacherAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Student)
class StudentAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Lesson)
class LessonAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Assignment)
class AssignmentAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Exam)
class ExamAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Review)
class ReviewAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = [
        "student",
        "course",
    ]
