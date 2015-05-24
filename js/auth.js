/* alias away the sync method */
Backbone._sync = Backbone.sync;

/* define a new sync method */
Backbone.sync = function(method, model, options) {
    /* only need a token for non-get requests */
    if (method == 'create' || method == 'update' || method == 'delete') {
        var csrftoken = getCookie('csrftoken');

        options.beforeSend = function(xhr){
          xhr.setRequestHeader('X-CSRFToken', csrftoken);
        };
    }//if

    /* proxy the call to the old sync method */
    return Backbone._sync(method, model, options);
};
