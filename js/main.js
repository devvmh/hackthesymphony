$(document).ready(function() {
  ORCA.questions = new Questions();
  ORCA.answers = new Answers();
  ORCA.session = new Session({
    username: "Anonymous",
    ip: ORCA.ip_address,
    current_question: window.location.origin + '/api/questions/1',
  });
  $.when(ORCA.questions.fetch({
           'error': function() {
             window.location = 'api-auth/login?next=/';
           },
         }),
         ORCA.answers.fetch({
           'error': function() {
             window.location = 'api-auth/login?next=/';
           },
         })
  ).then(function() {
    ORCA.router = new ORCARouter();
    Backbone.history.start();
    ORCA.router.navigate('questions/1', {trigger: true});
    ORCA.session.save({
      'error': function() {
        window.location = 'api-auth/login?next=/';
      },
    });
  });
});
