from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('user', UserProfileViewSet, basename='users')
router.register('teacher', TeacherViewSet, basename='teachers')
router.register('student', StudentViewSet, basename='students')
router.register('category', CategoryViewSet, basename='categories')
router.register('subcategory', SubCategoryViewSet, basename='subcategories')
router.register('course', CourseViewSet, basename='courses')
router.register('lesson', LessonViewSet, basename='lessons')
router.register('assignment', AssignmentViewSet, basename='assignments')
router.register('exam', ExamViewSet, basename='exams')
router.register('certificate', CertificateViewSet, basename='certificates')
router.register('review', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
]