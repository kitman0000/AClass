from django.shortcuts import render, redirect
from myApp import models
from django.http import HttpResponse
import face_recognition
import os
import base64
import time
from myApp.Helper.JsonHelper import JsonHelper

import json


class teacherRollCall:

    def __init__(self):
        global local_storage_path
        local_storage_path = "C:\\Users\\zhong\\Desktop\\temp\\"

    def date(self, request):
        dateObj = models.RollCallDate.objects.all()

        date_obj_list = list()
        for item in dateObj:
            date_obj_list.append(JsonHelper.json_serialize(item))

        return HttpResponse(
            json.dumps(date_obj_list, ensure_ascii=False))

    def detail(self, request):
        date = request.POST.get('date')
        rollCallObj = models.RollCallStuDetail.objects.filter(date=date)

        rollCallObjList = list()

        for item in rollCallObj:
            item.stuName = models.StudentInfo.objects.get(stuId=item.stuId).stuName
            rollCallObjList.append(JsonHelper.json_serialize(item))

        return HttpResponse(
            json.dumps(rollCallObjList, ensure_ascii=False))


    def rollCall(self,request):

        today_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        imgData = request.POST.get('imgData')
        imgBinData = base64.b64decode(imgData)

        tempFilePath = local_storage_path + time.time().__str__() + ".jpg"
        file = open(tempFilePath, "wb")
        file.write(imgBinData)
        file.close()

        # 识别
        image_unknow = face_recognition.load_image_file(tempFilePath)

        encoding_unknow = face_recognition.face_encodings(image_unknow)[0]

        student_list = models.StudentInfo.objects.all()
        for student in student_list:
            image_current = face_recognition.load_image_file(local_storage_path + student.stuImg)
            encoding_current = face_recognition.face_encodings(image_current)[0]
            result = face_recognition.compare_faces([encoding_current], encoding_unknow, tolerance=0.4)
            if result[0]:
                stu_name = student.stuName
                stu_id = student.stuId
                break

        else:
            return HttpResponse("NO_FACE_FOUND")

        roll_call_obj = models.RollCallStuDetail.objects.get(stuId=stu_id,date=today_date)
        if roll_call_obj.status:
            return HttpResponse("HAS_ROLL_CALL"+stu_name)
        roll_call_obj.status = "1"
        roll_call_obj.save()

        return HttpResponse(stu_name)


    def startRollCall(self,request):
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        models.RollCallDate.objects.create(date=date)
        stu_obj_list = models.StudentInfo.objects.all()
        for item in stu_obj_list:
            stu_id = item.stuId
            models.RollCallStuDetail.objects.create(stuId=stu_id,date=date,status=0)

        return HttpResponse("ROLLCALL_START_SUCCESS")
