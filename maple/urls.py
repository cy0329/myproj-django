from django.urls import path, include
from rest_framework.routers import DefaultRouter

from maple.views import MapleViewSet

app_name = "maple"

router = DefaultRouter()
router.register("character", MapleViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
