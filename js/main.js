$(document).ready(function() {
  ORCA.questions = new Questions(ORCA.questions);
  ORCA.answers = new Answers(ORCA.answers);
  ORCA.router = new ORCARouter();
  Backbone.history.start();

//  if (localStorage.getItem('session')) {
//    ORCA.session = new Session(JSON.parse(localStorage.getItem('session')));
//    var current_route = ORCA.session.attributes.current_question.replace(window.location.origin + '/api/', '');
//    ORCA.router.navigate(current_route, {trigger: true});
//  } else {
    ORCA.session = new Session({
      username: "Anonymous",
      ip: ORCA.ip_address,
      current_question: window.location.origin + '/api/questions/1',
      session_token: Math.random().toString(36).slice(2),
    });
    ORCA.router.navigate('questions/1', {trigger: true});
    ORCA.session.save();
    localStorage.setItem('session', JSON.stringify(ORCA.session));
//  }//if
});
