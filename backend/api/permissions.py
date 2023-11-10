from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Права для администратора или только для чтения.

    """

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_superuser)


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Права для автора или только для чтения.

    """

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'author'):
            author_field = 'author'
        elif hasattr(obj, 'customer'):
            author_field = 'customer'
        elif hasattr(obj, 'user'):
            author_field = 'user'
        else:
            return False
        return (
            request.method in permissions.SAFE_METHODS
            or getattr(obj, author_field) == request.user
        )


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Права для владельца или только для чтения.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == 'PATCH':
            return obj == request.user
        return True


class IsOwnerOrReadOnlyProfile(permissions.BasePermission):
    """
    Права для владельца или только для чтения.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == 'PATCH':
            return obj.user == request.user
        return True


class IsInitiatorOrReceiverChatPermission(permissions.BasePermission):
    """
    Права для работы с чатами.

    """

    def has_object_permission(self, request, view, obj):
        return obj.initiator == request.user or obj.receiver == request.user


class IsInitiatorOrReceiverMessagePermission(permissions.BasePermission):
    """
    Права для работы с сообщениями чатов.

    """

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return obj.sender == request.user
        return (obj.chat.initiator == request.user
                or obj.chat.receiver == request.user)
