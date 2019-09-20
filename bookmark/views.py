from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

#bookmark/urls.py에서 call되는 method
def index(request):
    query = "select * from temp"
    cursor = connection.cursor()
    row = cursor.execute(query)
    rst = row.fetchone()

    # return(request, html파일 경로, template에서 사용될 dictionary data{name:data}
    # 실제 연결시킬 root이하 html파일 경로(url이 아님) 지정
    return render(request, 'index.html', {'result':rst})

def menu1(request):
    return render(request, 'menu/menu1.html')

def insert(request):
    print("ggg")
    ss = request.POST['bnid']
    bb = request.POST['bsid']

    query = "insert into temp(id, name)  values(\"%s\", \"%s\")" % (ss, bb)
    cursor = connection.cursor()
    print(query)
    cursor.execute(query)

    return render(request, 'index.html')

def qrcode(request):
    qr = "https://chart.googleapis.com/chart?cht=qr&chl=http://www.megabus.com?uid=32456744&chs=200x200"
    return render(request, 'menu/qrcode.html', {'qr': qr})

# Create your views here.
