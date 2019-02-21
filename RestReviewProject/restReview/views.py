from . import serializers
from . import models
from rest_framework import generics
from django.shortcuts import render
# Create your views here.


def home(request):
    courses = models.Course.objects.all()
    return render(request, 'home.html', {'course_list': courses})


class ListCreateCourse(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CouseSerializer


class RetriveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CouseSerializer


class ListReview(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class RetriveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
