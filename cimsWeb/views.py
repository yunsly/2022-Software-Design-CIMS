from django.shortcuts import render

# Create your views here.

def stageInfo(request):
    return render(request,'stageInfo.html')

def mypage(request):
    return render(request, 'mypage.html')

