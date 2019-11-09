from django.db import models
import json


# Create your models here.
class HomeworkByMonth(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    uploadDate = models.TextField()
    destDate = models.TextField()
    teacher = models.TextField()
    teacherId = models.TextField()

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class HomeworkDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    homeworkId = models.IntegerField()
    timespan = models.TextField(30)

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class StudentLogin(models.Model):
    id = models.IntegerField(primary_key=True)
    stuId = models.TextField()
    pwd = models.TextField()

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class TeacherLogin(models.Model):
    id = models.IntegerField(primary_key=True)
    teacherId = models.TextField()
    pwd = models.TextField()

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class RollCallDate(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.TextField()

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class RollCallStuDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    stuId = models.TextField()
    date = models.TextField()
    status = models.BooleanField()
    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class StudentInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    stuId = models.TextField()
    stuName = models.TextField()
    stuImg = models.TextField()

class StudentUploadInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    stuId = models.TextField()
    questionId = models.IntegerField()
    filePath = models.TextField()
    mark = models.IntegerField(default=-1)
    status = models.BooleanField(default=0)


