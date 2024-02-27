from django.urls import path
from .views import madlib_form, madlib_result
from . import views

urlpatterns = [
    path('', madlib_form, name='madlib_form'),
    path('result/<int:pk>/', madlib_result, name='madlib_result'),
    path('submit_madlib/', views.submit_madlib, name='submit_madlib'),
]
