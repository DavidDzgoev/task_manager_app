from django.urls import path

from . import views


urlpatterns = [
    path("task/", views.TaskListView.as_view()),
    path("task/<int:pk>/", views.TaskView.as_view()),
    path("task/my/", views.TaskUserView.as_view()),
    path("task/add/", views.TaskCreateView.as_view()),
    path("task/edit/<int:pk>/", views.TaskEditView.as_view()),
    path("task/delete/<int:pk>/", views.TaskDeleteView.as_view()),
    path('register/', views.RegisterView.as_view()),
]
