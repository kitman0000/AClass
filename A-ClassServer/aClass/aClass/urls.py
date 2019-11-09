"""aClass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from myApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url('api/student/account/login', views.studentLogin),
    url('api/teacher/account/login', views.teacherLogin),
    url('api/student/homework/month', views.studentCheckHomeworkByMonth),
    url('api/student/homework/detail', views.studentCheckHomeworkDetail),
    url('api/teacher/homework/month', views.teacherCheckHomeworkByMonth),
    url('api/teacher/homework/detail', views.teacherCheckHomeworkDetail),
    url('api/teacher/homework/scoring', views.teacherHomeworkScroing),
    url('api/teacher/homework/addHomework', views.teacherAddHomework),
    url('api/teacher/homework/addQuestion', views.teacherAddQuestion),
    url('api/student/rollCall/detail', views.studentCheckRollCall),
    url('api/teacher/rollCall/date', views.teacherCheckRollCallDate),
    url('api/teacher/rollCall/detail', views.teacherCheckRollCallDetail),
    url('api/student/account/changePwd', views.studentChangePwd),
    url('api/teacher/account/changePwd', views.teacherChangePwd),
    url('api/teacher/student/addStudent', views.teacherAddStudent),
    url('api/teacher/teacher/rollCall', views.teacherRollCalling),
    url('api/student/account/checkIdPwd', views.studentCheckIdPwd),
    url('api/teacher/account/checkIdPwd', views.teacherCheckIdPwd),
    url('api/teacher/student/showStudent', views.teacherShowStudent),
    url('api/teacher/student/deleteStudent', views.teacherDeleteStudent),
    url('api/teacher/homework/doneQuestion', views.teacherDoneQuestion),
    url('api/student/homework/ulHomework', views.studentUploadHomework),
    url('api/teacher/homework/getQuestionTitle',views.teacherGetQuestionTitle),
    url('api/student/homework/getQuestionTitle', views.studentGetQuestionTitle),
    url('api/teacher/rollCall/startRollCall', views.teacherStartRollCall)

]