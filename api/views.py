from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class HealthCheck(APIView):
    def get(self, request):
        return Response({
            "status": "ok",
            "message": "Backend is running"
        })


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AskSerializer

class AskAPIView(APIView):
    def post(self,request):
        serializer = AskSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        question = serializer.validated_data['question']

        answer = f"you asked: {question}"
        return Response({
            "question": question,
            "answer": answer
        })

