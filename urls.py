
from django.contrib import admin
from django.urls import path
from resources import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.resource_list, name='resource-list'),
    path('resource/new/', views.resource_create, name='resource-create'),
    path('resource/<int:pk>/edit/', views.resource_update, name='resource-update'),
    path('resource/<int:pk>/delete/', views.resource_delete, name='resource-delete'),
]
