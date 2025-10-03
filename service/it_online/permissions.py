from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "admin"


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "teacher"


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "student"


class IsCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class IsAssignmentOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.course.created_by == request.user


class IsReviewOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user
