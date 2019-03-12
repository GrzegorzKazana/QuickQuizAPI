from django.db import models

import string
import random

ID_HASH_LENGTH = 6


class HashedIdModel(models.Model):
    hash_id = models.CharField(
        max_length=ID_HASH_LENGTH, primary_key=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        seed_string = string.digits + string.ascii_lowercase + string.ascii_uppercase
        while not self.hash_id:
            new_hash = ''.join(random.sample(seed_string, ID_HASH_LENGTH))
            if type(self).objects.filter(pk=new_hash).count() == 0:
                self.hash_id = new_hash

        super(HashedIdModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Quiz(HashedIdModel):
    quiz_title = models.CharField(max_length=255)


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    correct_answer = models.ForeignKey(
        'Answer', on_delete=models.PROTECT, null=True)


class Answer(models.Model):
    to_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=127)
