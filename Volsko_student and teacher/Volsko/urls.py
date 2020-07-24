"""Volsko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#from django.urls import path, include
from app.views import *
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('app.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url('accounts/signup/', SignUpView.as_view(), name='signup'),
    url('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    url('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    url(r'^logout/$',views.user_logout,name='logout'),

]
