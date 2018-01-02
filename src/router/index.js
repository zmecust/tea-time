import Vue from 'vue/dist/vue.js'
import Router from 'vue-router'
import Main from '../view/Main.vue';
import DigitRecognition from '../view/DigitRecognition.vue';

Vue.use(Router)

const router = new Router({
  // mode: 'history',
  routes: [
    {
      path: '/',
      component: Main
    },
    {
      path: '/digit_recognition',
      component: DigitRecognition
    }
  ]
})

export default router;
