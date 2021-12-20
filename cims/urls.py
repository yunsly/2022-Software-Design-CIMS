
from django.contrib import admin
from django.urls import path
import cimsWeb.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cimsWeb.views.home, name='Home'), 

    path('region/', cimsWeb.views.region),
    path('stageInfo/level1', cimsWeb.views.level1),
    path('stageInfo/level2', cimsWeb.views.level2),
    path('stageInfo/level3', cimsWeb.views.level3),
    path('stageInfo/level4', cimsWeb.views.level4),
    
    path('startpage/', cimsWeb.views.startpage, name='startpage'),
    path('stageInfo/', cimsWeb.views.stageInfo, name='stageInfo'),
    path('currentStage/', cimsWeb.views.currentStage, name='currentStage'),
    path('localCoronic/', cimsWeb.views.localCoronic, name='localCoronic'),
    path('mypage/', cimsWeb.views.mypage, name='mypage'),
]
