from django.shortcuts import render, redirect
from . models import Student
import re

def home(request):
    if request.method == "POST":

        action = request.POST.get("action")

        if action == "add":
            name = request.POST.get("name", "").strip()
            year_section = request.POST.get("year_section", "").strip()
            course = request.POST.get("course", "").strip()

            if not name or not year_section or not course:
                students = Student.objects.all()

                return render(request, "main/home.html", {
                    "students": students,
                    "error": "All fields are required.",
                })

            if not re.match(r"^[1-4][A-Za-z]$", year_section):
                students = Student.objects.all()

                return render(request, "main/home.html", {
                    "students": students,
                    "error": "Year & Section must be a valid data.",
                })

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
        "students": students,
    })