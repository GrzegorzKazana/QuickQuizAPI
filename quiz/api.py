from quiz.models import Quiz, Question, Answer
from rest_framework import viewsets, permissions
from .serializers import AnswerSerializer, QuestionSerializer, QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuizSerializer
