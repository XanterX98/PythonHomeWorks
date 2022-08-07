from django.db import models


class CourseCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__} #{self.pk} {self.name!r}>"


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__} #{self.pk} {self.name!r}>"


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(null=True)
    views = models.PositiveSmallIntegerField(default=0)
    likes = models.PositiveSmallIntegerField(default=0)
    is_popular = models.BooleanField(default=False)
    category = models.ForeignKey(CourseCategory, on_delete=models.RESTRICT)
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__} #{self.pk} {self.name!r}>"
