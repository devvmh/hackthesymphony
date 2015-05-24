// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function declareModelsAndCollections() {
  /* alias away the sync method */
  Backbone._sync = Backbone.sync;

  /* define a new sync method */
  Backbone.sync = function(method, model, options) {
      /* only need a token for non-get requests */
      if (method == 'create' || method == 'update' || method == 'delete') {
          var csrftoken = getCookie('csrftoken');

          options.beforeSend = function(xhr){
            var user = "admin";// your actual username
            var pass = "password";// your actual password
            var token = user.concat(":", pass);
            xhr.setRequestHeader('Authorization', ("Basic ".concat(btoa(token))));
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
          };
      }//if

      /* proxy the call to the old sync method */
      return Backbone._sync(method, model, options);
  };
  BaseDjangoCollection = Backbone.Collection.extend({
    parse: function(data) {
      return data.results;
    },
  });
  Question = Backbone.Model.extend({
  });
  Question.prototype.answers = function() {
    return ORCA.answers.where({
      old_question: window.location.href + this.url().substring(1),
    });
  };
  Answer = Backbone.Model.extend({
  });
  Session = Backbone.Model.extend({
    urlRoot: '/api/sessions',
  });
  SessionAnswer = Backbone.Model.extend({
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
}//declareModelsAndCollections

function declareMainObject() {
  ORCA.questions = new Questions();
  ORCA.questions.fetch();
  ORCA.answers = new Answers();
  ORCA.answers.fetch();
  ORCA.first_question_url = window.location.href + 'api/questions/1';
  ORCA.session = new Session({
    username: "Anonymous",
    ip: ORCA.ip_address,
    current_question: ORCA.first_question_url,
  });
  ORCA.session.save();
}//declareMainObject

function populateCurrentQuestion(id) {
  q = ORCA.questions.get(id);
  console.log(q);
}//populateCurrentQuestion

$(document).ready(function() {
  declareModelsAndCollections();
  declareMainObject();
  $.when(ORCA.questions.fetch(), 
         ORCA.answers.fetch(), 
         ORCA.session.save()).then(function() {
    populateCurrentQuestion(1);
  });
});
