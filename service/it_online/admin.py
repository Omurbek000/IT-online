from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

import nested_admin
from nested_admin import NestedModelAdmin, NestedTabularInline
@admin.register(
    UserProfile,
    Teacher,
    Student,
    Review,
)
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


#! for subcategory and category models бир бирине тез кошуу учун
class SubCategoryInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = SubCategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    inlines = [SubCategoryInline]

    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


class OptionInline(nested_admin.NestedTabularInline, TranslationInlineModelAdmin):
    model = Option
    extra = 1


class QuestionsInline(nested_admin.NestedTabularInline, TranslationInlineModelAdmin):
    model = Questions
    extra = 1
    inlines = [OptionInline]


@admin.register(Exam)
class ExamAdmin(NestedModelAdmin,TranslationAdmin):
    inlines = [QuestionsInline]

    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


class AssignmentInline(nested_admin.NestedTabularInline, TranslationInlineModelAdmin):
    model = Assignment
    extra = 1
    

class LessonInline(nested_admin.NestedTabularInline, TranslationInlineModelAdmin):
    model = Lesson
    extra = 1
    inlines = [AssignmentInline]



@admin.register(Course)
class CourseAdmin(NestedModelAdmin, TranslationAdmin):
    inlines = [LessonInline]

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
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass
