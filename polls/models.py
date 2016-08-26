from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class UserStatus(models.Model):
    status = models.CharField(max_length=200)
    status_date = models.DateTimeField(default=timezone.now)
    user_id = models.CharField(max_length=200)
