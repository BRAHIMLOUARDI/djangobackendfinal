import os
from django.db.models import Q
from django.db import transaction
from rest_framework.decorators import action
from requests import Response
from backend.models import Words
from backend.serializers import wordsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render


from keras.models import load_model
from backend.dataprocessing import logits_to_sentence
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'



model=load_model('./finalfinal.h5')











class wordsViewSet(viewsets.ModelViewSet):
    queryset = Words.objects.all()
    serializer_class = wordsSerializer
    def get_object(self, pk):
        try:
            return Words.objects.get(pk=pk)
        except Words.DoesNotExist:
            raise Http404
    
    def retrieve(self,request,*args,**kwargs):
       
   

        words=Words.objects.filter(Q(English=kwargs['pk'])|Q(Arabic=kwargs['pk'])|Q(French=kwargs['pk'])|Q(id=kwargs['pk']))
        print(args)
        if words.exists():
           serializer=wordsSerializer(words,many=True)
           return Response({ "success": True, "data": serializer.data[0] })

        return Response({ "success": False, "msg": 'word not found' })

   

    def update(self, request, pk, format=None):
        word=self.get_object(pk)
        serializer = wordsSerializer(word, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({ "success": True, "msg": 'word updeted successfully' })
        
        return Response({ "success": False, "msg": 'failed to update the word' })
        
      

    def destroy(self, request, pk, format=None):
        try:
          word=Words.objects.get(pk=pk)
          word.delete()
          return Response({ "success": True, "msg": 'word deleted successfully' })
        except Words.DoesNotExist:
          return Response({ "success":False, "msg": 'failed to delete the word' })



    def create(self,request,*args,**kwargs):    
        serializer = wordsSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({ "success": True, "msg": 'word created successfully' })
        
        return Response({ "success": False, "msg": 'failed to create the word' })
    @action(detail=True)
    def translate(self, request, *args, **kwargs):
        print(kwargs['pk'])
        prex=logits_to_sentence(model ,kwargs['pk']).split("   ")[0]
        return Response({"ans":prex })