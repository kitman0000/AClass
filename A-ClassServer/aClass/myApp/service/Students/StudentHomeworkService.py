from django.shortcuts import render, redirect
from myApp import models
from myApp.Helper.JsonHelper import JsonHelper
from django.http import HttpResponse
from django import forms
import time
import json


class studentHomework:
    def month(self, request):
        month = request.POST.get("month")
        month = "-" + month + "-"
        homeworkObj = models.HomeworkByMonth.objects.filter(uploadDate__icontains=month)
        homeworkObjList = list()

        for item in homeworkObj:
            homeworkObjList.append(JsonHelper.json_serialize(item))
        return HttpResponse(
            json.dumps(homeworkObjList, ensure_ascii=False))

    def detail(self, request):
        homeworkId = request.POST.get("homeworkId")
        stuId = request.POST.get("stuId")
        homeworkObj1 = models.HomeworkDetail.objects.filter(homeworkId=homeworkId)
        homeworkObjList1 = list()
        for item in homeworkObj1:
            homeworkObj2 = models.StudentUploadInfo.objects.get(stuId=stuId, questionId=item.id)
            item.status = homeworkObj2.status
            item.mark= homeworkObj2.mark
            homeworkObjList1.append(JsonHelper.json_serialize(item))
        return HttpResponse(
            json.dumps(homeworkObjList1, ensure_ascii=False))

    def handle_uploaded_file(self,f):
        file_name = '/static/upload/'+time.time().__str__()+'.zip'

        with open("myApp" + file_name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return file_name

    def ulHomework(self, request):
        stuId = request.POST.get("stuId")
        questionId = request.POST.get("questionId")

        file_path = self.handle_uploaded_file(request.FILES['uploadFile'])

        stu_upload_obj = models.StudentUploadInfo.objects.get(stuId=stuId,questionId=questionId)
        stu_upload_obj.filePath = file_path
        stu_upload_obj.status = 1
        stu_upload_obj.save()

        return HttpResponse("HOMEWORK_UPLOAD_SUCCESS")


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()