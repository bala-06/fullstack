# mous/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mou_list, name='mou_list'),
    path('upload/', views.upload_mou, name='upload_mou'),
    path('activity/<int:activity_id>/complete/', views.complete_outcome, name='complete_outcome'),
]
