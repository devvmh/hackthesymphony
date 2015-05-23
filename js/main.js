function declareModelsAndCollections() {
  Session = Backbone.Model.extend({
  });
  Questions = Backbone.Collection.extend({
    url: '/api/questions',
  });
  Answers = Backbone.Collection.extend({
    url: '/api/answers',
  });
  Sessions = Backbone.Collection.extend({
    url: '/api/sessions',
    model = Session,
  });
  SessionAnswers = Backbone.Collection.extend({
    url: '/api/session-answers',
  });
}

function declareMainObject() {
  HDIS = new Object();
  HDIS.questions = new Questions();
  HDIS.questions.fetch();
  HDIS.answers = new Answers();
  HDIS.answers.fetch();
  HDIS.session = new Session();

$(document).ready(function() {
  declareModelsAndCollections();
  declareMainObject();
});
