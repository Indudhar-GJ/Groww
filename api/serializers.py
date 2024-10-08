from rest_framework import serializers
from .models import *


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age', 'email']


class CourseChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseChapter
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    chapters = CourseChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'


class BoughtCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoughtCourses
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizAnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    option = serializers.CharField(max_length=200)


class QuizStatisticsSerializer(serializers.Serializer):
    date = serializers.DateField()
    number_of_quizzes = serializers.IntegerField()
