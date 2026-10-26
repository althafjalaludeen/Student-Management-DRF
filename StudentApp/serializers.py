from rest_framework import serializers
from StudentApp.models import StudentDB, CourseDB, MarksDB


class StudentDBSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    place = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15)
    course = serializers.CharField(max_length=100)


class CourseDBSerializer(serializers.Serializer):
    course_name = serializers.CharField(max_length=100)
    university = serializers.CharField(max_length=100)
    duration = serializers.CharField(max_length=50)
    department = serializers.CharField(max_length=100)
    semester = serializers.IntegerField()


class MarksDBSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    python = serializers.IntegerField()
    django = serializers.IntegerField()
    database = serializers.IntegerField()

