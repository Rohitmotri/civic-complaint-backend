from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseBadRequest,JsonResponse
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# Create your views here.

@api_view(['POST'])
def AddUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Message":"User Registered Successfully"})
        else:
            print(serializer.errors)
            json_data = JsonResponse(serializer.errors)
            return Response(json_data)    
    
    return HttpResponseBadRequest




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




   