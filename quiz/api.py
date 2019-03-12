from quiz.models import Quiz, Question, Answer
from rest_framework import viewsets, permissions
from .serializers import AnswerSerializer, QuestionSerializer, QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
