<template>
    <div class="row">
        <div class="col-md-6">
            <h5 class="g-mb-20">Мой заказ</h5>

            <table class="table table-striped">
                <tr v-for="product in cart">
                    <td><a :href="product.link">{{ product.title }}</a></td>
                    <td>
                        <cart-actions :product="product" :cart="cart"/>
                    </td>
                    <td class="text-right">{{ product.count }} x {{ product.price }} <i class="fa fa-rub"></i></td>
                </tr>
                <tr class="g-color-white-opacity-0_8 g-font-size-16">
                    <td class="g-pt-30" colspan="2">Сумма заказа</td>
                    <td class="g-pt-30 text-right">{{ total }} <i class="fa fa-rub"></i></td>
                </tr>
            </table>

            <div class="row g-font-size-18 g-px-10 g-mb-30">
                <div class="col-6 g-font-weight-600">К оплате:</div>
                <div class="col-6 text-right">{{ orderSum }} <i class="fa fa-rub"></i></div>
            </div>

        </div>
        <div class="col-md-6">
            <h5 class="g-mb-20">Метод доставки</h5>
            <div class="g-mb-15">
                <label class="form-check-inline u-check g-pl-25 ml-0 g-mr-25">
                    <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0" name="radInline1_1" type="radio"
                           checked="">
                    <div class="u-check-icon-radio-v4 g-absolute-centered--y g-left-0 g-width-18 g-height-18">
                        <i class="g-absolute-centered d-block g-width-10 g-height-10 g-bg-primary--checked"></i>
                    </div>
                    Доставка курьером (+100 руб.)
                </label>

                <label class="form-check-inline u-check g-pl-25 ml-0 g-mr-25">
                    <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0" name="radInline1_1" type="radio">
                    <div class="u-check-icon-radio-v4 g-absolute-centered--y g-left-0 g-width-18 g-height-18">
                        <i class="g-absolute-centered d-block g-width-10 g-height-10 g-bg-primary--checked"></i>
                    </div>
                    Самовывоз
                </label>
            </div>

            <h5 class="g-mb-20">Метод оплаты</h5>
            <div class="row g-mb-10">
                <!-- Left Column -->
                <div class="col-md-12">
                    <div class="form-group g-mb-10">
                        <label class="u-check g-pl-25">
                            <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0" name="radGroup2_1" type="radio"
                                   checked="">
                            <div class="u-check-icon-radio-v4 g-absolute-centered--y g-left-0 g-width-18 g-height-18">
                                <i class="g-absolute-centered d-block g-width-10 g-height-10 g-bg-primary--checked"></i>
                            </div>
                            Оплата через Яндекс кошелёк
                        </label>
                    </div>

                    <div class="form-group g-mb-10">
                        <label class="u-check g-pl-25">
                            <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0" name="radGroup2_1" type="radio">
                            <div class="u-check-icon-radio-v4 g-absolute-centered--y g-left-0 g-width-18 g-height-18">
                                <i class="g-absolute-centered d-block g-width-10 g-height-10 g-bg-primary--checked"></i>
                            </div>
                            Оплата банковской картой
                        </label>
                    </div>

                    <div class="form-group">
                        <label class="u-check g-pl-25">
                            <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0" name="radGroup2_1" type="radio">
                            <div class="u-check-icon-radio-v4 g-absolute-centered--y g-left-0 g-width-18 g-height-18">
                                <i class="g-absolute-centered d-block g-width-10 g-height-10 g-bg-primary--checked"></i>
                            </div>
                            Оплата наличными при получении
                        </label>
                    </div>
                </div>
                <!-- End Left Column -->
            </div>
            <!-- End Columned Radios -->

            <h5 class="g-mb-20">Личная информация</h5>
            <div class="g-mb-30 row">
                <div class="form-group g-mb-10 col-12">
                    <label for="username">Имя *</label>
                    <input type="email" class="form-control rounded-0 form-control-md" id="username"
                           aria-describedby="emailHelp" placeholder="Введите ваше имя">
                </div>
                <div class="form-group g-mb-10 col-6">
                    <label for="userphone">Телефон *</label>
                    <input type="email" class="form-control rounded-0 form-control-md" id="userphone"
                           aria-describedby="emailHelp" placeholder="Введите ваш номер телефона">
                </div>

                <div class="form-group g-mb-10 col-6">
                    <label for="useremail">E-Mail</label>
                    <input type="email" class="form-control rounded-0 form-control-md" id="useremail"
                           aria-describedby="emailHelp" placeholder="Введите ваш E-Mail">
                </div>
            </div>

            <h5 class="g-mb-20">Адрес доставки *</h5>
            <div class="g-mb-30 row">
                <div class="form-group g-mb-10 col-12">
                    <input type="email" class="form-control rounded-0 form-control-md" id="address"
                           aria-describedby="emailHelp" placeholder="Введите ваш адрес">
                </div>
            </div>

            <h5 class="g-mb-20">Комментарий к заказу</h5>
            <div class="g-mb-30 row">
                <div class="form-group g-mb-10 col-12">
                    <textarea class="form-control rounded-0 form-control-md" rows="2"></textarea>
                </div>
            </div>

            <!-- Checkboxes Option 2 -->
            <label class="form-check-inline u-check g-pl-25 g-mb-30">
                <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0" type="checkbox">
                <div class="u-check-icon-checkbox-v4 g-absolute-centered--y g-left-0">
                    <i class="fa" data-check-icon=""></i>
                </div>
                Я согласен с условиями использования&nbsp;<a href="#">персональных данных</a>&nbsp;*
            </label>
            <!-- End Checkboxes Option 2 -->

            <div class="row">
                <div class="col-12">
                   <a href="#!" class="btn btn-md u-btn-lightred g-mr-10 g-mb-15 g-font-size-16">Заказать</a>
                </div>
            </div>

        </div>

    </div>
</template>

<script>
    import CartActions from './CartActions.vue';

    export default {
        name: "Order",
        components: {
            CartActions
        },
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
            },
            orderSum() {
                return this.total + 200;
            }
        },
    }
</script>

<style scoped>

</style>