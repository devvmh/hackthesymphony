from django.db.models import *

class Question(Model):
  #question_id is not the same as pk
  question = CharField(max_length=2550)
  #answers - foreign key from Answer class on old_question field
  def __unicode__(self): return self.question
  
class Answer(Model):
  old_question = ForeignKey(Question, related_name='answers')
  answer = CharField(max_length=2550)
  new_question = ForeignKey(Question, related_name='answer_leading_here', blank=True)
  redirect_url_if_no_new_question = URLField(blank=True)
  def __unicode__(self): return self.answer + ' (' + self.old_question.question + ')'

class Session(Model):
  username = CharField(max_length=255, blank=True)
  current_question = ForeignKey(Question, blank=True, default=1)
  #answers - foreign key from SessionAnswer
  def __unicode__(self):
    if self.username:
      return self.username
    else:
      return "Anonymous - on Question #" + str(self.current_question.pk)

class SessionAnswer(Model):
  session = ForeignKey(Session, related_name='answers')
  question = ForeignKey(Question, related_name='sessions_answered_this_question')
  answer = ForeignKey(Answer, related_name='sessions_using_this_answer')
  def __unicode__(self):
    return self.session + " answered '" + str(self.answer) + "' to '" + str(self.question) + "'."
