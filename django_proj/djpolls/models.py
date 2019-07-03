from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Question (models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Answer (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)    

    def __str__(self):
        return self.choice_text

