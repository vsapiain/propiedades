from Api.proxy import PlanContratoProxy
#from django.core import serializers
from Api.serializers import PlanContratoProxySerializer

class PlanService:
    def get_all_particular(self):
        plan_data = {}
        msg = ""
        error = 0
        try:
            data = PlanContratoProxy.objects_particular.order_by('nid_plan_contrato')
        except PlanContratoProxy.DoesNotExist:
            plan_data["error"] = 1
            plan_data["msg"] = "Planes inexistentes"
            plan_data["data"] = ""
            return plan_data
        try:
            data_serializer = PlanContratoProxySerializer(data, many=True)
        except Exception as err:
            msg = "Error carga Planes"
            error = 1
            data = ""
        finally:
            plan_data["msg"] = msg
            plan_data["error"] = error
            plan_data["data"] = data_serializer.data
            return plan_data