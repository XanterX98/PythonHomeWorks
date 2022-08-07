from django.urls import path

from . import views
from .views import CoursesListView, CourseDetailView

app_name = "mysite"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', CoursesListView.as_view(), name='courses'),
    path('course-details/<int:pk>/', CourseDetailView.as_view(), name="course-details"),
]
