from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "maple"

router = DefaultRouter()
router.register("maple", MapleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

