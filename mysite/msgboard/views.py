from django.shortcuts import render
from msgboard import models
import datetime
from msgboard.models import Msg

msglist = [
    {"username": "xk", "msg": "hehe", "time": "2018"},
    {"username": "xek", "msg": "h2", "time": "2017"},
]


# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        msg = request.POST.get("msg", None)
        date = datetime.datetime.now()
        print(username, msg, date)
        # msglist.append({"username": username, "msg": msg, "time": date})
        # 保存在数据库
        # models.Msg.objects.create(username=username, msg=msg, time=date)
        saveMsg(username, msg, date)
    msglist = models.Msg.objects.all()

    return render(request, "index.html", {"data": msglist})


def saveMsg(username, msg, date):
    s = Msg(username=username, msg=msg, time=date)
    s.save()
