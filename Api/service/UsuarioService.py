#from PropiedadesApp.proxy import cuenta_acceso_proxy
from Api.proxy import  CuentaAccesoProxy
from Api.models import CuentaAcceso
from Api.models import Usuario
from Api.models import Particular
from Api.models import Direccion

from Api.models import  PlanContrato
from Api.models import Servicio
from Api.models import ServicioPedido

from Api.service.TokenService import TokenService

class UsuarioService:
    def is_authenticated_particular(self, email, clave):
        token = ""
        msg = ""
        usuario = ""
        error = '0'
        tipo_usuario_paticular = 1
        plan = ""
        plan_id = ""
        try:
            obj_cuenta = CuentaAccesoProxy.objects.filter(nid_usuario__nid_tipo_usuario=tipo_usuario_paticular)
            obj_servicio_pedido = ServicioPedido.objects.filter(nid_servicio__nid_tipo_servicio=1).filter(
                nid_pedido__nid_usuario=8).filter(nestadoregistro_pedido=1).filter(
                nid_servicio__nestadoregistro_servicio=1).filter(nid_pedido__nid_usuario__nestadoregistro_usuario=1)
            obj_plan = PlanContrato.objects.filter(
                nid_servicio__nid_servicio=obj_servicio_pedido.get().nid_servicio.nid_servicio).get()
            service_token = TokenService()
            obj_cuenta = CuentaAccesoProxy.objects_particular.filter(semail_cuenta_acceso=email).get()
            if obj_cuenta.sclave_cuenta_acceso == clave:
                usuario = obj_cuenta.semail_cuenta_acceso
                obj_usuario = obj_cuenta.nid_usuario
                plan_id = obj_plan.nid_plan_contrato
                plan = obj_plan.snombre_plan_contrato
                plan_link = "<a href=/planes/" + str(plan_id) + ">Plan " + plan + "</a>"
                payload = {'username': obj_cuenta.semail_cuenta_acceso, 'id': str(obj_cuenta.nid_cuenta_acceso),
                           'tipo': str(tipo_usuario_paticular), 'plan': plan, 'plan_id': str(plan_id),
                           'planLink': plan_link}
                token = service_token.encode_token(payload)
            else:
                usuario = ""
                error = '1'
                msg = "Clave de acceso incorrecta"
        except CuentaAccesoProxy.DoesNotExist:
            error = '1'
            msg = "Usuario no autorizado"
        except Exception as err:
            error = '1'
            msg = err
        finally:
            user_details = {}
            user_details['username'] = usuario
            user_details['token'] = token
            user_details['plan'] = plan
            user_details['plan_id'] = plan_id
            user_details['planLink'] = "<a href=/planes/" + str(plan_id) + ">Plan " + plan +"</a>"
            user_details['msg'] = msg
            user_details['error'] = error
            return user_details

    def is_authenticated_corredora(self, nombre_usuario, clave):
        try:
            token = ""
            msg = ""
            error = '0'
            usuario = ""
            tipo_usuario_corredora = 2
            service_token = TokenService()
            obj_cuenta = CuentaAccesoProxy.objects.filter(nid_usuario__nid_tipo_cliente=tipo_usuario_corredora). \
                filter(snombreusuario_cuenta_acceso=nombre_usuario).get()
            if obj_cuenta.sclave_cuenta_acceso == clave:
                payload = {'usuario': obj_cuenta.snombreusuario_cuenta_acceso, 'id': str(obj_cuenta.nid_cuenta_acceso),
                           'tipo': str(tipo_usuario_corredora)}
                usuario = obj_cuenta.snombreusuario_cuenta_acceso
                token = service_token.encode_token(payload)
            else:
                usuario = ""
                msg = "Clave de acceso incorrecta"
            user_details = {}
            user_details['username'] = usuario
            user_details['token'] = token
            user_details['msg'] = msg
            user_details['error'] = "0"
            return user_details
        except CuentaAccesoProxy.DoesNotExist:
            error = '1'
            msg = "Usuario no autorizado"
        except Exception as err:
            error = '1'
            msg = err
        finally:
            user_details['username'] = usuario
            user_details['token'] = token
            user_details['msg'] = msg
            user_details['error'] = error
            return user_details

    def is_authenticated_inmobiliaria(self, nombre_usuario, clave):
        try:
            token = ""
            msg = ""
            usuario = ""
            tipo_usuario_inmobiliaria = 3
            try:
                service_token = TokenService()
                obj_cuenta = CuentaAccesoProxy.objects.filter(nid_cliente__nid_tipo_cliente=tipo_usuario_inmobiliaria). \
                    filter(snombreusuario_cuenta_acceso=nombre_usuario).get()
                if obj_cuenta.sclave_cuenta_acceso == clave:
                    payload = {'usuario': obj_cuenta.snombreusuario_cuenta_acceso, 'id': str(obj_cuenta.nid_cuenta_acceso),
                               'tipo': str(tipo_usuario_inmobiliaria)}
                    usuario = obj_cuenta.snombreusuario_cuenta_acceso
                    token = service_token.encode_token(payload)
                else:
                    usuario = ""
                    msg = "Clave de acceso incorrecta"
            except CuentaAccesoProxy.DoesNotExist:
                msg = "Usuario no autorizado"
            user_details = {}
            user_details['username'] = usuario
            user_details['token'] = token
            user_details['msg'] = msg
            user_details['error'] = ""
            return user_details
        except ValueError:
            return None

    def update_user(self,id,data):
        user_data = {}
        tipo_particular = 1
        try:
            obj_cuenta = CuentaAcceso.objects.filter(nid_cuenta_acceso=int(id))
            obj_usuario = obj_cuenta.get()
            obj_usuario = obj_usuario.nid_usuario
            if obj_usuario.nid_tipo_usuario.nid_tipo_usuario == tipo_particular:
                obj_usuario.semailcontacto_usuario = data["email_contacto"]
                obj_usuario.save()
                obj_particular = Particular.objects.filter(nid_usuario__nid_usuario = obj_usuario.nid_usuario).get()
                obj_particular.snmobre_partiular = data["nombre"]
                obj_particular.sapellidop_particular = data["apellidoP"]
                obj_particular.sapellidom_particular = data["apellidoM"]
                obj_particular.save()
                obj_direccion = obj_usuario.nid_direccion
                obj_direccion.sdireccion_direccion = data["direccion"]
                obj_direccion.save()
            error = "0"
            msg = ""
        except CuentaAcceso.DoesNotExist:
            error = '1'
            msg = "Usuario inexistentes"
            user_data["data"] = ""
        except Exception as err:
            msg = err
            error = '1'
        finally:
            user_data["msg"] = msg
            user_data["error"] = error
            return user_data

    def update_account(self, id, data):
        user_data = {}
        msg = ''
        error = '0'
        tipo_particular = 1
        tipo_corredora = 2
        tipo_inmobiliaria = 2
        try:
            clave = data["clave"]
            obj_cuenta = CuentaAcceso.objects.filter(nid_cuenta_acceso=int(id)).get()
            obj_cuenta.sclave_cuenta_acceso = clave
            obj_cuenta.save()
            user_data["error"] = "0"
            user_data["msg"] = "Dato(s) actualizado(s) correctamente "
        except CuentaAcceso.DoesNotExist:
            error = "1"
            user_data["msg"] = "Cuenta de acceso invalida"
            return user_data
        finally:
            user_data["msg"] = msg
            user_data["error"] = error
            return user_data

    def get_user_detail(self, id):
        tipo_particular = 1
        error = "0"
        msg = ""
        try:
            user_data = {}
            obj_cuenta = CuentaAcceso.objects.filter(nid_cuenta_acceso=int(id))
            obj_cuenta = obj_cuenta.get()
            obj_usuario = obj_cuenta.nid_usuario
            obj_direccion = obj_usuario.nid_direccion
            user_data["rut"] = obj_usuario.srut_usuario
            user_data["EmailCuenta"] = obj_cuenta.semail_cuenta_acceso
            user_data["EmailContacto"] = "" if obj_usuario.semailcontacto_usuario is None else obj_usuario.semailcontacto_usuario
            user_data["password"] = obj_cuenta.sclave_cuenta_acceso
            if obj_direccion is not None:
                user_data["direccion"] = obj_direccion.sdireccion_direccion
                if obj_direccion.nid_comuna is not None:
                    user_data["comunaId"] = obj_direccion.nid_comuna.nid_comuna
            if obj_usuario.nid_tipo_usuario.nid_tipo_usuario == tipo_particular:
                particular_data = Particular.objects.filter(nid_usuario__nid_usuario=obj_usuario.nid_usuario).get()
                user_data["nombre"] = particular_data.snombre_particular
                user_data["apellidoP"] = particular_data.sapellidop_particular
                user_data["apellidoM"] = particular_data.sapellidom_particular
        except CuentaAcceso.DoesNotExist:
            error = "1"
            msg = "Usuario no encontrado"
        except Exception as err:
            error = '1'
            msg = err
        finally:
            user_data["msg"] = msg
            user_data["error"] = error
            return user_data

