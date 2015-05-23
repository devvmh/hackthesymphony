$(document).ready(function() {
  Question = Backbone.Model.extend({
  });
  Answer = Backbone.Model.extend({
  });

  Questions = Backbone.Collection.extend({
    url: '/raw/questions',
    model: Question,
  });
  Answers = Backbone.Collection.extend({
    url: '/raw/answers',
    model: Answer,
  });

  qlst = new Questions();
  qlst.fetch();
  alst = new Answers();
  alst.fetch();
});
