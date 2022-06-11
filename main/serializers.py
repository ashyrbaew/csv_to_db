from django.db.models import Sum
from rest_framework import serializers
from .models import Blackbox


class BlackboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blackbox
        fields = '__all__'
        # fields = ('total_info_count', 'aircraft')

