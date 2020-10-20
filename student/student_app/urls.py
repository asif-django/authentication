"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('change_pwd', views.change_password, name="change_pwd"),
    path('user-details/<int:stu_id>/', views.user_details,
         name="user_details"),
    path('users-list/', views.users_list, name="users_list"),
    path('logout', views.user_logout, name="user_logout"),
]
