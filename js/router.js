function goToNextPage(answerObject) {
  var id = answerObject.attributes.id;
  var new_question = answerObject.attributes.new_question;
  var session_answer = new SessionAnswer({
    session: ORCA.session.url(),
    question: ORCA.session.attributes.current_question,
    answer: ORCA.answers.get(id).url(),
  });
  ORCA.session.attributes.current_question = answerObject.attributes.new_question;
  $.when(
    session_answer.save(),
    ORCA.session.save()
  ).then(function() {
    new_question = new_question.replace(window.location.origin + '/api/', '');
    ORCA.router.navigate(new_question, {trigger: true});
  });
}//goToNextPage

function renderAnswersOnQuestionPage(answers) {
  $('.answers').html('');
  $.each(answers, function(index, answerObject) {
    var answer = answerObject.attributes.answer;
    var id = answerObject.attributes.id;
    var comment = answerObject.attributes.comment;
    var new_question = answerObject.attributes.new_question;
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
        if (answerObject.attributes.comment) {
          $('.question').before('<div class="comment">' + answerObject.attributes.comment + '</div>');
          $.when(
            $('.comment').fadeIn('slow').delay(2000).fadeOut('slow')
          ).then(function() {
            $('.comment').remove();
            goToNextPage(answerObject);
          });
        } else {
          goToNextPage(answerObject);
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
    $('#back-button a').unbind('click');
    $('#back-button a').click(function() {
      //pop current page, then pop previous page to use;
      //navigate will add the previous page back on
      ORCA.router.history.pop();
      ORCA.router.navigate(ORCA.router.history.pop().fragment, {trigger: true});
    });
  },
});
