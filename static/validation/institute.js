$(function () {
  //Initialize form validation on the registration form.
  //It has the name attribute "registration"

  
  $("#institute").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      institute_name: "required",
      website_name : "required",
      person_contact:"required",
      country: "required",
      state: "required",
      city: "required",
      address: "required",
      description: "required",


      year_established: {
        required: true,
        // Specify that email should be validated
        // by the built-in "email" rule
        date: true,
      },
      email: {
        required: true,
        // Specify that email should be validated
        // by the built-in "email" rule
        email: true,
      },
      contact: {
        required: true,
        maxlength: 10,
        minlength: 10,      
      },
      pincode:{
        required:true,
        maxlength:6,
        minlength:6,
      },
      password: {
        required: true,
        minlength: 8,
      },
      cpassword: {
        required: true,
        equalTo: "#password",
      },
    },
    // Specify validation error messages
    messages: {
      first_name: "Please enter your first name!!",
      last_name : "Please enter your last name!!",
      email: {
        email: "Please enter a valid email address!!",
       }, 
      mobile_number: {
        required: "Please enter phone number",
        maxlength: "Please enter a valid phone number!!",
        minlength: "Please enter a valid phone number!!",
        
      },
      password: {
        required: "Please provide a password",
        minlength: "Password must be at least 8 characters long",
      },
      cpassword: {
        required: "Please confirm your password!!",
        equalTo : "password must be same",
      },
      address:"Please give your address!!",
      pincode:{
         required: "Please enter pincode!!",
          maxlength: "Please enter a valid Pinocde!!",
          minlength: "Please enter a valid Pinocde!!",
        
      },

      
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    // submitHandler: function(form) {
    //   form.submit();
    // }
  });
});
