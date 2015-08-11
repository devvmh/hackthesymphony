$(document).ready(function() {
  ORCA.questions = new Questions(ORCA.questions);
  ORCA.answers = new Answers(ORCA.answers);
  ORCA.router = new ORCARouter();
  Backbone.history.start();

  if (localStorage.getItem('session')) {
    ORCA.session = new Session(JSON.parse(localStorage.getItem('session')));
    var current_route = '/questions/' + ORCA.session.attributes.current_question;
    ORCA.router.navigate(current_route, {trigger: true});
    ORCA.session.save(ORCA.session.attributes, {error: function() {
      alert("invalid session");
      localStorage.removeItem('session');
      window.location = "/";
    }});
  } else {
    ORCA.session = new Session({
      username: "Anonymous",
      ip: ORCA.ip_address,
      current_question: 1,
      session_token: Math.random().toString(36).slice(2),
      session_answers: [],
    });
    ORCA.router.navigate('questions/1', {trigger: true});
    localStorage.setItem('session', JSON.stringify(ORCA.session));
    ORCA.session.save();
  }//if
});
