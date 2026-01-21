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
from rag.rag_service import rag_service

class AskAPIView(APIView):
    def post(self, request):
        serializer = AskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question = serializer.validated_data["question"]
        user_id = request.user.id

        answer = rag_service.ask(user_id, question)

        return Response({
            "user_id": user_id,
            "question": question,
            "answer": answer
        })
