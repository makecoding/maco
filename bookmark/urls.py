from django.urls import path
from . import views

urlpatterns = [
    #(실제 root이하의 web url (html 파일 위치가 아님), views.py의 메서드, ??)
    # http://127.0.0.1:8000/bookmark/
    path('', views.index, name='index'),

    # http://127.0.0.1:8000/menu/menu1 (아래 내용과 접근 url만 다를 뿐 매핑되는 html파일은 동일함)
    path('menu/menu1', views.menu1, name='menu1'),
    # http://127.0.0.1:8000/menu/menu1.html (위의 내용과 접근 url만 다를 뿐 매핑되는 html파일은 동일함)
    #path('menu/menu1.html', views.menu1, name='menu1'),

    path('menu/insertform', views.insertform, name='insertform'),
    path('menu/insert', views.insert, name='insert'),

    path('menu/login', views.login, name='login'),

    path('menu/qrcode', views.qrcode, name='qrcode'),

    path('menu/getstop', views.getstop.as_view(), name='getstop'),
]
