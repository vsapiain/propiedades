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
            data_serializer = PlanContratoProxySerializer(data, many=True)
        except PlanContratoProxy.DoesNotExist:
            error = 1
            msg = "Planes inexistentes"
        except Exception as err:
            msg = err
            error = 1
            data = ""
        finally:
            plan_data["msg"] = msg
            plan_data["error"] = error
            plan_data["data"] = data_serializer.data
            return plan_data