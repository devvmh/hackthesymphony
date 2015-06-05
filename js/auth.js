/* alias away the sync method */
Backbone._sync = Backbone.sync;

/* define a new sync method */
Backbone.sync = function(method, model, options) {
    /* only need a token for non-get requests */
    if (method == 'create' || method == 'update' || method == 'delete') {
        var csrf_token = getCookie('csrftoken');
        var session_token = ORCA.session.attributes.session_token;

        options.beforeSend = function(xhr){
          xhr.setRequestHeader('X-CSRFToken', csrf_token);
          xhr.setRequestHeader('X-Session-Token', session_token);
        };
    }//if

    /* proxy the call to the old sync method */
    return Backbone._sync(method, model, options);
};
