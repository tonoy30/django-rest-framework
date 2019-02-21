from . import serializers
from . import models
from django.shortcuts import get_object_or_404
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


class ListCreateReview(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('pk'))
    # TODO: practice

    def perform_create(self, serializer):
        course = get_object_or_404(
            models.Course, pk=self.kwargs.get('pk')
        )
        serializer.save(course=course)


class RetriveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    # TODO: practice

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            course_id=self.kwargs.get('pk'),
            pk=self.kwargs.get('pk_1')
        )
