from django.shortcuts import render

from .models import CoronicStatusOfRegion, CoronicStatusOfKorea

# Create your views here.
def home(request):
    return render(request, 'home.html')

def startpage(request):
    total = CoronicStatusOfKorea.objects.all()
    context = {'total': total}
    return render(request, 'startpage.html', context)

def stageInfo(request):
    return render(request,'stageInfo.html')

def currentStage(request):
    return render(request, 'currentStage.html')

def localCoronic(request):
    coronic = CoronicStatusOfRegion.objects.all()
    context = {'coronic':coronic}
    return render(request, 'localCoronic.html', context)


def mypage(request):
    return render(request, 'mypage.html')

