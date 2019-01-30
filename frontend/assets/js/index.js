// Шаблон
import './template.js';
import Vue from 'vue';

import VeeValidate from 'vee-validate';
Vue.use(VeeValidate);

window.$ = window.jQuery = require('jquery');

const app = new Vue({
    el: '#app'
});