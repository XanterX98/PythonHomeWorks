from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpRequest

from .models import Course


def index(request: HttpRequest):
    popular_courses = Course\
        .objects\
        .select_related("category", "teacher")\
        .order_by("id")\
        .all()\
        .filter(is_popular=True)
    context = {
        "courses": popular_courses,
    }
    return render(request, "mysite/index.html", context=context)


def about(request: HttpRequest):
    context = {
        "page_title": "About Us",
        "white_header": True,
    }
    return render(request, "mysite/about-us.html", context=context)


def contact(request: HttpRequest):
    context = {
        "page_title": "Contact Us",
        "white_header": True,
    }
    return render(request, "mysite/contact.html", context=context)


def courses(request: HttpRequest):
    all_courses = Course.objects.select_related("category", "teacher").order_by("id").all()
    context = {
        "page_title": "All courses",
        "white_header": True,
        "courses": all_courses,
    }
    return render(request, "mysite/courses.html", context=context)


def course_details(request: HttpRequest, pk: int):
    course = get_object_or_404(
        Course.objects.select_related("category", "teacher"),
        pk=pk,
    )
    context = {
        "page_title": course.name,
        "white_header": True,
        "course": course,
    }
    return render(request, "mysite/course-details.html", context=context)
