from rest_framework import viewsets, routers
from django_filters.rest_framework import DjangoFilterBackend
from .models import Costs, Plan
from .serializers import CostSerializers, PlanSerializers
from django_filters import rest_framework as rest_filters, NumberFilter, CharFilter, BooleanFilter
#from rest_framework import filters


class PlanFilter(rest_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='incontains')
    amount = NumberFilter(field_name='amount')
    Completed = BooleanFilter(field_name='Completed')

    class Meta:
        model = Plan
        fields = ['name', 'amount', 'Completed']


class CostViewSet(viewsets.ModelViewSet):
    queryset = Costs.objects.all()
    serializer_class = CostSerializers


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlanFilter


router = routers.DefaultRouter()
router.register(r'cost', CostViewSet)
router.register(r'plan', PlanViewSet)
