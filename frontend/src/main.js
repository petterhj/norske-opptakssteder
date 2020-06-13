import Vue from 'vue'
import VueRouter from 'vue-router'
import VueChimera from 'vue-chimera'

import App from './App.vue'
import Home from './components/views/Home.vue'
import Productions from './components/views/Productions.vue'
import Production from './components/views/Production.vue'
import ErrorPage from './components/views/ErrorPage.vue'

Vue.config.productionTip = false

Vue.use(VueRouter);
Vue.use(VueChimera, {
  baseURL: 'http://localhost:5000/',
  // prefetch: true,
});

const router = new VueRouter({
  mode: 'history',
  routes: [
    { name: 'home', path: '/', component: Home },
    
    { name: 'productions', path: '/produksjoner', component: Productions },
    { name: 'production', path: '/produksjoner/film/:slug', component: Production },

    { name: 'error', path: '*', component: ErrorPage, props: { status_code: 404 } },
  ]
})

new Vue({
  el: '#app',
  // store,
  router,
  render: h => h(App)
})