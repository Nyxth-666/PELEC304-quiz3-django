from django.shortcuts import render
from . models import Student

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        year_section = request.POST.get("year_section")
        course = request.POST.get("course")

        Student.objects.create(
            name=name,
            year_section=year_section,
            course=course,
        )

    students = Student.objects.all()

    return render(request, "main/home.html", {
        "students":students
    })