from Api.proxy import PlanContratoProxy
from Api.serializers import PlanContratoProxySerializer
from rest_framework import status

class PlanService:
    def get_all_particular(self):
        plan_data = {}
        msg = ""
        error = 0
        data = ''
        status_err = ''
        try:
            data = PlanContratoProxy.objects_particular.order_by('nid_plan_contrato')
            data_serializer = PlanContratoProxySerializer(data, many=True)
            data = data_serializer.data
            status_err = status.HTTP_200_OK
        except PlanContratoProxy.DoesNotExist:
            error = 1
            msg = "Planes inexistentes"
            status_err = status.HTTP_404_NOT_FOUND
        except Exception as err:
            msg = err
            error = 1
            data = ""
            status_err = status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            plan_data["msg"] = msg
            plan_data["error"] = error
            plan_data["data"] = data_serializer.data
            plan_data["status"] = status_err
            return plan_data