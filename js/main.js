$(document).ready(function() {
  ORCA.questions = new Questions(ORCA.questions);
  ORCA.answers = new Answers(ORCA.answers);
  ORCA.session = new Session({
    username: "Anonymous",
    ip: ORCA.ip_address,
    current_question: window.location.origin + '/api/questions/1',
    session_token: Math.random().toString(36).slice(2),
  });
  ORCA.router = new ORCARouter();
  Backbone.history.start();
  ORCA.router.navigate('questions/1', {trigger: true});
  ORCA.session.save({
    'error': function() {
      window.location = 'api-auth/login?next=/';
    },
  });
});
