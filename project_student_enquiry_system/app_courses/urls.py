from django.urls import path
from app_courses import views

urlpatterns = [
    path('list/', views.course_index, name ='course-index'),
    path('create/', views.course_create, name='course-create'),
    path('edit/', views.course_edit, name='course-edit'),
    path('show/', views.course_show, name='course-show'),
]