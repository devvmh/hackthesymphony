from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Question
    fields = ('id', 'question', 'answers')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Answer
    fields = ('id', 'old_question', 'answer', 'new_question', 'comment', 'protip')

class SessionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Session
    fields = ('id', 'username', 'ip', 'session_token', 'session_answers')
    depth = 1 #show all session_answers

class SessionAnswerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = SessionAnswer
    fields = ('id', 'session', 'question', 'answer')
