<template>
    <div class="u-basket d-inline-block g-valign-middle g-pt-6 g-ml-30 g-ml-0--lg g-pos-abs g-top-15 g-right-65 g-pos-rel--lg g-top-0--lg g-right-0--lg">
        <a href="/shop/cart/"
           rel="nofollow"
           id="basket-bar-invoker"
           class="u-icon-v1 g-color-white-opacity-0_8 g-color-white--hover g-text-underline--none--hover g-width-20 g-height-20"
           aria-controls="basket-bar"
           aria-haspopup="true"
           aria-expanded="false"
           data-dropdown-event="hover"
           data-dropdown-target="#basket-bar"
           data-dropdown-type="css-animation"
           data-dropdown-duration="500"
           data-dropdown-hide-on-scroll="false"
           data-dropdown-animation-in="fadeIn"
           data-dropdown-animation-out="fadeOut">
            <span class="u-badge-v1--sm g-color-white g-bg-primary g-rounded-50x">{{ countProducts }}</span>
            <i class="fa fa-shopping-cart"></i>
        </a>

        <div id="basket-bar"
             v-show="cart.length > 0"
             class="u-basket__bar u-dropdown--css-animation u-dropdown--hidden g-brd-top g-brd-2 g-brd-primary g-color-white-opacity-0_8 g-mt-15--lg g-mt-15--lg--scrolling g-bg-gray-dark-v1"
             aria-labelledby="basket-bar-invoker">
            <div class="js-scrollbar g-height-280">

                <!-- Product -->
                <div class="u-basket__product g-brd-white-opacity-0_5" v-for="(item) in cart">
                    <div class="row align-items-center no-gutters">
                        <div class="col-4 g-pr-20">
                            <a :href="item.link" class="u-basket__product-img">
                                <img :src="item.img" :alt="item.title">
                            </a>
                        </div>

                        <div class="col-8">
                            <h6 class="g-font-weight-600 g-mb-0">
                                <a :href="item.link"
                                   class="g-color-white g-color-white-opacity-0_5--hover g-text-underline--none--hover">{{ item.title }}</a>
                            </h6>
                            <small class="g-color-gray-dark-v5 g-font-size-14">{{ item.count }} x {{ item.price }} <i
                                    class="fa fa-rub"></i></small>
                        </div>
                    </div>
                    <button class="u-basket__product-remove g-color-white-opacity-0_9" type="button" @click="remove(item)">&times;</button>
                </div>
                <!-- End Product -->
            </div>

            <div class="g-brd-top g-brd-white-opacity-0_5 g-pa-15 g-pb-20">
                <div class="d-flex flex-row align-items-center justify-content-between g-letter-spacing-1 g-font-size-16 g-mb-15">
                    <strong class="text-uppercase g-font-weight-600">Общая сумма</strong>
                    <strong class="g-color-primary g-font-weight-600">{{ total }} <i class="fa fa-rub"></i></strong>
                </div>

                <div class="d-flex align-items-center justify-content-center g-font-size-18">
                    <a href="/shop/cart/" class="btn btn-md u-btn-outline-primary">Перейти в корзину</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import EventBus from '../event-bus.js'

    export default {
        name: "Cart",
        props: ["cart"],
        computed: {
            total() {
                return this.cart.reduce((total, i) => {
                    return total + i.price * i.count
                }, 0)
            },
            countProducts() {
                return this.cart.reduce((total, i) => {
                    return total + i.count
                }, 0)
            }
        },
        methods: {
            remove(item) {
                EventBus.$emit('REMOVE-CART-ITEM', item);
            }
        }
    }
</script>

<style scoped>

</style>