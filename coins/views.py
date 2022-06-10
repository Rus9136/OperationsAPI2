from rest_framework import viewsets, routers
from django_filters.rest_framework import DjangoFilterBackend
from .models import Costs, Plan
from .serializers import CostSerializers, PlanSerializers


class CostViewSet(viewsets.ModelViewSet):
    queryset = Costs.objects.all()
    serializer_class = CostSerializers


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['name, Completed']


router = routers.DefaultRouter()
router.register(r'cost', CostViewSet)
router.register(r'plan', PlanViewSet)
