// Styles
import '../vendor/bootstrap/bootstrap.min.css';
import '../vendor/icon-awesome/scss/font-awesome.scss';
import '../vendor/hamburgers/hamburgers.min.css';
import '../include/scss/unify.scss'
import '../include/scss/custom.scss'

// Scripts
import '../vendor/jquery-migrate/jquery-migrate.min.js';
import '../vendor/bootstrap/bootstrap.min.js';

import './hs.core.js';
import './components/hs.header.js';
import './components/hs.scrollbar.js';
import './helpers/hs.hamburgers.js';
import './components/hs.tabs.js';

// JS Plugins Init
$(document).on('ready', function () {
    // initialization of tabs
    $.HSCore.components.HSTabs.init('[role="tablist"]');
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