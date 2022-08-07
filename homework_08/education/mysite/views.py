from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpRequest

from .models import Course
from django.views.generic import ListView, DetailView, DeleteView, CreateView


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


class CoursesListView(ListView):
    # model = Animal
    queryset = Course.objects.select_related("category", "teacher").order_by("id").all()
    context_object_name = "courses"
    template_name = "mysite/courses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'All courses'
        context["white_header"] = True
        return context


class CourseDetailView(DetailView):
    queryset = Course.objects.select_related("category", "teacher")
    template_name = "mysite/course-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.object.name
        context["white_header"] = True
        return context
