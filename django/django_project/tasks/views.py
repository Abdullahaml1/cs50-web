from django.shortcuts import render

tasks_list = ["read", "write", "speak"]

# Create your views here.

def index(request):
    context = {"tasks_list": tasks_list}
    return render(request, "tasks/index.html", context)


def add(request):
    return render(request, "tasks/add.html")
