from rest_framework import viewsets, permissions
from .models import Quiz, Question, Answer
from .serializers import AnswerSerializer, QuestionSerializer, QuizSerializer
from .utils import CustomJsonRenderer
from .throttles import QuizPostThrottle, QuizGetThrottle


class QuizViewSet(viewsets.ModelViewSet):
    quiz_post_throttle_scope = 'post_scope'
    quiz_get_throttle_scope = 'get_scope'

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    renderer_classes = (CustomJsonRenderer,)

    def get_throttles(self):
        if self.request.method.lower() == 'get':
            return (QuizGetThrottle(),)
        elif self.request.method.lower() == 'post':
            return (QuizPostThrottle(),)
        else:
            return super(QuizViewSet, self).get_throttles()
