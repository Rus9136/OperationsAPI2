from rest_framework import serializers
from .models import Costs, Plan


class CostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Costs
        fields = "__all__"


class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
