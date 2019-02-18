// Шаблон
import './template.js';
import Vue from 'vue';

import VeeValidate from 'vee-validate';

Vue.use(VeeValidate);

window.$ = window.jQuery = require('jquery');

import Cart from './vue-components/Cart.vue';
import CartActions from './vue-components/CartActions.vue';

new Vue({
    el: '#app',
    components: {
        Cart,
        CartActions
    },
    data: {
        cart: [
            {
                'id': 1,
                'title': 'Title',
                'link': 'link',
                'img': '/static/img-temp/150x150/img1.jpg',
                'price': 1000,
                'count': 2,
            },
            {
                'id': 251,
                'title': 'Title 2',
                'link': 'link2',
                'img': '/static/img-temp/150x150/img1.jpg',
                'price': 2000,
                'count': 3,
            }
        ]
    },
    mounted() {
        if (localStorage.getItem('cart')) {
            try {
                this.cart = JSON.parse(localStorage.getItem('cart'));
            } catch (e) {
                localStorage.removeItem('cart');
            }
        }
    }
});
