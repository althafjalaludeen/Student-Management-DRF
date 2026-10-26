from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from StudentApp.models import StudentDB, CourseDB, MarksDB
from StudentApp.serializers import (
    StudentDBSerializer,
    CourseDBSerializer,
    MarksDBSerializer
)


class StudentGradeView(APIView):

    def post(self, request):
        name = request.data.get('name')
        mark1 = request.data.get('mark1')
        mark2 = request.data.get('mark2')
        mark3 = request.data.get('mark3')

        total = mark1 + mark2 + mark3
        percentage = total / 3

        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B'
        elif percentage >= 60:
            grade = 'C'
        elif percentage >= 50:
            grade = 'D'
        else:
            grade = 'F'

        if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
            status = 'Pass'
        else:
            status = 'Fail'

        return Response({
            'student_name': name,
            'total_marks': total,
            'percentage': round(percentage, 2),
            'grade': grade,
            'status': status
        })


class StudentListCreateView(APIView):

    def get(self, request):
        qs = StudentDB.objects.all().values()
        serializer = StudentDBSerializer(qs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = StudentDBSerializer(data=form_data)

        if serializer_instance.is_valid():
            original_data = serializer_instance.validated_data
            StudentDB.objects.create(**original_data)

            return Response(data={
                'message': 'Student added successfully'
            })
        else:
            return Response(data={
                'message': 'Invalid data',
                'errors': serializer_instance.errors
            })


class CourseListCreateView(APIView):

    def get(self, request):
        qs = CourseDB.objects.all().values()
        serializer = CourseDBSerializer(qs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = CourseDBSerializer(data=form_data)

        if serializer_instance.is_valid():
            original_data = serializer_instance.validated_data
            CourseDB.objects.create(**original_data)

            return Response(data={
                'message': 'Course added successfully'
            })
        else:
            return Response(data={
                'message': 'Invalid data',
                'errors': serializer_instance.errors
            })


class MarksListCreateView(APIView):

    def get(self, request):
        qs = MarksDB.objects.all().values()
        serializer = MarksDBSerializer(qs, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = MarksDBSerializer(data=form_data)

        if serializer_instance.is_valid():
            original_data = serializer_instance.validated_data
            MarksDB.objects.create(**original_data)

            return Response(data={
                'message': 'Marks added successfully'
            })
        else:
            return Response(data={
                'message': 'Invalid data',
                'errors': serializer_instance.errors
            })
