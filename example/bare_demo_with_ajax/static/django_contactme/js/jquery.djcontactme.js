/*
 * jquery.djcontactme
 * https://github.com/danirus/django-contactme
 *
 * Copyright (c) 2015 Daniel Rus Morales
 * Licensed under the MIT License.
 */
(function($) {
  var $contactme;
  
  $.fn.djcontactme = function(opts) {
    var opts = $.extend({}, $.fn.djcontactme.opts, opts);
    $contactme = this;
    var active_input = null;
    
    function setActiveInput() {
      active_input = this.name;
    }

    function onCformSubmit(event) {
      event.preventDefault();
      var $form = $(event.target);
      var preview = (active_input == 'preview');
      var postaction = $form.attr('action') || './';
      var ajaxaction = $form.attr('data-ajax-action');
      var contactdata = $form.serialize() + (preview ? '&preview=1' : '');
      
      $.ajax({
        type: 'POST',
        url: ajaxaction || postaction,
        data: contactdata,
        dataType: 'json',
        success: function(data) {
          var $form = $(event.target);
          // empty preview
          $('.' + opts.previewClass).html('').hide();
          $('.' + opts.discardedClass).html('').hide();
          // remove errors
          $form.find('.errors').hide();
          $form.find('.' + opts.fieldErrorsClass).remove();
          $form.find('.error').removeClass('error');
          if(data.status=='errors') {
            $form.find('.errors').show();
            for(var field_name in data.errors) {
              var field = $(event.target.elements[field_name]);
              if(opts.addFieldWrapperClass) {
                field.parent().addClass(opts.fieldWrapperClass);
              }
              if(opts.addFieldErrorsAfterFieldWrapper) {
                field.parent().after(data.errors[field_name]);
              } else {
                field.after(data.errors[field_name]);
              }
            }
          } else if(data.status=='preview') {
            $('.' + opts.previewClass).html(data.html).show();
          } else if(data.status=='discarded') {
            $('.' + opts.discardedClass).html(data.html).show();
          } else if(data.status=='success') {
            $('.' + opts.confirmationSentClass).html(data.html).show();
          }
        },
        error: function() {
          $('.' + opts.previewClass).html("An error ocurred while sending the form.").show();
        }
      });
    }
    
    if($contactme.length > 0) {
      // Detect last active input.
      // Submit if return is hit or any button other than preview is hit.
      $contactme.find(':input').focus(setActiveInput).mousedown(setActiveInput);
      contactme.submit(submitForm);
    }
  };

  $.fn.djcontactme.opts = {
    addFieldWrapperClass: true,
    fieldWrapperClass: "error",
    addFieldErrorsAfterFieldWrapper: true,
    fieldErrorsClass: "errorlist",
    previewClass: "djcontactme-msg",
    discardedClass: "djcontactme-msg",
    confirmationSentClass: "djcontactme"
  }
  
})(jQuery);
