from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny ,SAFE_METHODS,BasePermission, IsAuthenticatedOrReadOnly,IsAuthenticated,IsAdminUser,DjangoModelPermissions
from .serializers import*
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponseGone,JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from posts.permissions import *
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
# Create your views here.

class WritePermission(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.id==request.user

class ChefMenageList(generics.ListCreateAPIView):
    permission_classes=[IsAgentAuthenticated]
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.filter(owner1=user.id)
    def perform_create(self, serializer):
        serializer.save(owner1=self.request.user)


class ChefMenageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAgentAuthenticated]
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.filter(owner1=user.id)
    def perform_create(self, serializer):
        serializer.save(owner1=self.request.user)

#Les Conjoint
class ConjointList(generics.ListCreateAPIView):
    permission_classes=[IsAgentAuthenticated]
    model=Conjoint
    serializer_class=PostConjointSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Conjoint.objects.filter(owner2=user.id)
    def perform_create(self, serializer):
        serializer.save(owner2=self.request.user)
  
class ConjointDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[IsAgentAuthenticated]
    model=Conjoint
    serializer_class=PostConjointSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Conjoint.objects.filter(owner2=user.id)
    def perform_create(self, serializer):
        serializer.save(owner2=self.request.user)

#Les Recensés
class RecenserList(generics.ListCreateAPIView):
    permission_classes=[IsAgentAuthenticated]
    model=Recenser
    serializer_class=RecensementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Recenser.objects.filter(owner3=user.id)
    def perform_create(self, serializer):
        serializer.save(owner3=self.request.user)
  
class RecenserDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[IsAgentAuthenticated]
    model=Recenser
    serializer_class=RecensementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Recenser.objects.filter(owner3=user.id)
    def perform_create(self, serializer):
        serializer.save(owner3=self.request.user)

#Les Enfants
class EnfantList(generics.ListCreateAPIView):
    permission_classes=[IsAgentAuthenticated]
    model=Enfant
    serializer_class=EnfantS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Enfant.objects.filter(owner4=user.id)
    def perform_create(self, serializer):
        serializer.save(owner4=self.request.user)
  
class EnfantDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[IsAgentAuthenticated]
    model=Enfant
    serializer_class=EnfantS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Enfant.objects.filter(owner4=user.id)
    def perform_create(self, serializer):
        serializer.save(owner4=self.request.user)

#Les commodites
class CommoditeList(generics.ListCreateAPIView):
    permission_classes=[IsAgentAuthenticated]
    model=Commodite
    serializer_class=CommoditeS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Commodite.objects.filter(owner5=user.id)
    def perform_create(self, serializer):
        serializer.save(owner5=self.request.user)
  
class CommoditeDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[IsAgentAuthenticated]
    model=Commodite
    serializer_class=CommoditeS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Commodite.objects.filter(owner5=user.id)
    def perform_create(self, serializer):
        serializer.save(owner5=self.request.user)

#Les equipements
class EquipementList(generics.ListCreateAPIView):
    permission_classes=[IsAgentAuthenticated]
    model=Equipement
    serializer_class=EquipementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Equipement.objects.filter(owner6=user.id)
    def perform_create(self, serializer):
        serializer.save(owner6=self.request.user)
  
class EquipementDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[IsAgentAuthenticated]
    model=Equipement
    serializer_class=EquipementS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Equipement.objects.filter(owner6=user.id)
    def perform_create(self, serializer):
        serializer.save(owner6=self.request.user)

#Les deces
class DecesList(generics.ListCreateAPIView):
    permission_classes=[IsAgentAuthenticated]
    model=Deces
    serializer_class=DeceS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Deces.objects.filter(owner7=user.id)
    def perform_create(self, serializer):
        serializer.save(owner7=self.request.user)
  
class DecesDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[IsAgentAuthenticated]
    model=Deces
    serializer_class=DeceS
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Deces.objects.filter(owner7=user.id)
    def perform_create(self, serializer):
        serializer.save(owner7=self.request.user)

#les charges
class ChargeList(generics.ListCreateAPIView):
    permission_classes=[IsAgentAuthenticated]
    model=Charge
    serializer_class=PostChargeSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Charge.objects.filter(owner8=user.id)
    def perform_create(self, serializer):
        serializer.save(owner8=self.request.user)
  
class ChargeDetail(generics.RetrieveUpdateDestroyAPIView,WritePermission):
    permission_classes=[IsAgentAuthenticated]
    model=Charge
    serializer_class=PostChargeSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Charge.objects.filter(owner8=user.id)
    def perform_create(self, serializer):
        serializer.save(owner8=self.request.user)


class ListRecenser(generics.ListAPIView):
    permission_classes=[IsAgentAuthenticated]
    model=Chef_menage
    serializer_class=PostChefMSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields=['district','region','departement','sous_prefecture','commune','milieu_r','quartier']
    def get_queryset(self):
        user = self.request.user
        return Chef_menage.objects.filter(owner=user.id)

class RecensementView(APIView):
    permission_classes=[IsAgentAuthenticated]
    analyse={}
    def post(self,request):
        data = JSONParser().parse(request)
        if data['Chef_menage']:
            for chef_menage in data['chef_menage']:
                serializerch = PostChefMSerializer(data=chef_menage)
                if serializerch.is_valid():
                    serializerch.save()
                    analyse['capital_humain']=[chef_menage['sexes'],chef_menage['annee_naissance']]
        if data['Conjoint']:
            for conjoint in data['Conjoint']:
                serializerco = PostConjointSerializer(data=conjoint)
                if serializerco.is_valid():
                    serializerco.save()
        if data['Recenser']:
            for recenser in data['Recenser']:
                serializerr = RecensementS(data=recenser)
                if serializerr.is_valid():
                    serializerr.save()
        if data['Enfant']:
            for enfant in data['Enfant']:
                serializere=EnfantS(data=enfant)
                if serializere.is_valid():
                    serializere.save()

        if data['Charge']:
            for charge in data['Charge']:
                serializere=PostChargeSerializer(data=charge)
                if serializerg.is_valid():
                    serializerg.save()

        if data['Commodite']:
            for commodite in data['Commodite']:
                serializerc=CommoditeS(data=commodite)
                if serializerc.is_valid():
                    serializerc.save()
        if data['Equipement']:
            for equipement in data['Equipement']:
                serializereq=EquipementS(data=equipement)
                if serializereq.is_valid():
                    serializereq.save()
        if data['Deces']:
            for deces in data['Deces']:
                serializerd=DeceS(data=deces)
                if serializerd.is_valid():
                    serializerd.save()
            return JsonResponse(serializerp.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    # def get(self,request,pk):
    #     try:
    #         affectations = Affecter.objects.get(pk=pk)
    #     except affectations.DoesNotExist:
    #         return HttpResponse(status=404)
    #     serializer = PostAffectationSerializer(affectations)
    #     return JsonResponse(serializer.data)

 