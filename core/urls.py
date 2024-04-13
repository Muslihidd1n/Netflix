from django.contrib import admin
from django.urls import path

from film.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloApi.as_view()),
    path('aktyorlar/', AktyorlarAPI.as_view()),
    path('kinolar/', KinolarAPI.as_view()),
    path('tariflar/', TariflarAPI.as_view()),


    path('aktyorlar/<int:pk>/', AktyorAPI.as_view()),
    path('kinolar/<int:pk>/',  KinoAPI.as_view()),
    path('kinolar/<int:pk>/aktyorlar',  KinoAktyorlarAPI.as_view()),
    path('aktyorlar/<int:pk>/kinolar',  AktyorKinolarAPI.as_view()),
    path('tariflar/<int:pk>/', TarifAPI.as_view()),

]
