from .models import *
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "username", "email", "first_name", "last_name", "is_active"]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = SubCategory
        fields = ["id", "name", "category"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "name", "price", "category", "lessons_count"]

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons(self, obj):
        return LessonSerializer(obj.lesson_set.all(), many=True).data


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = "__all__"

    def get_questions_count(self, obj):
        return obj.quesstions_set.count()


class QuesstionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quesstions
        fields = "__all__"

    def get_options(self, obj):
        return OptionSerializer(obj.option_set.all(), many=True).data


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True, many=True)

    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = "__all__"
