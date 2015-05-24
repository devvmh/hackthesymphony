function declareMainObject() {
  ORCA.questions = new Questions();
  ORCA.answers = new Answers();
  ORCA.first_question_url = window.location.origin + '/api/questions/1';
  ORCA.session = new Session({
    username: "Anonymous",
    ip: ORCA.ip_address,
    current_question: ORCA.first_question_url,
  });
}//declareMainObject

$(document).ready(function() {
  declareMainObject();
  $.when(ORCA.questions.fetch(), 
         ORCA.answers.fetch(), 
         ORCA.session.save()).then(function() {
    ORCA.router = new ORCARouter();
    Backbone.history.start();
    ORCA.router.navigate('questions/1', {trigger: true});
  });
});
