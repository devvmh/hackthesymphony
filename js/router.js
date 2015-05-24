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
    "questions/:id": "renderQuestion",
  },
  renderQuestion(id) {
    console.log("got here 2");
    //render question text
    q = ORCA.questions.get(id);
    $('.question p').html(q.attributes.question);
    
    //render answers
    $('.answers').html('');
    $.each(q.answers(), function(index, value) {
      var answer = value.attributes.answer;
      var id = value.attributes.id;
      var new_question = value.attributes.new_question;
      new_question = new_question.replace(window.location.origin + '/api/', '');
      var html = '<div class="answer answer-' + id + '">';
      html += '<a href="javascript:void(0);">' + answer + '</a>';
      html += '</div>';
      $('.answers').append(html);
      $('.answer-' + id + ' a').click(function() {
        ORCA.router.navigate(new_question, {trigger: true});
      });
    });

    //set up back button
    $('#back-button a').unbind('click');
    $('#back-button a').click(function() {
      console.log(ORCA.router.history);
      //pop current page, then pop previous page to use;
      //navigate will add the previous page back on
      ORCA.router.history.pop();
      ORCA.router.navigate(ORCA.router.history.pop().fragment, {trigger: true});
      console.log(ORCA.router.history);
    });
  },
});
