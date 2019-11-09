from django.shortcuts import render, redirect
from myApp import models
from myApp.Helper.JsonHelper import JsonHelper
from django.http import HttpResponse
import face_recognition
import os
import base64

import json


class teacherStudent:
    def showStudent(self, request):
        stuObj = models.StudentInfo.objects.all()
        stuObjList = list()
        for item in stuObj:
            stuObjList.append(JsonHelper.json_serialize(item))
        return HttpResponse(
            json.dumps(stuObjList, ensure_ascii=False))

    def deleteStudent(self, request):
        stuId = request.POST.get('stuId')
        models.StudentInfo.objects.filter(stuId=stuId).delete()
        return HttpResponse("STUDENT_DELETE_SUCCESS")

    def __init__(self):
        global local_storage_path
        local_storage_path = "C:\\Users\\zhong\\Desktop\\temp\\"

    def addStudent(self,request):

        imgData = request.POST.get('imgData')
        stuName = request.POST.get('stuName')
        stuNumber = request.POST.get('stuNumber')

        if not imgData or not stuName or not stuNumber:
            return HttpResponse("PARAMS_NOT_FOUND")

        imgBinData = base64.b64decode(imgData)
        path = stuNumber + ".jpg"

        file = open(local_storage_path + path,"wb")

        file.write(imgBinData)
        file.close()


        # 识别是否有人脸
        try:
            image_unknow = face_recognition.load_image_file(local_storage_path + path)

            encoding_unknow = face_recognition.face_encodings(image_unknow)[0]

        except:
            return HttpResponse("NO_FACE_FOUND")


        try:
            models.StudentInfo.objects.create(stuId=stuNumber,stuName=stuName,stuImg=path)
            models.StudentLogin.objects.create(stuId=stuNumber,pwd="e10adc3949ba59abbe56e057f20f883e") # 默认密码123456
            return HttpResponse("ADD_STUDENT_SUCCESS")
        except:
            return HttpResponse("ADD_STUDENT_FAILED")

