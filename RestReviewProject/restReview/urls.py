from django.urls import path
from restReview import views


urlpatterns = [
    path('', views.home, name='home'),
    path('reviews/', views.ListReview.as_view(), name='reviews'),
    path('courses/', views.ListCreateCourse.as_view(), name='courses'),
    path('courses/<int:pk>/', views.RetriveUpdateDestroyCourse.as_view(),
         name='course_detail'),
    path('reviews/<int:pk>/', views.RetriveUpdateDestroyReview.as_view(),
         name='review_detail'),
]
