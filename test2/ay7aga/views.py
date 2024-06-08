from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import test_data as Test , User_acc

# Create your views here.
from .serializers import TestSerializer ,UserSerializer


class testApiView(generics.ListCreateAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        return Test.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        ser = self.get_serializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class UserApiView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User_acc.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        ser = self.get_serializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
