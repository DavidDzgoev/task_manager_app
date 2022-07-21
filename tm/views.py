from rest_framework import permissions, generics
from rest_framework.permissions import AllowAny

from .models import Task, User
from .serializers import (
    TaskListSerializer,
    TaskDetailSerializer,
    TaskCreateSerializer,
    TaskDeleteSerializer,
    RegisterSerializer
)


class TaskListView(generics.ListAPIView):
    """Returns list of all tasks"""

    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAdminUser]


class TaskView(generics.RetrieveAPIView):
    """Returns specific task"""

    queryset = Task.objects.filter()
    serializer_class = TaskDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskCreateView(generics.CreateAPIView):
    """Creates new task"""

    serializer_class = TaskCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskEditView(generics.UpdateAPIView):
    """Edits existed task"""

    serializer_class = TaskCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner__in=[self.request._user])


class TaskDeleteView(generics.DestroyAPIView):
    """Deletes existed task"""

    serializer_class = TaskDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner__in=[self.request._user])


class TaskUserView(generics.ListAPIView):
    """Returns list of user tasks"""

    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request._user)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
