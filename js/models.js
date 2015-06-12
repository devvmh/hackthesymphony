Question = Backbone.Model.extend({
  urlRoot: '/api/questions',
});
Question.prototype.answers = function() {
  return ORCA.answers.where({
    old_question: window.location.origin + this.url(),
  });
};
Answer = Backbone.Model.extend({
  urlRoot: '/api/answers',
});
Session = Backbone.Model.extend({
  urlRoot: '/api/sessions',
});
SessionAnswer = Backbone.Model.extend({
  urlRoot: '/api/session-answers',
});
