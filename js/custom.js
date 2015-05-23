$(document).ready(function() {
  Questions = Backbone.Collection.extend({
    url: '/raw/questions',
  });
  Question = Backbone.Model.extend({
    idAttribute: "pk",
  });
  Answers = Backbone.Collection.extend({
    url: '/raw/answers',
  });
  Answer = Backbone.Model.extend({
    idAttribute: "pk",
  });
  qlst = new Questions();
  qlst.fetch();
  alst = new Answers();
  alst.fetch();
});
