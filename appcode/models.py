from django.db.models import *

class Question(Model):
  #question_id is not the same as pk
  question = CharField(max_length=2550)
  #answers - foreign key from Answer class on old_question field
  def __unicode__(self): return self.question
  
class Answer(Model):
  old_question = ForeignKey(Question, related_name='answers')
  answer = CharField(max_length=2550)
  comment = CharField(max_length=2550, blank=True)
  protip = CharField(max_length=2550, blank=True)
  new_question = ForeignKey(Question, related_name='answer_leading_here', blank=True)
  def __unicode__(self): return self.answer + ' (' + self.old_question.question + ')'

class Session(Model):
  username = CharField(max_length=255, blank=True)
  current_question = ForeignKey(Question, blank=True, default=1)
  ip = CharField(max_length=15)
  session_token = CharField(max_length=255)
  #answers - foreign key from SessionAnswer
  def __unicode__(self):
    return self.session_token

class SessionAnswer(Model):
  session = ForeignKey(Session, related_name='session_answers')
  question = ForeignKey(Question, related_name='session_answers')
  answer = ForeignKey(Answer, related_name='sessions_using_this_answer')
  def __unicode__(self):
    return str(self.session) + " answered '" + str(self.answer) + "' to '" + str(self.question) + "'."

class ConcertManager(Manager):
  def in_the_future(self):
    return [c for c in self.all() if not self.date_passed(c)]

  def date_passed(self, concert):
    from dateutil import parser
    from datetime import date
    today_date = date.today()
  
    #parse dat
    datestr = concert.date.split("\n")[-1]
    concert_date = None
    try:
      concert_date = parser.parse(datestr).date()
    except ValueError:
      return false #just include this concert just in case

    #KWS season
    if concert_date.month < 7:
      concert_date = concert_date.replace(year = concert_date.year + 1)
  
    #has the concert already passed?
    return (concert_date < today_date)


class Concert(Model):
  objects = ConcertManager()
  title = CharField(max_length=2550)
  date = TextField()
  description = TextField()
  highlights = TextField(blank=True, null=True)
  image = TextField(blank=True, null=True)
  youtube_embed_link = URLField(blank=True, null=True)
  def __unicode__(self):
    return self.title

class ConcertAnswerScore(Model):
  concert = ForeignKey(Concert)
  answer = ForeignKey(Answer)
  score = IntegerField()
  def __unicode__(self):
    return str(self.concert) + ' Ans:' + str(self.answer.pk) + ' Score:' + str(self.score)
