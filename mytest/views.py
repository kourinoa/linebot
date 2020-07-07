from django.shortcuts import render


# Create your views here.

# 進入index執行的method
def index(request):
    pdata = {"num": 2, "word": "hellow"}
    return render(request, "index.html", context=pdata)
