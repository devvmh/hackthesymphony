from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Question
    fields = ('question')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Answer
    fields = ('old_question', 'answer', 'new_question', 'redirect_url_if_no_new_question')

class SessionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Session
    fields = ('username', 'current_question')

class SessionAnswers(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = SessionAnswers
    fields = ('session', 'question', 'answer')
