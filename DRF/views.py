from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, auth
from DRF.models import model_data
from DRF.serializers import serializer_data

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

def home(request):
    return render(request, 'create.html')

def create(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        #saving data into auth_user field of database, which will create user
        userAdm=User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )
        userAdm.save()
        print("User created successfully")

        #saving data into our custom model, which will use for CRUD operations
        userModel=model_data(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )
        userModel.save()
        print("Databased saved successfully")

        return HttpResponse("Your Data has been created successfully!")

    else:
        return HttpResponse("Error! Please fillout the form first")

#RestAPI
#1) GET

#i) Get request for all database
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication])
class listt(ListAPIView):
    queryset=model_data.objects.all()
    serializer_class=serializer_data

#ii) Get request for particular database
@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication])
def get(request,username):
    try:
        find=model_data.objects.get(username=username)
    except model_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        output=serializer_data(find)
        return Response(output.data)


#2) PUT
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update(request, username):
    try:
        find=model_data.objects.get(username=username)
    except model_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="PUT":
        output=serializer_data(find, data=request.data)
        data={}
        if output.is_valid():
            output.save()
            data['success']="Data updated successfully"
            return Response(data)
        return Response(output.errors, status=status.HTTP_400_BAD_REQUEST)


#3) POST
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def post(request):
    if request.method=="POST":
        output=serializer_data(data=request.data)
        if output.is_valid():
            output.save()
            return Response(output.data, status=status.HTTP_201_CREATED)
        return Response(output.errors, status=status.HTTP_400_BAD_REQUEST)


#4) DELETE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete(request,username):
    try:
        find=model_data.objects.get(username=username)
    except model_data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="DELETE":
        output=find.delete()
        data={}
        if output:
            data["success"]= "Data deleted successfully"
        else:
            data["failure"]= "Failed to delete data"
        return Response("data deleted")