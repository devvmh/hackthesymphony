BaseDjangoCollection = Backbone.Collection.extend({
  parse: function(data) {
    return data.results;
  },
});
Questions = BaseDjangoCollection.extend({
  url: '/api/questions',
  model: Question,
  parse: function(data) {
    return data.results;
  },
});
Answers = BaseDjangoCollection.extend({
  url: '/api/answers',
  model: Answer,
  parse: function(data) {
    return data.results;
  },
});
Sessions = BaseDjangoCollection.extend({
  url: '/api/sessions',
  model: Session,
  parse: function(data) {
    return data.results;
  },
});
SessionAnswers = BaseDjangoCollection.extend({
  url: '/api/session-answers',
  model: SessionAnswer,
  parse: function(data) {
    return data.results;
  },
});
