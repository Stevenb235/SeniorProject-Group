"""
URL configuration for pawplan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from core import views
from django.conf.urls.static import static
from core import views
from django.conf import settings

urlpatterns = [
    # Partials URLS
    path("admin/", admin.site.urls),
    path("animal_list", views.animal_list, name="animal_list"),
    path("animal/<int:pet_id>", views.animal, name="animal"),
    path("animals", views.animals, name="animals"),
    path("dashboard/", views.worker_dash, name="worker_dash"),
    path("", views.home, name="home"),
    path("about/", views.about_view, name="about"),
    path("adopt/", views.adapt, name="adopt"),
    path("animal/adoption/<int:pet_id>", views.adoption, name="adoption"),
    path("filter_tasks/", views.filter_tasks, name="filter_tasks"),
    path("sort_tasks/", views.sort_tasks, name="sort_tasks"),
    path("animal/add", views.add_animal, name="add_animal"),
    path("animal/edit/<int:pet_id>", views.edit_animal, name="edit_animal"),
    path("animal/delete/<int:pet_id>", views.delete_animal, name="delete_animal"),
    path("filter_animals/", views.filter_animals, name="filter_animals"),
    path("sort_animals/", views.sort_animals, name="sort_animals"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("task/add/", views.add_task, name="add_task"),
    path("task/edit/<int:task_id>/", views.edit_task, name="edit_task"),
    path("task/delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("task/complete/<int:task_id>/", views.complete_task, name="complete_task"),
    path("task/release/<int:task_id>/", views.release_task, name="release_task"),
    path("volunteer/", views.volunteer_form, name="volunteer_form"),
    path(
        "add_task_comment/<int:task_id>/",
        views.add_task_comment,
        name="add_task_comment",
    ),
    path(
        "add_animal_comment/<int:pet_id>/",
        views.add_animal_comment,
        name="add_animal_comment",
    ),
    path(
        "api/tasks/calendar/", views.get_tasks_for_calendar, name="get_calendar_tasks"
    ),
    path("dashboard/calendar/", views.task_calendar, name="task_calendar"),
    path(
        "display_all_comments/", views.display_all_comments, name="display_all_comments"
    ),
    path("task_items/", views.task_items, name="task_items"),
    path("complete_item/<int:item_id>", views.complete_item, name="complete_item"),
    path("swap_task/<int:task_id>", views.swap_task, name="swap_task"),
    path("manage_employees/", views.worker_dash, name="manage_employees"),
    path("manage_shelter_info/", views.worker_dash, name="manage_shelter_info"),
    path("animal/adoption/<int:pet_id>", views.adoption, name="adoption"),
    path("worker/add", views.add_worker, name="add_worker"),
    path("worker/edit/<int:worker_id>", views.edit_worker, name="edit_worker"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
