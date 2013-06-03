$( document ).ready( function() {
    // Dummy button example
    //$( ".dummyinactive" ).click( function() {
    //  $( this ).toggleClass("dummyinactive");
    //  $( this ).toggleClass("dummyactive");
    //  $( "#nav_home" ).toggleClass("active");
    //});

    // Nav bar
    $( "#nav_home" ).click( function() {
      // Check if other blocks are visible. If so, hide them first.
      if ( $(".about").is(":visible") ) {
        $( ".about" ).toggle( "slide" );
        $( "#nav_about" ).toggleClass("active");
      }
      if ( $(".resume").is(":visible") ) {
        $( ".resume" ).toggle( "slide" );
        $( "#nav_resume" ).toggleClass("active");
      }
      if ( $(".contact").is(":visible") ) {
        $( ".contact" ).toggle( "slide" );
        $( "#nav_contact" ).toggleClass("active");
      }
      // Now display the selected block.
      $( ".home" ).toggle( "slide" );
      $( "#nav_home" ).toggleClass("active");
    });
    $( "#nav_about" ).click( function() {
      // Check if other blocks are visible. If so, hide them first.
      if ( $(".home").is(":visible") ) {
        $( ".home" ).toggle( "slide" );
        $( "#nav_home" ).toggleClass("active");
      }
      if ( $(".resume").is(":visible") ) {
        $( ".resume" ).toggle( "slide" );
        $( "#nav_resume" ).toggleClass("active");
      }
      if ( $(".contact").is(":visible") ) {
        $( ".contact" ).toggle( "slide" );
        $( "#nav_contact" ).toggleClass("active");
      }
      // Now display the selected block.
      $( ".about" ).toggle( "slide" );
      $( "#nav_about" ).toggleClass("active");
    });
    $( "#nav_resume" ).click( function() {
      // Check if other blocks are visible. If so, hide them first.
      if ( $(".home").is(":visible") ) {
        $( ".home" ).toggle( "slide" );
        $( "#nav_home" ).toggleClass("active");
      }
      if ( $(".about").is(":visible") ) {
        $( ".about" ).toggle( "slide" );
        $( "#nav_about" ).toggleClass("active");
      }
      if ( $(".contact").is(":visible") ) {
        $( ".contact" ).toggle( "slide" );
        $( "#nav_contact" ).toggleClass("active");
      }
      // Now display the selected block.
      $( ".resume" ).toggle( "slide" );
      $( "#nav_resume" ).toggleClass("active");
    });
    $( "#nav_contact" ).click( function() {
      // Check if other blocks are visible. If so, hide them first.
      if ( $(".home").is(":visible") ) {
        $( ".home" ).toggle( "slide" );
        $( "#nav_home" ).toggleClass("active");
      }
      if ( $(".about").is(":visible") ) {
        $( ".about" ).toggle( "slide" );
        $( "#nav_about" ).toggleClass("active");
      }
      if ( $(".resume").is(":visible") ) {
        $( ".resume" ).toggle( "slide" );
        $( "#nav_resume" ).toggleClass("active");
      }
      // Now display the selected block.
      $( ".contact" ).toggle( "slide" );
      $( "#nav_contact" ).toggleClass("active");
    });
});
