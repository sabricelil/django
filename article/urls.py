from django.contrib import admin
from django.urls import path
from . import views

app_name="article"


urlpatterns=[

    path('kontrolpaneli/',views.kontrolpaneli, name="kontrolpaneli"),
    path('makale_ekle/',views.makale_ekle, name="makale_ekle"),
    path('article/<int:id>',views.makale_detay, name="makale_detay"),
    path('makale_guncelle/<int:id>',views.makale_guncelle, name="makale_guncelle"),
    path('makale_sil/<int:id>',views.makale_sil, name="makale_sil"),
    path('',views.articles, name="articles"),
]