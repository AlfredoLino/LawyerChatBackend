from django.urls import path
from lawchat import views

urlpatterns = [
    path('', views.main),
    path('about/', views.about)
]