function declareModelsAndCollections() {
  Question = Backbone.Model.extend({
  });
  Answer = Backbone.Model.extend({
  });
  Session = Backbone.Model.extend({
  });
  SessionAnswer = Backbone.Model.extend({
  });
  Questions = Backbone.Collection.extend({
    url: '/api/questions',
    model: Question,
    parse: function(data) {
      return data.results;
    },
  });
  Answers = Backbone.Collection.extend({
    url: '/api/answers',
    model: Answer,
    parse: function(data) {
      return data.results;
    },
  });
  Sessions = Backbone.Collection.extend({
    url: '/api/sessions',
    model: Session,
    parse: function(data) {
      return data.results;
    },
  });
  SessionAnswers = Backbone.Collection.extend({
    url: '/api/session-answers',
    model: SessionAnswer,
    parse: function(data) {
      return data.results;
    },
  });
}//declareModelsAndCollections

function declareMainObject() {
  HDIS = new Object();
  HDIS.questions = new Questions();
  HDIS.questions.fetch();
  HDIS.answers = new Answers();
  HDIS.answers.fetch();
  HDIS.session = new Session();
}//declareMainObject

$(document).ready(function() {
  declareModelsAndCollections();
  declareMainObject();
});
