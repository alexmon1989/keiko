<template>
    <div class="d-flex justify-content-between align-items-center w-100">
        <div><a href="#" @click.prevent='decrease'><i class="fa fa-minus"></i></a></div>
        <div class="g-font-size-18">{{ total }}</div>
        <div><a href="#" @click.prevent='increase'><i class="fa fa-plus"></i></a></div>
    </div>
</template>

<script>
    export default {
        name: "CartActions",
        props: ["product", "cart"],
        data: function () {
            return {cartItems: this.cart}
        },
        computed: {
            total() {
                let self = this;
                let res = this.cartItems.find(x => x.id === self.product.id);
                if (res) {
                    return res.count;
                }
                return 0;
            }
        },
        methods: {
            decrease() {
                let self = this;
                let res = this.cartItems.find(x => x.id === self.product.id);
                if (res) {
                    res.count--;
                    if (res.count === 0) {
                        let index = this.cartItems.indexOf(res);
                        if (index > -1) {
                          this.cartItems.splice(index, 1);
                        }
                    }
                }
            },
            increase() {
                let self = this;
                let res = this.cartItems.find(x => x.id === self.product.id);
                if (res) {
                    res.count++;
                } else {
                    this.cartItems.push(this.product);
                    this.cartItems[this.cartItems.length - 1].count = 1;
                }
            },
        }
    }
</script>

<style scoped>

</style>