BaseDjangoCollection = Backbone.Collection.extend({
});
Questions = BaseDjangoCollection.extend({
  url: '/api/questions',
  model: Question,
});
Answers = BaseDjangoCollection.extend({
  url: '/api/answers',
  model: Answer,
});
Sessions = BaseDjangoCollection.extend({
  url: '/api/sessions',
  model: Session,
});
SessionAnswers = BaseDjangoCollection.extend({
  url: '/api/session-answers',
  model: SessionAnswer,
});
