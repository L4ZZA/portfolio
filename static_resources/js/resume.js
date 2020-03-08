(function ($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function () {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#sideNav'
  });

  // -- example from bootstrap.com
  // $('#myModal').on('shown.bs.modal', function () {
  // $('#myInput').trigger('focus')
  // })

  // $('#portfolioModal1').on('shown.bs.modal', function () {
  //   $(".modal-open").removeAttr("style");
  //   $(".modal-open").addClass("fixModal");
  // });

  // $('#portfolioModal1').on('hidden.bs.modal', function () {
  //   $(".modal-open").removeAttr("style");
  //   $(".modal-open").removeClass("fixModal");
  // });
  
  // $('#portfolioModal1').on('show.bs.modal', function () { $('body.modal-open').addClass("fixModal"); }); 
  // $('#portfolioModal1').on('hidden.bs.modal', function () { $('body.modal-open').removeClass("fixModal"); });

})(jQuery); // End of use strict
