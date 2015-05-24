function declareMainObject() {
}//declareMainObject

$(document).ready(function() {
  ORCA.questions = new Questions();
  ORCA.answers = new Answers();
  ORCA.session = new Session({
    username: "Anonymous",
    ip: ORCA.ip_address,
    current_question: window.location.origin + '/api/questions/1',
  });
  $.when(ORCA.questions.fetch(), 
         ORCA.answers.fetch(), 
         ORCA.session.save()).then(function() {
    ORCA.router = new ORCARouter();
    Backbone.history.start();
    ORCA.router.navigate('questions/1', {trigger: true});
  });
});
