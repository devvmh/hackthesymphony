
ORCARouter = Backbone.Router.extend({
  routes: {
    "questions/:id": "renderQuestion",
  },
  renderQuestion(id) {
    q = ORCA.questions.get(id);
    $('.question p').html(q.attributes.question);
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
  },
});
