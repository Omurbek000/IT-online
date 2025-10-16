from django_filters import FilterSet
from .models import *


class UserProfileFilter(FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'username': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'is_active': ['exact'],
        }


class TeacherFilter(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'position': ['exact'],
            'work_experience': ['gt', 'lt'],
        }


class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            'level': ['exact'],
            'user': ['exact'],
        }


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['exact', 'icontains'],
        }


class SubCategoryFilter(FilterSet):
    class Meta:
        model = SubCategory
        fields = {
            'name': ['exact', 'icontains'],
            'category': ['exact'],
        }


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'category': ['exact'],
            'teacher': ['exact'],
            'price': ['gt', 'lt'],
            'level': ['exact'],
            'language_course': ['exact'],
        }


class LessonFilter(FilterSet):
    class Meta:
        model = Lesson
        fields = {
            'course': ['exact'],
            'created_date': ['gt', 'lt'],
        }


class AssignmentFilter(FilterSet):
    class Meta:
        model = Assignment
        fields = {
            'lesson': ['exact'],
            'title': ['icontains'],
        }


class ExamFilter(FilterSet):
    class Meta:
        model = Exam
        fields = {
            'exam_title': ['exact', 'icontains'],
            'course': ['exact'],
        }


class QuestionFilter(FilterSet):
    class Meta:
        model = Quesstions
        fields = {
            'exam': ['exact'],
            'text': ['icontains'],
        }


class OptionFilter(FilterSet):
    class Meta:
        model = Option
        fields = {
            'question': ['exact'],
            'is_correct': ['exact'],
        }


class CertificateFilter(FilterSet):
    class Meta:
        model = Certificate
        fields = {
            'student': ['exact'],
            'course': ['exact'],
        }


class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = {
            'user': ['exact'],
            'course': ['exact'],
            'rating': ['gt', 'lt'],
        }


class CartFilter(FilterSet):
    class Meta:
        model = Cart
        fields = {
            'user': ['exact'],
        }


class CartItemFilter(FilterSet):
    class Meta:
        model = CartItem
        fields = {
            'cart': ['exact'],
            'course': ['exact'],
        }
