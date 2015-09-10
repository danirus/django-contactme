(function($) {
  $.fn.djcontactme = function(options) {

    var settings = $.extend({
      addFieldWrapperClass: true,
      fieldWrapperClass: "error",
      addFieldErrorsAfterFieldWrapper: true,
      fieldErrorsClass: "errorlist",
      previewClass: "djcontactme-msg",
      discardedClass: "djcontactme-msg",
      confirmationSentClass: "djcontactme"
    }, options);

    function setActiveInput() {
      console.log('setActiveInput() called');
      active_input = this.name;
    }

    function onCformSubmit(event) {
      event.preventDefault();
      var cform = $(event.target);
      var preview = (active_input == 'preview');
      var postaction = cform.attr('action') || './';
      var ajaxaction = cform.attr('data-ajax-action');
      var cformdata = cform.serialize() + (preview ? '&preview=1' : '');
      
      $.ajax({
        type: 'POST',
        url: ajaxaction || postaction,
        data: cformdata,
        dataType: 'json',
        success: function(data) {
          var $form = $(event.target);
          // empty preview
          $('.'+settings.previewClass).html('').hide();
          $('.'+settings.discardedClass).html('').hide();
          // remove errors
          $form.find('.errors').hide();
          $form.find('.'+settings.fieldErrorsClass).remove();
          $form.find('.error').removeClass('error');
          if(data.status=='errors') {
            $form.find('.errors').show();
            for(var field_name in data.errors) {
              var field = $(event.target.elements[field_name]);
              if(settings.addFieldWrapperClass) {
                field.parent().addClass(settings.fieldWrapperClass);
              }
              if(settings.addFieldErrorsAfterFieldWrapper) {
                field.parent().after(data.errors[field_name]);
              } else {
                field.after(data.errors[field_name]);
              }
            }
          } else if(data.status=='preview') {
            $('.'+settings.previewClass).html(data.html).show();
          } else if(data.status=='discarded') {
            $('.'+settings.discardedClass).html(data.html).show();
          } else if(data.status=='success') {
            $('.'+settings.confirmationSentClass).html(data.html).show();
          }
        },
        error: function(data) {
          $('.'+settings.previewClass).html("An error ocurred while sending the form.").show();
        }
      });
    }
    
    var cform = this;
    if(cform.length > 0) {
      // Detect last active input.
      // Submit if return is hit or any button other than preview is hit.
      cform.find(':input').focus(setActiveInput).mousedown(setActiveInput);
      cform.submit(onCformSubmit);
    }
    console.log('djcontactme has been initialize');
  }
})(jQuery);
