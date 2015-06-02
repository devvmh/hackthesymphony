function backButtonOnClick() {
  //only use back button if not on first page
  if (ORCA.router.history.length > 1) {
    //pop current page, then pop previous page to use;
    //navigate will add the previous page back on
    ORCA.router.history.pop();
    ORCA.router.navigate(ORCA.router.history.pop().fragment, {trigger: true});
  }//if
}//backButtonOnClick

function answerOnClick(ans) {
  $('.answer').unbind('click');
  $(document).queue(function() {
    popUpComment(ans, this);
  });
  goToNextPage(ans);
}//answerOnClick

function clearPage() {
  $('.question, .answers').html('');
  $('.comment').remove()
}//clearPage

function fadePage() {
  $('.question, .answers, .back-button a').fadeOut('slow');
  $('.question, .answers').html('');
}//fadePage

function popUpComment(ans, dequeuer) {
  if (!ans.attributes.comment) {
    $(dequeuer).dequeue();
    return;
  }

  $('.question, .answers, .back-button a').fadeOut('slow').promise().done(function() {
    var comment = ans.attributes.comment;
    var comment_length = comment.length * 50;
    if (comment_length < 800) comment_length = 800;

    //chain then calls to run animations in sequence
    //hidden by default, but populate html
    $('.question').before(ORCA.templates.comment({answer: ans}))
    $('.comment').fadeIn().delay(comment_length).fadeOut('slow');
    $(dequeuer).dequeue();
  });
}//answerOnClick

function goToNextPage(ans) {
  var id = ans.attributes.id;
  var new_question = ans.attributes.new_question;
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
  ORCA.session.attributes.current_question = ans.attributes.new_question;

  session_answer.save(session_answer.attributes, {'success': function() {
    ORCA.session.save(ORCA.session.attributes, {'success': function() {
    ORCA.router.navigate('questions/' + new_question_id, {trigger: true});
  }})}});
}//goToNextPage

ORCARouter = Backbone.Router.extend({
  initialize: function(options) {
    //set up history storage for use with back button
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

    $('.question, .answers, .back-button a').fadeOut('slow').promise().done(function() {

      $('.question, .answers').html('');
      $('.question').html(ORCA.templates.question({question: q}));
     
      //render answers
      $.each(q.answers(), function(index, ans) {
        //add the answer to the page
        $('.answers').append(ORCA.templates.answer({answer: ans}));
     
        //answer click handler
        $('.answer-' + ans.attributes.id).click(function() {
          answerOnClick(ans);
        });
      });
     
      //set up back button
      $('.back-button a').unbind('click');
      $('.back-button a').click(function() {
        backButtonOnClick();
      });
 
      //once this is done, show everything together
      $('.question, .answers, .back-button a').fadeIn('slow');
    });
  },
});

