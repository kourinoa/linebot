from django.urls import path
from mytest import views

urlpatterns = [
    path("", views.index, name="index"),  # 設定訪問/mytest，執行views 裏面的index method
    path("callback/", views.callback, name="callback"),
]
