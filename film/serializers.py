from rest_framework import serializers


class AktyorSerializers(serializers.Serializer):
    ism = serializers.CharField()
    davlat = serializers.CharField()
    jins = serializers.CharField()
    tugilgan_sana = serializers.DateField()


class TarifSerializers(serializers.Serializer):
    nom = serializers.CharField()
    davomiylik = serializers.IntegerField()
    narx = serializers.IntegerField()
