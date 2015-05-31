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
  $.when(
    session_answer.save(),
    ORCA.session.save()
  ).then(function() {
    ORCA.router.navigate('questions/' + new_question_id, {trigger: true});
  });
}//goToNextPage

function transitionToNextQuestion(ans) {
  $('.answer').unbind('click');

  var comment = ans.attributes.comment;
  var comment_length = comment.length * 50;

  //chain then calls to run animations in sequence
  $.when().then(function() {
    $('.question, .answer, .back-button a').fadeOut('slow');
  }).then(function() {
    //clear the content for later
    $('.question').html('');
    $('.answers').html('');
  }).then(function() {
    if (ans.attributes.comment) {
      //floor on value of comment_length
      if (comment_length < 800) comment_length = 800;
    
      //hidden by default, but populate html
      $('.question').before('<div class="comment">' + comment + '</div>');
    }//if
  }).then(function() {
    //fade in, wait a bit, fade out, then remove it and go to next page
    $.when(
      $('.comment').fadeIn().delay(comment_length).fadeOut('slow')
    ).then(function() {
      $('.comment').remove(); //if it's even there
      goToNextPage(ans);
    });
  });
} //transitionToNextQuestion

function clearPage() {
        $('.question').html('');
        $('.answers').html('');
} //clearPage

function backButtonOnClick() {
      //only use back button if not on first page
      if (ORCA.router.history.length > 1) {
        //clear question and answer
        clearPage();
        //pop current page, then pop previous page to use;
        //navigate will add the previous page back on
        ORCA.router.history.pop();
        ORCA.router.navigate(ORCA.router.history.pop().fragment, {trigger: true});
      }//if
} //backButtonOnClick

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
    $('.question').hide();
    $('.question').html(ORCA.templates.question({question: q}));
    
    //render answers
    $.each(q.answers(), function(index, ans) {
      //add the answer to the page
      $('.answers').append(ORCA.templates.answer({answer: ans}));
  
      //answer click handler
      $('.answer-' + ans.attributes.id).click(function() {
        transitionToNextQuestion(ans);
      });
    });
  
    //set up back button
    $('.back-button a').unbind('click');
    $('.back-button a').click(function() 
        {backButtonOnClick();
    });

    //once this is done, show everything together
    $('.question, .answer, .back-button a').fadeIn('slow');
  },
});
