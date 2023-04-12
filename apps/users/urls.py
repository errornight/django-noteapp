from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='DashboardPage'),
    path('signup/', views.signup_user, name='SignupPage'),
    path('login/', views.login_user, name='LoginPage'),
    path('edit/', views.edit_profile, name='EditProfilePage'),
    path('logout/', views.log_out, name='LogoutPage')

]