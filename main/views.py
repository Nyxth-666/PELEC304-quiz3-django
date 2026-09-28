from django.shortcuts import render
from .models import Student

def Home(request):
    students = Student.objects.all()
    return render(request, 'main/home.html', {'students': students})