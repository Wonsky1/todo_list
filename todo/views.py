from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")



class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags-list")


class TagsListView(generic.ListView):
    model = Tag


def change_status(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse("todo:task-list"))
