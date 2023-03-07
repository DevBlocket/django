from rest_framework import viewsets

from fix_request.models import FixRequest
from fix_request.serializers import FixRequestSerializer


class FixRequestModelViewSet(viewsets.ModelViewSet):

    serializer_class = FixRequestSerializer

    def get_queryset(self):

        queryset = FixRequest.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset


