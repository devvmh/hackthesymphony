function renderAnswersOnQuestionPage(answers) {
  $('.answers').html('');
  $.each(answers, function(index, value) {
    var answer = value.attributes.answer;
    var id = value.attributes.id;
    var comment = value.attributes.comment;
    var new_question = value.attributes.new_question;
    new_question = new_question.replace(window.location.origin + '/api/', '');
    var html = '<div class="answer answer-' + id + '">';
    html += '<a href="javascript:void(0);">' + answer + '</a>';
    html += '</div>';
    $('.answers').append(html);
    $('.answer-' + id + ' a').click(function() {
      $.when(
        $('.answer').fadeOut('slow'),
        $('.question').fadeOut('slow')
      ).then(function() {
        $('.question').html('');
        $('.question').show();
        if (value.attributes.comment) {
          $.when(
            $('.question').before('<div class="comment">' + value.attributes.comment + '</div>'),
            $('.comment').fadeIn('slow'),
            $('.comment').delay(2000).fadeOut('slow'),
            $('.comment').remove()
          ).then(function() {
            ORCA.router.navigate(new_question, {trigger: true});
          });
        } else {
          ORCA.router.navigate(new_question, {trigger: true});
        }//if
      });
    });
  });
}//renderAnswersOnQuestionPage

ORCARouter = Backbone.Router.extend({
  initialize: function(options) {
    this.history = [];
    this.listenTo(this, 'route', function(name, args) {
      this.history.push({
        name : name,
        args : args,
        fragment : Backbone.history.fragment
      });
    });
  },
  routes: {
    "questions/:id": "renderQuestionPage",
  },
  renderQuestionPage(id) {
    //render question text
    q = ORCA.questions.get(id);
    $('.question').html(q.attributes.question);
    
    //render answers
    renderAnswersOnQuestionPage(q.answers());

    //set up back button
    $('#back-button a').unbind('click');
    $('#back-button a').click(function() {
      //pop current page, then pop previous page to use;
      //navigate will add the previous page back on
      ORCA.router.history.pop();
      ORCA.router.navigate(ORCA.router.history.pop().fragment, {trigger: true});
    });
  },
});
