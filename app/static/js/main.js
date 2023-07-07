(function ($) {
    "use strict";

    // Spinner
    const spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    // Initiate the wowjs
    new WOW().init();

    // progress bar

    // Sticky Navbar
    $(document).ready(function () {
        // Check if the user has scrolled on page load
        checkScroll();

        // Trigger the checkScroll() function when the window is resized
        $(window).resize(checkScroll);

        // Trigger the checkScroll() function when the window is scrolled
        $(window).scroll(checkScroll);
    });

    function checkScroll() {
        // Check the position of the scroll bar and add/remove classes accordingly
        if ($(window).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm test-nav');
        }
    }

    function updateOverall(percentage) {
        const progressBar = $('#overall');
        progressBar.css('width', percentage + '%');

        if (percentage >= 0 && percentage <= 20) {
            progressBar.removeClass().addClass('progress-bar red');
        } else if (percentage > 20 && percentage <= 40) {
            progressBar.removeClass().addClass('progress-bar yellow');
        } else if (percentage > 40 && percentage <= 60) {
            progressBar.removeClass().addClass('progress-bar orange');
        } else if (percentage > 60 && percentage <= 80) {
            progressBar.removeClass().addClass('progress-bar lime');
        } else if (percentage > 80 && percentage <= 100) {
            progressBar.removeClass().addClass('progress-bar green');
        }
    }

    function updateCoffee(percentage) {
        const progressBar = $('#coffee');
        progressBar.css('width', percentage + '%');

        if (percentage >= 0 && percentage <= 20) {
            progressBar.removeClass().addClass('progress-bar red');
        } else if (percentage > 20 && percentage <= 40) {
            progressBar.removeClass().addClass('progress-bar yellow');
        } else if (percentage > 40 && percentage <= 60) {
            progressBar.removeClass().addClass('progress-bar orange');
        } else if (percentage > 60 && percentage <= 80) {
            progressBar.removeClass().addClass('progress-bar lime');
        } else if (percentage > 80 && percentage <= 100) {
            progressBar.removeClass().addClass('progress-bar green');
        }
    }

    function updateWifi(percentage) {
        const progressBar = $('#wifi');
        progressBar.css('width', percentage + '%');

        if (percentage >= 0 && percentage <= 20) {
            progressBar.removeClass().addClass('progress-bar red');
        } else if (percentage > 20 && percentage <= 40) {
            progressBar.removeClass().addClass('progress-bar yellow');
        } else if (percentage > 40 && percentage <= 60) {
            progressBar.removeClass().addClass('progress-bar orange');
        } else if (percentage > 60 && percentage <= 80) {
            progressBar.removeClass().addClass('progress-bar lime');
        } else if (percentage > 80 && percentage <= 100) {
            progressBar.removeClass().addClass('progress-bar green');
        }
    }

    function updateOPower(percentage) {
        const progressBar = $('#power');
        progressBar.css('width', percentage + '%');

        if (percentage >= 0 && percentage <= 20) {
            progressBar.removeClass().addClass('progress-bar red');
        } else if (percentage > 20 && percentage <= 40) {
            progressBar.removeClass().addClass('progress-bar yellow');
        } else if (percentage > 40 && percentage <= 60) {
            progressBar.removeClass().addClass('progress-bar orange');
        } else if (percentage > 60 && percentage <= 80) {
            progressBar.removeClass().addClass('progress-bar lime');
        } else if (percentage > 80 && percentage <= 100) {
            progressBar.removeClass().addClass('progress-bar green');
        }
    }


    // Smooth scrolling on the navbar links
    $(".navbar-nav a").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();

            $('html, body').animate({
                scrollTop: $(this.hash).offset().top - 60
            }, 1500, 'easeInOutExpo');

            if ($(this).parents('.navbar-nav').length) {
                $('.navbar-nav .active').removeClass('active');
                $(this).closest('a').addClass('active');
            }
        }
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 25,
        dots: false,
        loop: true,
        nav: true,
        navText: [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ],
        responsive: {
            0: {
                items: 1
            },
            992: {
                items: 2
            }
        }
    });

    $(window).on('load', function () {
        var i = 0;
        var speed = 50; /* The speed/duration of the effect in milliseconds */

        function typeWriter() {
            if (i < str.length) {
                $("#text").append(str.charAt(i));
                i++;
                setTimeout(typeWriter, speed);
            }
        }

        typeWriter();
    });







    // dynamic row
    $("#add_rows").click(function () {
        // each click on the `+` button adds a row to the table
        $("#data_container tbody").append(`<tr><td><input class="input-group mb-3 form-control" name="item" type="text">
</td><td><input class="input-group mb-3 form-control" name="price" type="text"></td></tr>`);
    });
    $("#submit_rows").click(function () {
        // `obj` for storing the inputs, and the `n` to make unrepeated keys
        var obj = {}, n = 0;
        // loop over the rows
        $("#data_container tbody tr").each(function () {
            // add an array to the object
            obj[`r${n}`] = [];
            // loop over the inputs of this row
            $(this).find("input").each(function (ind, input) {
                // add the value of the input to the array and make sure to remove any semicolon since
                // we will use it to separate the inputs
                var val = input.value.replace(/;/g, "");
                obj[`r${n}`].push(val);
            });
            // no need for the array, just join it to a string of values separated by semicolons
            obj[`r${n}`] = obj[`r${n}`].join(";");
            // increase the value of `n`
            n++;
        });
        // log the object to the console so you can see what we are sending
        console.log(obj);
        // send the data to the server, see the console for a logging message for success
        $.post("", obj, (data, status) => console.log("Status: " + status));
    });


    // send data to flask app
    "use strict";

    var fullHeight = function () {

        $('.js-fullheight').css('height', $(window).height());
        $(window).resize(function () {
            $('.js-fullheight').css('height', $(window).height());
        });

    };
    fullHeight();

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
    updateOverall(over);
    updateCoffee(cofe);
    updateWifi(wifi);
    updateOPower(power);


})(jQuery);



















