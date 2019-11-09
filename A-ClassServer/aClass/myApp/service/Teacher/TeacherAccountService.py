from django.shortcuts import render, redirect
from myApp import models
from django.http import HttpResponse
import json


class teacherAccount:
    def login(self, request):
        teacherId = request.POST.get('teacherId')
        pwd = request.POST.get('pwd')
        try:
            teacherObj = models.TeacherLogin.objects.get(teacherId=teacherId)
            if pwd == teacherObj.pwd:
                return HttpResponse(teacherId)
            else:
                return HttpResponse("PWD_WRONG")
        except:
            return HttpResponse("TEACHERID_WRONG")

    def changePwd(self, request):
        teacherId = request.POST.get('teacherId')
        oldPwd = request.POST.get('oldPwd')
        newPwd = request.POST.get('newPwd')
        teacherObj = models.TeacherLogin.objects.get(teacherId=teacherId)
        if oldPwd == teacherObj.pwd:
            teacherObj.pwd = newPwd
            teacherObj.save()
            return HttpResponse("PWD_CHANGE_SUCESS")
        else:
            return HttpResponse("PWD_CHANGE_FAILED")

    def checkIdPwd(self, request):
        teacherId = request.POST.get('teacherId')
        pwd = request.POST.get('pwd')
        try:
            teacherObj = models.TeacherLogin.objects.get(teacherId=teacherId)
            if pwd == teacherObj.pwd:
                request.session['teacherId'] = teacherId
                return HttpResponse("CHECK_SUCCESS")
            else:
                return HttpResponse("CHECK_FAILED")
        except:
            return HttpResponse("CHECK_FAILED")
