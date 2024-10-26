# mou_tracker/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mous import views

urlpatterns = [
    path('', views.mou_list, name='mou_list'),
    path('upload/', views.upload_mou, name='upload_mou'),
    path('filter_results/', views.filter_results, name='filter_results'),
    path('mou/<int:pk>/edit/', views.edit_mou, name='edit_mou'),
    path('mou/<int:pk>/delete/', views.delete_mou, name='delete_mou'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
