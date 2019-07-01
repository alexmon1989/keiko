// Styles
import '../vendor/bootstrap/bootstrap.min.css';
import '../vendor/icon-awesome/scss/font-awesome.scss';
import '../vendor/hamburgers/hamburgers.min.css';
import '../vendor/animate.css';
import '../vendor/fancybox/jquery.fancybox.min.css';
import '../vendor/slick-carousel/slick/slick.css';
import '../vendor/malihu-scrollbar/jquery.mCustomScrollbar.min.css';
import '../vendor/animate.css';
import '../vendor/custombox/custombox.min.css';
import '../include/scss/unify.scss'
import '../include/scss/custom.scss'

// Scripts
import '../vendor/jquery-migrate/jquery-migrate.min.js';
import '../vendor/bootstrap/bootstrap.min.js';
import '../vendor/fancybox/jquery.fancybox.min.js';
import '../vendor/slick-carousel/slick/slick.js';
import '../vendor/malihu-scrollbar/jquery.mCustomScrollbar.concat.min.js';
import '../vendor/custombox/custombox.min.js';

import './hs.core.js';
import './components/hs.header.js';
import './components/hs.dropdown.js';
import './components/hs.scrollbar.js';
import './helpers/hs.hamburgers.js';
import './components/hs.tabs.js';
import './components/hs.popup.js';
import './components/hs.carousel.js';
import './components/hs.modal-window.js';

// JS Plugins Init
$(document).on('ready', function () {
    // initialization of popups
    $.HSCore.components.HSPopup.init('.js-fancybox');

    // initialization of carousel
    $.HSCore.components.HSCarousel.init('.js-carousel');

    // initialization of HSScrollBar component
    $.HSCore.components.HSScrollBar.init( $('.js-scrollbar') );

    // initialization of tabs
    $.HSCore.components.HSTabs.init('[role="tablist"]');

    // initialization of HSDropdown component
    $.HSCore.components.HSDropdown.init($('[data-dropdown-target]'));

    // initialization of popups
    $.HSCore.components.HSModalWindow.init('[data-modal-target]');
});

$(window).on('resize', function () {
    setTimeout(function () {
        $.HSCore.components.HSTabs.init('[role="tablist"]');
    }, 200);
});

$(window).on('load', function () {
    // initialization of header
    $.HSCore.components.HSHeader.init($('#js-header'));
    $.HSCore.helpers.HSHamburgers.init('.hamburger');
});