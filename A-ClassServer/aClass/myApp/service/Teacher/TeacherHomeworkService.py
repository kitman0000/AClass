from django.shortcuts import render, redirect
from myApp import models
from myApp.Helper.JsonHelper import JsonHelper
from django.http import HttpResponse
import time
import json

class teacherHomework:
    def month(self, request):
        month = request.POST.get("month")
        teacherId = request.POST.get('teacherId')
        month = "-" + month + "-"
        homeworkObj = models.HomeworkByMonth.objects.filter(uploadDate__icontains=month, teacherId=teacherId)
        homeworkObjList = list()

        for item in homeworkObj:
            homeworkObjList.append(JsonHelper.json_serialize(item))

        return HttpResponse(
            json.dumps(homeworkObjList, ensure_ascii=False))

    def detail(self, request):
        homeworkId = request.POST.get("homeworkId")
        homeworkObj = models.HomeworkDetail.objects.filter(homeworkId=homeworkId)
        homeworkObjList = list()

        for item in homeworkObj:
            homeworkObjList.append(JsonHelper.json_serialize(item))

        return HttpResponse(
            json.dumps(homeworkObjList, ensure_ascii=False))

    def scoring(self, request):
        questionid = request.POST.get("questionId")
        mark = request.POST.get("mark")
        teacherId = request.POST.get("teacherId")
        pwd = request.POST.get("pwd")
        stuId = request.POST.get("stuId")
        try:
            teacherObj = models.TeacherLogin.objects.get(teacherId=teacherId, pwd=pwd)
            try:
                homeworkObj = models.StudentUploadInfo.objects.get(questionId=questionid, stuId=stuId)
                homeworkObj.mark = mark
                homeworkObj.save()

                return HttpResponse("SCORED_SUCCESS")
            except:
                raise
                return HttpResponse("SCORED_FAILED")
        except:
            raise
            return HttpResponse("GUN")

    def addHomework(self, request):
        name = request.POST.get("name")
        uploadDate = request.POST.get("uploadDate")
        destDate = request.POST.get("destDate")
        teacherId = request.POST.get("teacherId")
        pwd = request.POST.get("pwd")
        try:
            teacherObj = models.TeacherLogin.objects.get(teacherId=teacherId, pwd=pwd)

            try:
                models.HomeworkByMonth.objects.create(name=name, uploadDate=uploadDate,
                                                        destDate=destDate, teacherId=teacherId)
                homeworkObj = models.HomeworkByMonth.objects.get(name=name)
                id = homeworkObj.id
                return HttpResponse(id)
            except:
                return HttpResponse("ADD_HOMEWORK_FAILED")
        except:
            return HttpResponse("GUN")


    def addQuestion(self, request):
        homeworkId = request.POST.get("homeworkId")
        title = request.POST.get("title")
        teacherId = request.POST.get('teacherId')
        pwd = request.POST.get('pwd')
        time_span = time.time().__str__()
        try:
            teacherObj = models.TeacherLogin.objects.get(teacherId=teacherId, pwd=pwd)
            try:
                models.HomeworkDetail.objects.create(homeworkId=homeworkId, title=title,timespan=time_span)
                question_id = models.HomeworkDetail.objects.get(timespan=time_span).id

                stu_obj_list = models.StudentInfo.objects.all()
                for item in stu_obj_list:
                    stu_id = item.stuId
                    models.StudentUploadInfo.objects.create(stuId=stu_id,questionId=question_id)

                return HttpResponse("ADD_QUESTION_SUCCESS")
            except:
                raise
        except:
            raise

    def doneQuestion(self, request):
        questionid = request.POST.get("questionId")
        homeworkObj = models.StudentUploadInfo.objects.filter(questionId=questionid)
        homeworkObjList = list()
        for item in homeworkObj:
            stuObj = models.StudentInfo.objects.get(stuId=item.stuId)
            item.stuName=stuObj.stuName
            homeworkObjList.append(JsonHelper.json_serialize(item))

        return HttpResponse(
            json.dumps(homeworkObjList, ensure_ascii=False))

    def teacherGetQuestionTitle(self,request):
        questionid = request.POST.get("questionId")
        title = models.HomeworkDetail.objects.get(id=questionid).title

        return HttpResponse(title)



