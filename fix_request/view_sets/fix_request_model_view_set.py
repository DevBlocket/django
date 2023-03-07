from rest_framework import viewsets

from fix_request.models import FixRequest
from fix_request.serializers import FixRequestSerializer


class FixRequestModelViewSet(viewsets.ModelViewSet):

    queryset = FixRequest.objects.all()
    serializer_class = FixRequestSerializer

