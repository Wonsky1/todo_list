from django.urls import path, include

from todo.views import (
    TaskListView, TaskCreateView,
    TagsListView, TagCreateView,
    change_status
)


urlpatterns = [
    path("", include("todo.urls", namespace="todo")),
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo"