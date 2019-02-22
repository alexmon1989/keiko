// Шаблон
import './template.js';
import Vue from 'vue';

import VeeValidate from 'vee-validate';

Vue.use(VeeValidate);

window.$ = window.jQuery = require('jquery');

import Cart from './vue-components/Cart.vue';
import CartActions from './vue-components/CartActions.vue';
import Order from './vue-components/Order.vue';
import EventBus from './event-bus.js'

new Vue({
    el: '#app',
    components: {
        Cart,
        CartActions,
        Order
    },
    data: {
        cart: []
    },
    mounted() {
        if (localStorage.getItem('cart')) {
            try {
                this.cart = JSON.parse(localStorage.getItem('cart'));
            } catch (e) {
                localStorage.removeItem('cart');
            }
        }

        EventBus.$on('DECREASE-CART-ITEM', product => {
            let res = this.cart.find(x => x.id === product.id);
            if (res) {
                res.count--;
                if (res.count === 0) {
                    let index = this.cart.indexOf(res);
                    if (index > -1) {
                      this.cart.splice(index, 1);
                    }
                }
            }
            this.saveCart();
            this.$nextTick(function () {
                $.HSCore.components.HSScrollBar.destroy($('.js-scrollbar'));
                $.HSCore.components.HSScrollBar.init($('.js-scrollbar'));
            })
        });

        EventBus.$on('INCREASE-CART-ITEM', product => {
            let res = this.cart.find(x => x.id === product.id);
            if (res) {
                res.count++;
            } else {
                product.count = 1;
                this.cart.push(product);
            }
            this.saveCart();
            this.$nextTick(function () {
                $.HSCore.components.HSScrollBar.destroy($('.js-scrollbar'));
                $.HSCore.components.HSScrollBar.init($('.js-scrollbar'));
            })
        });

        EventBus.$on('REMOVE-CART-ITEM', item => {
            this.cart.splice(this.cart.indexOf(item), 1);
            this.saveCart();
            this.$nextTick(function () {
                $.HSCore.components.HSScrollBar.destroy($('.js-scrollbar'));
                $.HSCore.components.HSScrollBar.init($('.js-scrollbar'));
            })
        });
    },

    methods: {
        saveCart() {
          const parsed = JSON.stringify(this.cart);
          localStorage.setItem('cart', parsed);
        }
    }
});
