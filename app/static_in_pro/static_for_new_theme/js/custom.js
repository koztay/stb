/**
 * Template Name: Daily Shop
 * Version: 1.0
 * Template Scripts
 * Author: MarkUps
 * Author URI: http://www.markups.io/

 Custom JS


 1. CARTBOX
 2. TOOLTIP
 3. PRODUCT VIEW SLIDER
 4. POPULAR PRODUCT SLIDER (SLICK SLIDER)
 5. FEATURED PRODUCT SLIDER (SLICK SLIDER)
 6. LATEST PRODUCT SLIDER (SLICK SLIDER)
 7. TESTIMONIAL SLIDER (SLICK SLIDER)
 8. CLIENT BRAND SLIDER (SLICK SLIDER)
 9. PRICE SLIDER  (noUiSlider SLIDER)
 10. SCROLL TOP BUTTON
 11. PRELOADER
 12. GRID AND LIST LAYOUT CHANGER
 13. RELATED ITEM SLIDER (SLICK SLIDER)


 **/

jQuery(function ($) {


    /* ----------------------------------------------------------- */
    /*  1. CARTBOX 
     /* ----------------------------------------------------------- */

    jQuery(".aa-cartbox").hover(function () {
            jQuery(this).find(".aa-cartbox-summary").fadeIn(500);
        }
        , function () {
            jQuery(this).find(".aa-cartbox-summary").fadeOut(500);
        }
    );

    /* ----------------------------------------------------------- */
    /*  2. TOOLTIP
     /* ----------------------------------------------------------- */
    jQuery('[data-toggle="tooltip"]').tooltip();
    jQuery('[data-toggle2="tooltip"]').tooltip();

    /* ----------------------------------------------------------- */
    /*  3. PRODUCT VIEW SLIDER 
     /* ----------------------------------------------------------- */

    jQuery('#demo-1 .simpleLens-thumbnails-container img').simpleGallery({
        loading_image: 'demo/images/loading.gif'
    });

    jQuery('#demo-1 .simpleLens-big-image').simpleLens({
        loading_image: 'demo/images/loading.gif'
    });

    /* ----------------------------------------------------------- */
    /*  4. POPULAR PRODUCT SLIDER (SLICK SLIDER)
     /* ----------------------------------------------------------- */

    jQuery('.aa-popular-slider').slick({
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 4,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });


    /* ----------------------------------------------------------- */
    /*  5. FEATURED PRODUCT SLIDER (SLICK SLIDER)
     /* ----------------------------------------------------------- */

    jQuery('.aa-featured-slider').slick({
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 4,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

    /* ----------------------------------------------------------- */
    /*  6. LATEST PRODUCT SLIDER (SLICK SLIDER)
     /* ----------------------------------------------------------- */
    jQuery('.aa-latest-slider').slick({
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 4,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

    /* ----------------------------------------------------------- */
    /*  7. TESTIMONIAL SLIDER (SLICK SLIDER)
     /* ----------------------------------------------------------- */

    jQuery('.aa-testimonial-slider').slick({
        dots: true,
        infinite: true,
        arrows: false,
        speed: 300,
        slidesToShow: 1,
        adaptiveHeight: true
    });

    /* ----------------------------------------------------------- */
    /*  8. CLIENT BRAND SLIDER (SLICK SLIDER)
     /* ----------------------------------------------------------- */

    jQuery('.aa-client-brand-slider').slick({
        dots: false,
        infinite: false,
        speed: 300,
        autoplay: true,
        autoplaySpeed: 2000,
        slidesToShow: 5,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 4,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

    /* ----------------------------------------------------------- */
    /*  9. PRICE SLIDER  (noUiSlider SLIDER)
     /* ----------------------------------------------------------- */
    /*
    * Aşağıdaki kodu düzenledim min max değerleri almasını sağladım...
    */
    jQuery(function () {
        if ($('body').is('.productPage')) {
            var skipSlider = document.getElementById('skipstep');
            var min_range = document.getElementById('minrange').value;
            var max_range = document.getElementById('maxrange').value;
            var min_set_value = document.getElementById('minsetvalue').value;
            var max_set_value = document.getElementById('maxsetvalue').value;
            console.log(min_range);
            console.log(max_range);
            console.log(min_set_value);
            console.log(max_set_value);
            var start_value_min = 0;
            var start_value_max = 100;
            if (min_set_value>0) {
                start_value_min = parseInt(min_set_value);
            }else {
                start_value_min = 0;
            }
            if (max_set_value>0) {
                start_value_max = parseInt(max_set_value);
            }else {
                start_value_max = parseInt(max_range);
            }
            console.log(start_value_min);
            console.log(start_value_max);

            // noUiSlider.create(skipSlider, {
            //     range: {
            //         'min': 0,
            //         'max': parseInt(max_range)
            //     },
            //     step: 10,
            //     snap: true,
            //     connect: true,
            //     start: [start_value_min, start_value_max]
            // });

            noUiSlider.create(skipSlider, {
                start: [ start_value_min, start_value_max ],
                step: 10,
                range: {
                  'min': 0,
                  'max': parseInt(max_range)
                }
            });

            // for value print
            var skipValues = [
                document.getElementById('skip-value-lower'),
                document.getElementById('skip-value-upper')
            ];

            skipSlider.noUiSlider.on('update', function (values, handle) {
                skipValues[handle].innerHTML = values[handle];
            });
        }
    });


    /* ----------------------------------------------------------- */
    /*  10. SCROLL TOP BUTTON
     /* ----------------------------------------------------------- */

    //Check to see if the window is top if not then display button

    jQuery(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.scrollToTop').fadeIn();
        } else {
            $('.scrollToTop').fadeOut();
        }
    });

    //Click event to scroll to top

    jQuery('.scrollToTop').click(function () {
        $('html, body').animate({scrollTop: 0}, 800);
        return false;
    });

    /* ----------------------------------------------------------- */
    /*  11. PRELOADER
     /* ----------------------------------------------------------- */

    jQuery(window).load(function () { // makes sure the whole site is loaded      
        jQuery('#wpf-loader-two').delay(200).fadeOut('slow'); // will fade out      
    })

    /* ----------------------------------------------------------- */
    /*  12. GRID AND LIST LAYOUT CHANGER 
     /* ----------------------------------------------------------- */

    jQuery("#list-catg").click(function (e) {
        e.preventDefault(e);
        jQuery(".aa-product-catg").addClass("list");
    });
    jQuery("#grid-catg").click(function (e) {
        e.preventDefault(e);
        jQuery(".aa-product-catg").removeClass("list");
    });


    /* ----------------------------------------------------------- */
    /*  13. RELATED ITEM SLIDER (SLICK SLIDER)
     /* ----------------------------------------------------------- */

    jQuery('.aa-related-item-slider').slick({
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 4,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

});

