from django.shortcuts import render, redirect
from myApp import models
from django.http import HttpResponse
import json

class studentAccount:
    def login(self, request):
        stuId = request.POST.get('stuId')
        pwd = request.POST.get('pwd')
        try:
            stuObj = models.StudentLogin.objects.get(stuId=stuId)
            if pwd == stuObj.pwd:
                return HttpResponse(stuId)
            else:
                return HttpResponse("PWD_WRONG")
        except:
            return HttpResponse("STUID_WRONG")

    def changePwd(self, request):
        stuId = request.POST.get('stuId')
        oldPwd = request.POST.get('oldPwd')
        newPwd = request.POST.get('newPwd')
        stuObj = models.StudentLogin.objects.get(stuId=stuId)
        print(oldPwd == stuObj.pwd)
        if oldPwd == stuObj.pwd:
            stuObj.pwd = newPwd
            stuObj.save()
            return HttpResponse("PWD_CHANGE_SUCCESS")
        else:
            return HttpResponse("PWD_CHANGE_FAILED")

    def checkIdPwd(self, request):
        stuId = request.POST.get('stuId')
        pwd = request.POST.get('pwd')
        try:
            stuObj = models.StudentLogin.objects.get(stuId=stuId)
            if pwd == stuObj.pwd:
                request.session['stuId'] = stuId
                return HttpResponse("CHECK_SUCCESS")
            else:
                return HttpResponse("CHECK_FAILED")
        except:
            return HttpResponse("CHECK_FAILED")