from django.urls import path
from restReview import views


urlpatterns = [
    path('', views.home, name='home'),
    path('reviews/', views.ListReview.as_view(), name='reviews'),
    path('courses/', views.ListCourse.as_view(), name='courses'),
]
