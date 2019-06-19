from rest_framework import serializers
from  Api.proxy import PlanContratoProxy

class PlanContratoProxySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanContratoProxy
        fields = ('nid_plan_contrato','snombre_plan_contrato','plan_actual','nid_tipo_plan_contrato')
        #fields = '__all__'
