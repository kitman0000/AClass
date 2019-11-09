from django.shortcuts import render, redirect
from myApp import models
from django.http import HttpResponse
import json
from myApp.Helper.JsonHelper import JsonHelper


class studentRollCall:
    def detail(self, request):
        stuId = request.POST.get('stuId')
        rollCallObj = models.RollCallStuDetail.objects.filter(stuId=stuId)

        rollCallObjList = list()

        for item in rollCallObj:
            item.stuName = models.StudentInfo.objects.get(stuId=item.stuId).stuName
            rollCallObjList.append(JsonHelper.json_serialize(item))

        return HttpResponse(
            json.dumps(rollCallObjList, ensure_ascii=False))