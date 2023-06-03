from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index1"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name= "signup"),
    path('about/', views.about, name="about")
]