###
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import random, hashlib

from .serializers import User_Serializer, UserPatchSerializer
from .models import Userset

def hash_proc(s):
    salt = "_typed with fingers"
    s += salt
    strlen = len(s)
    strand = ''.join((random.choice(s) for i in range(strlen)))
    hd = hashlib.sha256(strand.encode('utf-8')).hexdigest()
    return hd

# Create your views here.

class UsersetViews(APIView):

    def get(self, request, id=None):
        if id:
            print('request: id=', id)
            item = Userset.objects.get(id=id)
            serializer = User_Serializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        # debug
        usersets = Userset.objects.all()
        serializer = User_Serializer(usersets, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_id = serializer.data["id"]
            obj = Userset.objects.get(id=new_id)
            psw = obj.password
            print("passed psw ", psw)
            obj.password = hash_proc(psw)
            obj.save(update_fields=["password"])
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Userset.objects.get(id=id)
        serializer = UserPatchSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Userset, id=id)
        item.delete()
        return Response({"status": "success", "data": "record was deleted"})

        
