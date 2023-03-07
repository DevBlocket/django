from django.urls import path, include
from rest_framework import routers

from fix_request.view_sets import FixRequestModelViewSet

router = routers.SimpleRouter()
router.register('', FixRequestModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]