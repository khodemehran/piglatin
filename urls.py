from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = 'home'),
    path('translate/', views.translate, name = 'translate'),
    path('about/', views.about, name = 'about')
    
]
