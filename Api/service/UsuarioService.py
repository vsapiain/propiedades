#from PropiedadesApp.proxy import cuenta_acceso_proxy
from Api.proxy import  CuentaAccesoProxy
from Api.models import CuentaAcceso
from Api.models import Usuario
from Api.models import Particular
from Api.models import Direccion
from Api.models import UsuarioPlanContrato
from Api.service.TokenService import TokenService

class UsuarioService:
    def is_authenticated_particular(self, email, clave):
        try:
            token = ""
            msg = ""
            usuario = ""
            tipo_usuario_paticular = 1
            plan = ""
            plan_id = ""
            try:
                '''
                obj_cuenta = CuentaAccesoProxy.objects.filter(nid_usuario__nid_tipo_usuario=tipo_usuario_paticular).\
                    filter(semail_cuenta_acceso=email).get()
                '''
                service_token = TokenService()
                obj_cuenta = CuentaAccesoProxy.objects_particular.filter(semail_cuenta_acceso=email).get()
                if obj_cuenta.sclave_cuenta_acceso == clave:
                    usuario = obj_cuenta.semail_cuenta_acceso
                    obj_usuario = obj_cuenta.nid_usuario
                    obj_plan_usuario = UsuarioPlanContrato.objects.filter(nid_usuario = obj_usuario.nid_usuario ).get()
                    obj_plan = obj_plan_usuario.nid_plan_contrato
                    plan_id = obj_plan.nid_plan_contrato
                    plan = obj_plan.snombre_plan_contrato
                    plan_link = "<a href=/planes/" + str(plan_id) + ">Plan " + plan + "</a>"
                    payload = {'username': obj_cuenta.semail_cuenta_acceso, 'id': str(obj_cuenta.nid_cuenta_acceso),
                               'tipo': str(tipo_usuario_paticular), 'plan': plan, 'plan_id': str(plan_id),
                               'planLink': plan_link}
                    token = service_token.encode_token(payload)
                else:
                    usuario = ""
                    msg = "Clave de acceso incorrecta"
            except CuentaAccesoProxy.DoesNotExist:
                msg = "Usuario no autorizado"
            finally:
                user_details = {}
                user_details['username'] = usuario
                user_details['token'] = token
                user_details['plan'] = plan
                user_details['plan_id'] = plan_id
                user_details['planLink'] = "<a href=/planes/" + str(plan_id) + ">Plan " + plan +"</a>"
                user_details['msg'] = msg
                user_details['error'] = ""
                return user_details
        except ValueError:
            return None

    def is_authenticated_corredora(self, nombre_usuario, clave):
        try:
            token = ""
            msg = ""
            usuario = ""
            tipo_usuario_corredora = 2
            try:
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
            except CuentaAccesoProxy.DoesNotExist:
                msg = "Usuario no autorizado"
            user_details = {}
            user_details['username'] = usuario
            user_details['token'] = token
            user_details['msg'] = msg
            user_details['error'] = "0"
            return user_details
        except ValueError:
            user_details = {}
            user_details['username'] = ""
            user_details['token'] = ""
            user_details['msg'] = "Error inesperable"
            user_details['error'] = "1"

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
        try:
            user_data = {}
            tipo_particular = 1
            tipo_corredora = 2
            tipo_inmobiliaria = 2
            '''
            cuenta_rut =  Usuario.objects.filter(srut_usuario=data["rut"])
            if cuenta_rut.count()>0:
                user_data["error"] = "1"
                user_data["msg"] = "Rut existente"
                return user_data
            '''
            obj_cuenta = CuentaAcceso.objects.filter(nid_cuenta_acceso=int(id)).get()
            obj_usuario = obj_cuenta.nid_usuario
            if obj_usuario.nid_tipo_usuario.nid_tipo_usuario == tipo_particular:
                obj_usuario.semailcontacto_usuario = data["email_contacto"]
                obj_usuario.save()
                obj_particular = Particular.objects.filter(nid_usuario__nid_usuario = obj_usuario.nid_usuario).get()
                obj_particular.snmobre_partiular = data["nombre"]
                obj_particular.sapellidop_particular = data["apellidoP"]
                obj_particular.sapellidom_particular = data["apellidoM"]
                obj_particular.save()
                obj_direccion =  obj_usuario.nid_direccion
                obj_direccion.sdireccion_direccion = data["direccion"]
                obj_direccion.save()
            #guardar data
            user_data["error"] = "0"
            user_data["msg"] = ""
        except CuentaAcceso.DoesNotExist:
            user_data["error"] = "1"
            user_data["msg"] = "Usuario no encontrado"
        finally:
            return user_data

    def update_account(self, id, data):
        try:
            user_data = {}
            tipo_particular = 1
            tipo_corredora = 2
            tipo_inmobiliaria = 2
            clave = data["clave"]
            obj_cuenta = CuentaAcceso.objects.filter(nid_cuenta_acceso=int(id)).get()
            obj_cuenta.sclave_cuenta_acceso = clave
            obj_cuenta.save()
            user_data["error"] = "0"
            user_data["msg"] = "Dato(s) actualizado(s) correctamente "
        except CuentaAcceso.DoesNotExist:
            user_data["error"] = "1"
            user_data["msg"] = "Usuario no encontrado"
        finally:
            return user_data

    def get_user_detail(self, id):
        tipo_particular = 1
        try:
            user_data = {}
            obj_cuenta = CuentaAcceso.objects.filter(nid_cuenta_acceso=int(id)).get()
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
                user_data["error"] = "0"
        except CuentaAcceso.DoesNotExist:
            user_data["error"] = "1"
            user_data["msg"] = "Usuario no encontrado"
        finally:
            return user_data


    '''
    def encode_token(self,data_encode):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=60*30),
                'iat': datetime.datetime.utcnow(),
                'user': data_encode
            }
            return jwt.encode(
                payload,
                "secret_citypro"
            )
        except ValueError:
            return None

    def decode_token(self, token):
        token_details = {}
        try:
            token_data = jwt.decode(token, "secret_citypro")
            token_details['username'] = token_data['user']['username']
            token_details['id'] = token_data['user']['id']
            token_details['plan'] = token_data['user']['plan']
            token_details['plan_id'] = token_data['user']['plan_id']
            token_details['planLink'] = token_data['user']['planLink']
            token_details['msg'] = ""
            token_details['error'] = "0"
            token_details['token'] = token
            return token_details
        except (jwt.ExpiredSignatureError):
            token_details['username'] = ""
            token_details['id'] = ""
            token_details['msg'] = "La sesión a caducado"
            token_details['error'] = "1"
            token_details['token'] = ""
            return token_details
        except (jwt.DecodeError):
            token_details['username'] = ""
            token_details['id'] = ""
            token_details['msg'] = "Token invalido"
            token_details['error'] = "1"
            token_details['token'] = ""
            return token_details
    '''