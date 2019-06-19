from rest_framework import serializers
from  Api.models import PlanContrato

class PlanContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanContrato
        fields = ('nid_plan_contrato','snombre_plan_contrato')
