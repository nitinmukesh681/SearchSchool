// Wait for the DOM to be ready
$(function () {
  //Initialize form validation on the registration form.
  //It has the name attribute "registration"

  
  $("#setYourArticle").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      heading: "required",
      about : "required",
      article:"required",
     
    },
    // Specify validation error messages
    messages: {
      heading: "Please enter your heading!!",
      about : "Please enter your about!!",
      article : "Please enter your article!!",
      

      
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    // submitHandler: function(form) {
    //   form.submit();
    // }
  });
});
