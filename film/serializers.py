from rest_framework import serializers
from .models import *
from rest_framework.exceptions import *


class AktyorSerializers(serializers.Serializer):
    ism = serializers.CharField()
    davlat = serializers.CharField()
    jins = serializers.CharField()
    tugilgan_sana = serializers.DateField()


    def validate_ism(self, qiymat):
        if len(qiymat) < 4:
            raise ValidationError("Ism bunchalik kichik bolmaydi")
        return qiymat


class TarifSerializers(serializers.Serializer):
    nom = serializers.CharField()
    davomiylik = serializers.IntegerField()
    narx = serializers.IntegerField()




class KinoSerializer(serializers.ModelSerializer):
    aktyorlar = AktyorSerializers(many=True)
    class Meta:
        model= Kino
        fields = '__all__'

    def to_representation(self, instance):
        kino = super(KinoSerializer, self).to_representation(instance)
        kino.update({"aktyorlar_soni": len(kino.get("aktyorlar"))})
        return kino



class KinoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Kino
        fields = '__all__'


class KinoAktyorSerializer(serializers.ModelSerializer):
    class Meta:
        model = KinoAktyor
        fields = '__all__'





