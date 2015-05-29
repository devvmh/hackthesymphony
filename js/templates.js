//django-style templates
_.templateSettings = {
  'interpolate': /\{\{(.+?)\}\}/g,
  'evaluate': /\{%(.+?)%\}/g
};

ORCA.templates = {};
ORCA.templates.answer = _.template(
  '<div class="answer answer-{{ answer.attributes.id }}">' +
  '  <a href="javascript:void(0);">{{ answer.attributes.answer }}</a>' +
  '</div>'
);
ORCA.templates.question = _.template(
  '{{ question.attributes.question }}'
);
