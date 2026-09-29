from django.shortcuts import render, redirect
from . models import Student

def home(request):
    if request.method == "POST":

        action = request.POST.get("action")

        if action == "add":
            name = request.POST.get("name")
            year_section = request.POST.get("year_section")
            course = request.POST.get("course")

            Student.objects.create(
                name=name,
                year_section=year_section,
                course=course,
            )

        elif action == "delete":
            student_id = request.POST.get("student_id")

            Student.objects.filter(id=student_id).delete()

        elif action == "clear":
            Student.objects.all().delete()

        return redirect("home")

    students = Student.objects.all()

    return render(request, "main/home.html", {
        "students":students
    })