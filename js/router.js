function goToNextPage(answerObject) {
  var id = answerObject.attributes.id;
  var new_question = answerObject.attributes.new_question;
  var new_question_id = new_question.replace(window.location.origin + '/api/questions/', '');
  if (new_question_id == "666") {
    window.location = '/suggestions/' + ORCA.session.attributes.id + '/';
    return;
  }//if
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
    ORCA.router.navigate('questions/' + new_question_id, {trigger: true});
  });
}//goToNextPage

function showComment(comment) {
  if (!comment) {
    return;
  }//if

  //hidden by default
  $('.question').before('<div class="comment">' + comment + '</div>');

  var comment_length = comment.length * 50;
  if (comment_length < 800) comment_length = 800;
  $.when(
    $('.comment').fadeIn().delay(comment_length).fadeOut('slow')
  ).then(function() {
    $('.comment').remove();
  });
}//if

function renderAnswersOnQuestionPage(answers) {
  $('.answers').html('');
  $.each(answers, function(index, answerObject) {
    //grab info
    var answer = answerObject.attributes.answer;
    var id = answerObject.attributes.id;

    //add the answer to the page
    var html = '<div class="answer answer-' + id + '">';
    html += '<a href="javascript:void(0);">' + answer + '</a>';
    html += '</div>';
    $('.answers').append(html);

    //answer click handler
    $('.answer-' + id).click(function() {
      $('.answer').unbind('click');
      var answer_clicked = ORCA.answers.get(id);
      $.when(
        $('.answer').fadeOut('slow'),
        $('.question').fadeOut('slow'),
        $('.back-button a').fadeOut('slow')
      ).then(function() {
        $('.question').html('');
        $('.question').show();
        showComment(answer_clicked.attributes.comment);
        goToNextPage(answerObject);
      });
    });
  });

  //once this is done, show answers so there's no delay
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
    $('.back-button a').fadeIn('slow');
    $('.back-button a').unbind('click');
    $('.back-button a').click(function() {
      //pop current page, then pop previous page to use;
      //navigate will add the previous page back on
      //only use back button if not on first page
      if (ORCA.router.history.length > 1) {
        ORCA.router.history.pop();
        ORCA.router.navigate(ORCA.router.history.pop().fragment, {trigger: true});
      }//if
    });
  },
});
