from rest_framework import serializers
from .models import Costs

class CostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Costs
        fields = "__all__"


