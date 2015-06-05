ORCA = new Object();
ORCA.ip_address = "{{ ip_address }}";
ORCA.questions = {{ questions_json | safe }};
ORCA.questions = $.map(ORCA.questions, function(elt, index) {
  //we only want the fields portion + the pk as id for backbone
  elt.fields.id = elt.pk;
  return elt.fields;
});
ORCA.answers = {{ answers_json | safe }};
ORCA.answers = $.map(ORCA.answers, function(elt, index) {
  //we only want the fields portion + the pk as id for backbone
  elt.fields.id = elt.pk;
  elt.fields.old_question = window.location.origin + '/api/questions/' + elt.fields.old_question;
  elt.fields.new_question = window.location.origin + '/api/questions/' + elt.fields.new_question;
  return elt.fields;
});
