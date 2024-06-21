from django.urls import path,include
from django.contrib import admin
from rest_framework import routers
from .views import movieviewset

router=routers.DefaultRouter()
router.register(r'movies',movieviewset)

urlpatterns = [
    path('',include(router.urls))
]
