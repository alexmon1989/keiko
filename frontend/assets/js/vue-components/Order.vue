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
                    <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0"
                           name="radInline1_1"
                           type="radio"
                           value="self"
                           v-model="deliveryMode">
                    <div class="u-check-icon-radio-v4 g-absolute-centered--y g-left-0 g-width-18 g-height-18">
                        <i class="g-absolute-centered d-block g-width-10 g-height-10 g-bg-primary--checked"></i>
                    </div>
                    Самовывоз
                </label>

                <label class="form-check-inline u-check g-pl-25 ml-0 g-mr-25">
                    <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0"
                           name="radInline1_1"
                           type="radio"
                           value="courier"
                           v-model="deliveryMode">
                    <div class="u-check-icon-radio-v4 g-absolute-centered--y g-left-0 g-width-18 g-height-18">
                        <i class="g-absolute-centered d-block g-width-10 g-height-10 g-bg-primary--checked"></i>
                    </div>
                    Доставка курьером (+100 руб.)
                </label>
            </div>

            <h5 class="g-mb-20">Метод оплаты</h5>
            <div class="row g-mb-10">
                <!-- Left Column -->
                <div class="col-md-12">
                    <div class="form-group g-mb-10">
                        <label class="u-check g-pl-25">
                            <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0"
                                   name="radGroup2_1"
                                   type="radio"
                                   value="cash"
                                   v-model="payMode">
                            <div class="u-check-icon-radio-v4 g-absolute-centered--y g-left-0 g-width-18 g-height-18">
                                <i class="g-absolute-centered d-block g-width-10 g-height-10 g-bg-primary--checked"></i>
                            </div>
                            Оплата наличными при получении
                        </label>
                    </div>
                </div>
            </div>
            <!-- End Columned Radios -->

            <h5 class="g-mb-20">Личная информация</h5>
            <div class="g-mb-30 row">
                <div class="form-group g-mb-10 col-12" :class="{'u-has-error-v1': errors.first('username')}">
                    <label for="username">Имя *</label>
                    <input type="text"
                           class="form-control rounded-0 form-control-md"
                           id="username"
                           name="username"
                           v-model="username"
                           v-validate="'required'"
                           data-vv-as="Имя"
                           placeholder="Введите ваше имя">
                    <small class="form-control-feedback" v-if="errors.first('username')">{{ errors.first('username') }}</small>
                </div>
                <div class="form-group g-mb-10 col-6" :class="{'u-has-error-v1': errors.first('userphone')}">
                    <label for="userphone">Телефон *</label>
                    <input type="text"
                           class="form-control rounded-0 form-control-md"
                           id="userphone"
                           name="userphone"
                           v-model="userphone"
                           v-validate="'required|min:6'"
                           data-vv-as="Телефон"
                           placeholder="Введите ваш номер телефона">
                    <small class="form-control-feedback" v-if="errors.first('userphone')">{{ errors.first('userphone') }}</small>
                </div>

                <div class="form-group g-mb-10 col-6" :class="{'u-has-error-v1': errors.first('useremail')}">
                    <label for="useremail">E-Mail</label>
                    <input type="email"
                           class="form-control rounded-0 form-control-md"
                           name="useremail"
                           id="useremail"
                           v-model="useremail"
                           v-validate="'required|email'"
                           data-vv-as="E-Mail"
                           placeholder="Введите ваш E-Mail">
                    <small class="form-control-feedback" v-if="errors.first('useremail')">{{ errors.first('useremail') }}</small>
                </div>
            </div>

            <transition name="fade">
                <div v-if="deliveryMode==='courier'">
                    <h5 class="g-mb-20">Адрес доставки *</h5>
                    <div class="g-mb-30 row">
                        <div class="form-group g-mb-10 col-12" :class="{'u-has-error-v1': errors.first('useraddress')}">
                            <input type="text"
                                   class="form-control rounded-0 form-control-md"
                                   name="useraddress"
                                   id="useraddress"
                                   v-model="useraddress"
                                   v-validate="'required'"
                                   data-vv-as="Адрес доставки"
                                   placeholder="Введите ваш адрес">
                            <small class="form-control-feedback" v-if="errors.first('useraddress')">{{ errors.first('useraddress') }}</small>
                        </div>
                    </div>
                </div>
            </transition>

            <h5 class="g-mb-20">Комментарий к заказу</h5>
            <div class="g-mb-30 row">
                <div class="form-group g-mb-10 col-12">
                    <textarea class="form-control rounded-0 form-control-md"
                              rows="2"
                              v-model="usercomment"
                              placeholder="Ваш комментарий"></textarea>
                </div>
            </div>

            <div class="row g-mb-30" :class="{'u-has-error-v1': errors.first('personal_data')}">
                <div class="col-12">
                    <!-- Checkboxes Option 2 -->
                    <label class="form-check-inline u-check g-pl-25">
                        <input class="g-hidden-xs-up g-pos-abs g-top-0 g-left-0"
                               type="checkbox"
                               name="personal_data"
                               data-vv-as="Соглашение с условиями использования персональных данных"
                               v-validate="'required'">
                        <div class="u-check-icon-checkbox-v4 g-absolute-centered--y g-left-0">
                            <i class="fa" data-check-icon=""></i>
                        </div>
                        Я согласен с условиями использования&nbsp;<a href="#modal1" data-modal-target="#modal1" data-modal-effect="fadein">персональных данных</a>&nbsp;*
                    </label>
                    <!-- End Checkboxes Option 2 -->
                    <br>
                    <small class="form-control-feedback" v-if="errors.first('personal_data')">{{ errors.first('personal_data') }}</small>
                </div>
            </div>

            <div class="row">
                <div class="col-12">
                    <a href="#!"
                       :class="{'disabled': cart.length === 0}"
                       class="btn btn-md u-btn-lightred g-mr-10 g-mb-15 g-font-size-16"
                       @click.prevent="handleSubmit">Заказать</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import CartActions from './CartActions.vue';
    import EventBus from '../event-bus.js'

    export default {
        name: "Order",
        components: {
            CartActions
        },
        props: ["cart"],
        data() {
            return {
                deliveryMode: 'self',
                payMode: 'cash',
                username: '',
                userphone: '',
                useremail: '',
                useraddress: '',
                usercomment: '',
                terms: ''
            }
        },
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
                let delivery_cost = 0;
                if (this.deliveryMode === 'courier') {
                    delivery_cost = 100;
                }
                return this.total + delivery_cost;
            }
        },
        watch: {
            deliveryMode: function (val) {
                if (val === 'self') {
                    this.payMode = 'cash';
                }
            },
        },
        methods: {
            handleSubmit(e) {
                this.$validator.validate().then(valid => {
                    if (valid) {
                        axios.defaults.xsrfCookieName = 'csrftoken';
                        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
                        axios.post('/shop/create-order', {
                            deliveryMode: this.deliveryMode,
                            payMode: this.payMode,
                            username: this.username,
                            userphone: this.userphone,
                            useremail: this.useremail,
                            useraddress: this.useraddress,
                            usercomment: this.usercomment,
                            total: this.total,
                            orderSum: this.orderSum,
                            cart: this.cart
                        })
                            .then(response => {
                                EventBus.$emit('CLEAN-CART', location.href = '/shop/order-detail/' + response.data.unique_id);
                            })
                            .catch(e => {
                                this.errors.push(e);
                            })
                    }
                });
            }
        }
    }
</script>

<style scoped>
    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s;
    }

    .fade-enter, .fade-leave-to
    {
        opacity: 0;
    }
</style>