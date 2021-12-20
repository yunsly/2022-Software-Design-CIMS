
from django.contrib import admin
from django.urls import path
import cimsWeb.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cimsWeb.views.home, name='Home'), 

    path('region/', cimsWeb.views.region),
    path('socialDistanceLevel/', cimsWeb.views.socialDistanceLevel),
    path('socialDistanceLevel/level1', cimsWeb.views.level1),
    path('socialDistanceLevel/level2', cimsWeb.views.level2),
    path('socialDistanceLevel/level3', cimsWeb.views.level3),
    path('socialDistanceLevel/level4', cimsWeb.views.level4),
    
    path('startpage/', cimsWeb.views.startpage, name='startpage'),
    path('stageInfo/', cimsWeb.views.stageInfo, name='stageInfo'),
    path('currentStage/', cimsWeb.views.currentStage, name='currentStage'),
    path('localCoronic/', cimsWeb.views.localCoronic, name='localCoronic'),
    path('mypage/', cimsWeb.views.mypage, name='mypage'),
]
