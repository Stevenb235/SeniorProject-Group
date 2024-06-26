from django import forms
from .models import Task, AnimalComment, TaskComment, Animal, Worker


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "shelter",
            "assignee",
            "due_date",
            "animal",
            "required_role",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 3}),
            "completion_datetime": forms.DateInput(attrs={"type": "date"}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }

    task_item = forms.CharField(label="Task Item", max_length=400, required=True)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "completion_datetime",
            "assignee",
            "animal",
            "required_role",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 3}),
            "completion_datetime": forms.DateInput(attrs={"type": "date"}),
        }


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            "name",
            "color",
            "intake_type",
            "intake_date",
            "image",
            "age",
            "description",
            "sex",
            "ready_to_adopt",
            "shelter",
        ]
        widgets = {}


class CommentForm(forms.ModelForm):
    class Meta:
        fields = ["author", "comment" "date"]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 4, "cols": 50}),
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class AnimalCommentForm(forms.ModelForm):
    class Meta:
        fields = ["author", "comment" "date"]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 4, "cols": 50}),
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class TaskCommentForm(forms.ModelForm):
    class Meta:
        fields = ["author", "comment", "date"]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 4, "cols": 50}),
            "date": forms.DateInput(attrs={"type": "date"}),
        }


class AdoptionForm(forms.Form):
    name = forms.CharField(label="Full Name", max_length=400, required=True)
    phone_number = forms.CharField(label="Phone Number", max_length=20, required=True)
    email = forms.CharField(label="Email", max_length=300, required=True)
    address_one = forms.CharField(label="Address One", max_length=300, required=True)
    address_two = forms.CharField(label="Address Two", max_length=300, required=False)
    city = forms.CharField(label="City", max_length=300, required=True)
    state = forms.CharField(label="State", max_length=300, required=True)
    postal = forms.CharField(label="Postal", max_length=50, required=True)
    country = forms.CharField(label="Country", max_length=300, required=True)

class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=200, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), required=True)


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            "name",
            "username",
            "password",
            "role",
            "hire_date",
            "shelter",
            "address"
        ]
        widgets = {
            "hire_date": forms.DateInput(attrs={"type": "date"}),
            "title": forms.TextInput(attrs={"class": "form-control"})
        }