from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = ('id', 'question', 'answers')

class AnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Answer
    fields = ('id', 'old_question', 'answer', 'new_question', 'comment', 'protip')

class SessionSerializer(serializers.ModelSerializer):
  current_question = serializers.PrimaryKeyRelatedField(read_only=True)

  class Meta:
    model = Session
    fields = ('id', 'username', 'ip', 'session_token', 'session_answers', 'current_question')
    depth = 1 #show all session_answers

class SessionAnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = SessionAnswer
    fields = ('id', 'session', 'question', 'answer')
