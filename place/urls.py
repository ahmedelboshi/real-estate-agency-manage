from django.urls import include , path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('country',views.Country)
router.register('governorate',views.Governorate)
router.register('city',views.City)

urlpatterns = [
    path('',include(router.urls))
]