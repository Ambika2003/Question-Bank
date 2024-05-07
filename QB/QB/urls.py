"""
URL configuration for QB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from QuestionPractice import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('log/',views.userlogin,name='userlogin'),
    path('after/',views.afterlogin,name='afterlogin'),
    path('question/', views.mcq_question_view, name='mcq_question'),
    path('question1/', views.mcq_question_Science, name='mcq_question_science'),
    path('question2/', views.mcq_question_aptitude, name='mcq_question_aptitude'),
    # path('totalmarks/',views.submit_mcq,name='result'),
    

]
