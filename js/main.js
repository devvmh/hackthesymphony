$(document).ready(function() {
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

  qlst = new Questions();
  qlst.fetch();
  alst = new Answers();
  alst.fetch();
  session = new Session();
});
