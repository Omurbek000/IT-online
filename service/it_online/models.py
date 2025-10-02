from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    profile_image = models.ImageField(upload_to="profile_image/")
    bio = models.TextField()
    ROLE_CHOICES = (
        ("student", "Student"),
        ("teacher", "Teacher"),
    )
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default="student")

    def __str__(self):
        return f"{self.first_name} {self.role}"


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name


class Course(models.Model):
    course_name = models.CharField(max_length=64)
    descriptions = models.TextField()
    sub_category = models.ManyToManyField(SubCategory)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    LEVEL_CHOICES = (
        ("beginner", "Beginner"),
        ("middle", "Middle"),
        ("advanced", "Advanced"),
    )
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES, default="beginner")
    LANGUAGE_CHOICES = (
        ("english", "English"),
        ("arabic", "Arabic"),
        ("russian", "Russian"),
        ("spanish", "Spanish"),
        ("kyrgyz", "Kyrgyz"),
    )
    language_course = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=32, default="kyrgyz"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course_name} - {self.level}"


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    video_lesson = models.FileField(upload_to="lesson_video/", null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    docs_lesson = models.FileField(upload_to="lesson_docs/")

    def __str__(self):
        return f"{self.title}-{self.course}-{self.content}"


class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    description = models.TextField()
    due_data = models.DateField()
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.due_data} - {self.students}"


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    questions = models.CharField(max_length=64)
    passing_score = models.PositiveSmallIntegerField()
    duration = models.DurationField(default=timedelta(hours=1))


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField()
    certificate_url = models.FileField(upload_to="certificate/")

    def __str__(self):
        return f"{self.student} - {self.course} - {self.issued_at}"


class Review(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True
    )
    created_date = models.DateTimeField(auto_now_add=True)
