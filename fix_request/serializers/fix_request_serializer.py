from rest_framework import serializers

from fix_request.models import FixRequest


class FixRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixRequest
        fields = '__all__'
        