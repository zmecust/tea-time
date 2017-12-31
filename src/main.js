import Vue from 'vue/dist/vue.js'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

window.onload = function() {
  new Vue({
    el: '#app',
    router,
    template: '<App/>',
    components: { App }
  })
}