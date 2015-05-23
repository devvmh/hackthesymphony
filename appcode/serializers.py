from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Question
    fields = ('id', 'question')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Answer
    fields = ('id', 'old_question', 'answer', 'new_question', 'redirect_url_if_no_new_question')

class SessionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Session
    fields = ('id', 'username', 'current_question', 'ip')

class SessionAnswerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = SessionAnswer
    fields = ('id', 'session', 'question', 'answer')
