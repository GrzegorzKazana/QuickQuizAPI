from rest_framework import viewsets, permissions
from .models import Quiz, Question, Answer
from .serializers import AnswerSerializer, QuestionSerializer, QuizSerializer
from .utils import CustomJsonRenderer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    renderer_classes = (CustomJsonRenderer,)
