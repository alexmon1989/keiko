<template>
    <div class="d-flex justify-content-between align-items-center w-100">
        <div><a href="#" @click.prevent='decrease'><i class="fa fa-minus"></i></a></div>
        <div class="g-font-size-18">{{ total }}</div>
        <div><a href="#" @click.prevent='increase'><i class="fa fa-plus"></i></a></div>
    </div>
</template>

<script>
    import EventBus from '../event-bus.js'

    export default {
        name: "CartActions",
        props: ["product", "cart"],
        computed: {
            total() {
                let self = this;
                let res = this.cart.find(x => x.id === self.product.id);
                if (res) {
                    return res.count;
                }
                return 0;
            }
        },
        methods: {
            decrease() {
                EventBus.$emit('DECREASE-CART-ITEM', this.product);
            },
            increase() {
                EventBus.$emit('INCREASE-CART-ITEM', this.product);
            },
        }
    }
</script>

<style scoped>

</style>