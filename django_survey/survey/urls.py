from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
  path('register/', views.RegisterView.as_view(), name='register'),
  path('signin/', auth_views.LoginView.as_view(template_name='survey/signin.html'), name='signin'),
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('signout/', auth_views.LogoutView.as_view(), name='signxout'),
  path('surveys/create/', views.SurveyCreateView.as_view(), name='survey_create'),
]