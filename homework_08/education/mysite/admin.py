from django.contrib import admin

from .models import Course, CourseCategory, Teacher


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name')


admin.site.register(Teacher)
admin.site.register(CourseCategory)
admin.site.register(Course, CourseAdmin)
