from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Проверка соответствия авторов объекта и запроса для небезопасных методов"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
