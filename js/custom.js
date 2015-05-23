$(document).ready(function() {
  Question = Backbone.Model.extend({
  });
  Answer = Backbone.Model.extend({
  });

  Questions = Backbone.Collection.extend({
    url: '/api/questions',
    model: Question,
  });
  Answers = Backbone.Collection.extend({
    url: '/api/answers',
    model: Answer,
  });

  qlst = new Questions();
  qlst.fetch();
  alst = new Answers();
  alst.fetch();
});
