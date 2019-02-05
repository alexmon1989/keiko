// Styles
import '../vendor/bootstrap/bootstrap.min.css';
import '../vendor/hamburgers/hamburgers.min.css';
import '../vendor/malihu-scrollbar/jquery.mCustomScrollbar.min.css';
import '../include/scss/unify.scss'
import '../include/scss/custom.scss'

// Scripts
import '../vendor/jquery-migrate/jquery-migrate.min.js';
import '../vendor/bootstrap/bootstrap.min.js';
import '../vendor/malihu-scrollbar/jquery.mCustomScrollbar.concat.min.js';

import './hs.core.js';
import './components/hs.header.js';
import './components/hs.scrollbar.js';
import './helpers/hs.hamburgers.js';
import './components/hs.tabs.js';

// JS Plugins Init
$(document).on('ready', function () {
    // initialization of tabs
    $.HSCore.components.HSTabs.init('[role="tablist"]');

    // initialization of HSScrollBar component
    $.HSCore.components.HSScrollBar.init($('.js-scrollbar'));
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