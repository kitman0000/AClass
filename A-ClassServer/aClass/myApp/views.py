from myApp.service.Teacher import TeacherAccountService
from myApp.service.Teacher import TeacherHomeworkService
from myApp.service.Teacher import TeacherRollCallService
from myApp.service.Teacher import TeacherStudentService
from myApp.service.Students import StudentAccountService
from myApp.service.Students import StudentHomeworkService
from myApp.service.Students import StudentRollCallService
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

teacherAccount = TeacherAccountService.teacherAccount()
teacherHomework = TeacherHomeworkService.teacherHomework()
teacherRollCall = TeacherRollCallService.teacherRollCall()
teacherStudent = TeacherStudentService.teacherStudent()
studentAccount = StudentAccountService.studentAccount()
studentHomework = StudentHomeworkService.studentHomework()
studentRollCall = StudentRollCallService.studentRollCall()


@csrf_exempt
def studentLogin(request):
    return studentAccount.login(request)


@csrf_exempt
def teacherLogin(request):
    return teacherAccount.login(request)


@csrf_exempt
def studentCheckHomeworkByMonth(request):
    return studentHomework.month(request)


@csrf_exempt
def studentCheckHomeworkDetail(request):
    return studentHomework.detail(request)


@csrf_exempt
def studentCheckRollCall(request):
    return studentRollCall.detail(request)


@csrf_exempt
def teacherCheckRollCallDate(request):
    return teacherRollCall.date(request)


@csrf_exempt
def teacherCheckRollCallDetail(request):
    return teacherRollCall.detail(request)


@csrf_exempt
def studentChangePwd(request):
    return studentAccount.changePwd(request)


@csrf_exempt
def teacherChangePwd(request):
    return teacherAccount.changePwd(request)


@csrf_exempt
def teacherCheckHomeworkByMonth(request):
    return teacherHomework.month(request)


@csrf_exempt
def teacherCheckHomeworkDetail(request):
    return teacherHomework.detail(request)


@csrf_exempt
def teacherHomeworkScroing(request):
    return teacherHomework.scoring(request)


@csrf_exempt
def teacherAddHomework(request):
    return teacherHomework.addHomework(request)


@csrf_exempt
def teacherAddQuestion(request):
    return teacherHomework.addQuestion(request)


@csrf_exempt
def teacherAddStudent(request):
    return teacherStudent.addStudent(request)


@csrf_exempt
def teacherRollCalling(request):
    return teacherRollCall.rollCall(request)


@csrf_exempt
def studentCheckIdPwd(request):
    return studentAccount.checkIdPwd(request)


@csrf_exempt
def teacherCheckIdPwd(request):
    return teacherAccount.checkIdPwd(request)


@csrf_exempt
def teacherShowStudent(request):
    return teacherStudent.showStudent(request)

@csrf_exempt
def teacherDeleteStudent(request):
    return teacherStudent.deleteStudent(request)

@csrf_exempt
def teacherDoneQuestion(request):
    return teacherHomework.doneQuestion(request)


@csrf_exempt
def studentUploadHomework(request):
    return studentHomework.ulHomework(request)

@csrf_exempt
def teacherGetQuestionTitle(request):
    return teacherHomework.teacherGetQuestionTitle(request)

@csrf_exempt
def studentGetQuestionTitle(request):
    return teacherHomework.teacherGetQuestionTitle(request)

@csrf_exempt
def teacherStartRollCall(request):
    return teacherRollCall.startRollCall(request)