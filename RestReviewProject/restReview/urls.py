from django.urls import path
from restReview import views


urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.ListCreateCourse.as_view(), name='courses'),
    path('courses/<str:pk>/', views.RetriveUpdateDestroyCourse.as_view(),
         name='course_detail'),
    path('courses/<str:pk>/reviews/',
         views.ListCreateReview.as_view(), name='review_list'),
    path('courses/<str:pk>/reviews/<pk_1>/',
         views.RetriveUpdateDestroyReview.as_view(), name='review_detail'),
]
