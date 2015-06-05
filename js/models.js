Question = Backbone.Model.extend({
});
Question.prototype.answers = function() {
  return ORCA.answers.where({
    old_question: window.location.origin + this.url(),
  });
};
Answer = Backbone.Model.extend({
});
Session = Backbone.Model.extend({
  urlRoot: '/api/sessions',
});
SessionAnswer = Backbone.Model.extend({
  urlRoot: '/api/session-answers',
});
