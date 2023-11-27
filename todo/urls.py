from django.urls import path

from todo.views import (
    TaskListView, TaskCreateView,
    TagsListView, TagCreateView,
    change_status, TaskUpdateView,
    TaskDeleteView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("changestatus/<int:pk>/", change_status, name="task-change-status"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo"
