from django.urls import path, include
from . import views

urlpatterns = [
    path('txt/', views.default),
    path('image/',views.imganalyze),
    path('summarize/',views.summarize),
    path('audio/',views.tta),
    path('translate_file/',views.ppt_convert)
]