from . import serializers
from . import models
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


class ListCourse(APIView):
    def get(self, request, format=None):
        courses = models.Course.objects.all()
        serializer = serializers.CouseSerializer(courses, many=True)
        return Response(serializer.data)


class ListReview(APIView):
    def get(self, request, format=None):
        reviews = models.Review.objects.all()
        serializer = serializers.ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
