from django.shortcuts import render
from .models import Animal, Task, AnimalTask

# Create your views here.

def animal_list(request):
    animal = Animal.objects.all()[:10]

    return render(request, "animals.html", {
        'animals' : animal
    })


def worker_dash(request):
    tasks = Task.objects.all()
    return render(
        request,
        "worker_dashboard.html",
        {
            "tasks": tasks,
        },
    )

def about_view(request):
    return render(request, 'about.html')
