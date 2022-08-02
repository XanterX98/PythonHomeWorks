from django.urls import path

from . import views

app_name = "mysite"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('course-details/<int:pk>/', views.course_details, name='course-details'),
]
