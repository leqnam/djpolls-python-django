# https://www.django-rest-framework.org/tutorial/quickstart/#project-setup
from .models import Question
from rest_framework import serializers

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('url', 'id', 'question', 'pub_date', 'author_id')

