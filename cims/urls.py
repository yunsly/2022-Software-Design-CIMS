"""cims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import cimsWeb.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cimsWeb.views.home, name='Home'), 

    path('startpage/', cimsWeb.views.startpage, name='startpage'),
    path('stageInfo/', cimsWeb.views.stageInfo, name='stageInfo'),
    path('currentStage/', cimsWeb.views.currentStage, name='currentStage'),
    path('localCoronic/', cimsWeb.views.localCoronic, name='localCoronic'),
    path('mypage/', cimsWeb.views.mypage, name='mypage'),
    path('main/', cimsWeb.views.totalCoronic, name='main'),
    path('coronic/', cimsWeb.views.coronic, name='Coronic'),
]
