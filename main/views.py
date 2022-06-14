from django.db.models import Sum
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Blackbox
from .serializers import BlackboxSerializer


class AircraftViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [AllowAny]
    serializer_class = BlackboxSerializer
    queryset = Blackbox.objects.values(
        'aircraft', 'pre_legend', 'warning', 'paired_b', 'legend', 'lower_b',
        'repeat_legend', 'upper_a', 'lower_a','paired_a'
    ).order_by('aircraft').annotate(
        info_count=Sum('info_count'), errors_count=Sum('errors_count')
    )


class StatusViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [AllowAny]
    serializer_class = BlackboxSerializer
    queryset = Blackbox.objects.values(
        'status', 'pre_legend', 'warning', 'paired_b', 'legend', 'lower_b',
        'repeat_legend', 'upper_a', 'lower_a','paired_a'
    ).order_by('status').annotate(
        info_count=Sum('info_count'), errors_count=Sum('errors_count')
    )


class TypeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [AllowAny]
    serializer_class = BlackboxSerializer
    queryset = Blackbox.objects.values(
        'type','pre_legend', 'warning', 'paired_b', 'legend', 'lower_b',
        'repeat_legend', 'upper_a', 'lower_a','paired_a'
    ).order_by('type').annotate(
        info_count=Sum('info_count'), errors_count=Sum('errors_count')
    )
