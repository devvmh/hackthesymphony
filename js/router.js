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
        $('.question').fadeOut('slow'),
        $('#back-button a').fadeOut('slow')
      ).then(function() {
        $('.question').html('');
        $('.question').show();
        console.log(value.attributes.comment);
        if (value.attributes.comment) {
          console.log("got here");
          $('.question').before('<div class="comment">' + value.attributes.comment + '</div>');
          $.when(
            $('.comment').fadeIn('slow').delay(2000).fadeOut('slow')
          ).then(function() {
            $('.comment').remove();
            ORCA.router.navigate(new_question, {trigger: true});
          });
        } else {
          ORCA.router.navigate(new_question, {trigger: true});
        }//if
      });
    });
  });
$('.answer').fadeIn('slow');
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
    $('.question').hide();
    $('.question').html(q.attributes.question);
    $('.question').fadeIn('slow');
    
    //render answers
    renderAnswersOnQuestionPage(q.answers());

    //set up back button
    $('#back-button a').fadeIn('slow');
    $('#back-button a').unbind('click');
    $('#back-button a').click(function() {
      //pop current page, then pop previous page to use;
      //navigate will add the previous page back on
      ORCA.router.history.pop();
      ORCA.router.navigate(ORCA.router.history.pop().fragment, {trigger: true});
    });
  },
});
