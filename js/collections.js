BaseDjangoCollection = Backbone.Collection.extend({
  parse: function(data) {
    return data.results;
  },
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
