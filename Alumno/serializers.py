# ----------------librerias------------
from rest_framework import routers, serializers, viewsets

# ----------------Modelos--------------
# Nombre app                      nombre modelo
from Alumno.models import Alumno

from drf_dynamic_fields import DynamicFieldsMixin
#                         serializers
class AlumnoSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id','profesorAsig','address','name','ap_pat','ap_mat','matricula','materia','telefono','edad','sexo','fechaNacimiento')

