from django.shortcuts import render


# Create your views here.

# 進入index執行的method
def index(request):
    pdata = {"num": 2, "word": "hellow"}
    print("get request :", request)
    return render(request, "index.html", context=pdata)


def callback(request):
    print("call back request:", request)
    pdata = {"num": 2, "word": "callback"}
    return render(request, "index.html", context=pdata)
