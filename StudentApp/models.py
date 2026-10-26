from django.db import models


class StudentDB(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)


class CourseDB(models.Model):
    course_name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()


class MarksDB(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=100)
    python = models.IntegerField()
    django = models.IntegerField()
    database = models.IntegerField()



# Create your models here.
