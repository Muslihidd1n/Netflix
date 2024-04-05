from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *

class HelloApi(APIView):
    def get(self, request):
        d = {
            "xabar": "Salom Dunyo!",
            "qoshimcha": "Bu DRF'dagi 1-chi darsimiz boldi"
        }
        return Response(d)


    def post(self,request):
        data = request.data
        d = {
            "xabar": "Post qabul qilindi",
            "post bolgan malumot": data
        }
        return Response(d)

class AktyorlarAPI(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializers(aktyorlar, many=True)
        return Response(serializer.data)

    def post(self,request):
        aktyor = request.data
        serializer = AktyorSerializers(data=aktyor)
        if serializer.is_valid():
            valid_data = serializer.validated_data
            Aktyor.objects.create(
                ism = valid_data.get("ism"),
                davlat = valid_data.get("davlat"),
                jins = valid_data.get("jins"),
                tugilgan_sana = valid_data.get("tugilgan_sana")
            )
            return Response(serializer.data)
        return Response(serializer.errors)

class AktyorAPI(APIView):
    def get(self, request,pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializers(aktyor)
        return Response(serializer.data)

    def put(self, request, pk):
        data = request.data
        aktyor = Aktyor.objects.filter(id=pk)
        serializer = AktyorSerializers(aktyor.first(), data=data)
        if serializer.is_valid():
            data = serializer.validated_data
            aktyor.update(
                ism=data.get("ism"),
                davlat=data.get("davlat"),
                jins=data.get("jins"),
                tugilgan_sana=data.get("tugilgan_sana")
            )
            return Response(serializer.data)
        return Response(serializer.errors)



class TariflarAPI(APIView):
    def get(self, request):
        tariflar = Tarif.objects.all()
        serializer = TarifSerializers(tariflar, many=True)
        return Response(serializer.data)


    def post(self, request):
        tarif = request.data
        serializer = TarifSerializers(data=tarif)
        if serializer.is_valid():
            valid_data = serializer.validated_data
            Tarif.objects.create(
                nom = valid_data.get("nom"),
                davomiylik = valid_data.get("davomiylik"),
                narx = valid_data.get("narx")
            )
            return Response(serializer.data)
        return Response(serializer.errors)



class TarifAPI(APIView):
    def get(self, request,pk):
        tarif = Tarif.objects.get(id=pk)
        serializer = TarifSerializers(tarif)
        return Response(serializer.data)


    def put(self, request, pk):
        data = request.data
        tarif = Tarif.objects.filter(id=pk)
        serializer = TarifSerializers(tarif.first(), data=data)
        if serializer.is_valid():
            data = serializer.validated_data
            tarif.update(
                nom = data.get("nom"),
                davomiylik = data.get("davomiylik"),
                narx = data.get("narx"),
            )
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        tarif = Tarif.objects.get(id=pk).delete()
        tarif.delete()
        return Response({"succes":True,"message": "Plan deleted"})
