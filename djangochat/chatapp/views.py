from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')

def room(request, room_name):
    return render(request,'index.html',{"room_name": room_name})

class JwtView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data={"message": "You are authenticated"}, status=200)
