from django.db.models import *

class Question(Model):
  #question_id is not the same as pk
  question = CharField(max_length=2550)
  def __unicode__(self): return self.question
  
class Answer(Model):
  old_question = ForeignKey(Question, related_name='old')
  answer = CharField(max_length=2550)
  new_question = ForeignKey(Question, related_name='new', blank=True)
  redirect_url_if_no_new_question = URLField(blank=True)
  def __unicode__(self): return self.answer + ' (' + self.old_question.question + ')'
