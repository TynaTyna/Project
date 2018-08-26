from django.urls import path
from .views import new_course, edit_course


urlpatterns = [
    path('new/', new_course),
    path('edit/<int:course_id>/', edit_course),
]
