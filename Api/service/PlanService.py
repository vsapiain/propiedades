from Api.proxy import PlanContratoProxy
#from django.core import serializers
from Api.serializers import PlanContratoProxySerializer

class PlanService:
    def get_all_particular(self):
        data = PlanContratoProxy.objects_particular.order_by('nid_plan_contrato').all()
        plan_data = {}
        plan_data["error"] = "0"
        plan_data["msg"] = ""
        plan_data["obj"] = ""
        if len(list(data)) < 1:
            plan_data["error"] = "1"
            plan_data["msg"] = "No existen planes"
        else:
            obj_serialize = PlanContratoProxySerializer(data,many=True)
            plan_data["obj"] = obj_serialize.data
        return plan_data
