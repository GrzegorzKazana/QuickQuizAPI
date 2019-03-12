from rest_framework import serializers
from quiz.models import Quiz, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer_id', 'answer_text',)


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source='answer_set', many=True)
    correct_answer_index = serializers.IntegerField(write_only=True)

    class Meta:
        model = Question
        fields = ('question_id', 'question_text', 'correct_answer',
                  'answers', 'correct_answer_index')


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True)

    class Meta:
        model = Quiz
        fields = ('hash_id', 'quiz_title', 'questions',)

    def create(self, validated_data):
        questions_data = validated_data.pop('question_set')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            question = Question.objects.create(
                quiz=quiz, question_text=question_data['question_text'])
            answers = [Answer.objects.create(
                to_question=question, answer_text=answer_data['answer_text']) for answer_data in question_data['answer_set']]
            if len(answers) > question_data['correct_answer_index']:
                question.correct_answer = answers[question_data['correct_answer_index']]
                question.save()

        return quiz
