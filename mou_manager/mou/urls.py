from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_mou, name='create_mou'),
    path('', views.mou_list, name='mou_list'),
    path('mou/<int:mou_id>/add_event/', views.add_event, name='add_event'),
    path('view/<int:mou_id>/', views.view_mou, name='view_mou'),
    path('edit/<int:mou_id>/', views.edit_mou, name='edit_mou'),
    path('delete/<int:mou_id>/', views.delete_mou, name='delete_mou'),
    path('mou/<int:mou_id>/add_event/', views.add_event, name='add_event'),
    path('event/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('filter/', views.filter_mou, name='filter_mou'),
    

]