from django.db import connection
from django.shortcuts import render

from urllib.parse import *
from urllib.request import *

from rest_framework.response import Response
from rest_framework.views import APIView

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

def insertform(request):
    return render(request, 'menu/insert.html')

def insert(request):
    ss = request.POST['bnid']
    bb = request.POST['bsid']

    #mid = Article.objects.filter(id=ss,pw=bb)

    query = "insert into temp(id, name)  values('%s', '%s')" % (ss, bb)
    cursor = connection.cursor()
    cursor.execute(query)

    return render(request, 'index.html')

def login(request):
    uid = request.POST['uid']
    upw = request.POST['upw']

    #mid = Article.objects.filter(id=ss,pw=bb)

    query = "select count(*) from temp where id='%s' and name='%s' " % (uid, upw)
    cursor = connection.cursor()
    row = cursor.execute(query)
    cnt = row.fetchone()

    if (cnt==1):
        print("로그인 성공!!!")

    else :
        print("로그인 실패!!!")


    return render(request, 'index.html')

def qrcode(request):
    qr = "https://chart.googleapis.com/chart?cht=qr&chl=http://www.megabus.com?uid=32456744&chs=200x200"
    return render(request, 'menu/qrcode.html', {'qr': qr})

class getstop(APIView):

    def get(self, request, format=None):
        # slong = request.POST['stoplong']
        # slati = request.POST['stoplati']


        url = 'http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getCrdntPrxmtSttnList'
        queryParams = '?' + urlencode(
            {quote_plus('ServiceKey'): 'WS6IE%2F0nHkArdmPt3284YdVVLGtZPSuSQ0ANuFo463Hj3KU9zb7RpSz5hJHWQpWw0sE0Vbz9V4f7zBSdO7%2FR1A%3D%3D', quote_plus('gpsLati'): '36.3', quote_plus('gpsLong'): '127.3'})

        req = Request(url + queryParams)
        req.get_method = lambda: 'GET'
        response_body = urlopen(req).read()

        print(response_body)

        return Response(response_body)

    #return render(request, 'index.html')

# Create your views here.
