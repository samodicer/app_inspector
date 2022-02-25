import Vue from 'vue';
import App from './App.vue';
import router from './routes.js';
import store from './store';
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresLogin)) {
    if (localStorage.getItem('accessToken') == null) {
      next({ name: 'SignIn' });
    } else {
      next();
    }
  } else if (to.matched.some((record) => record.meta.requiresLogout)) {
    if (localStorage.getItem('accessToken') != null) {
      next({ name: 'Home' });
    } else {
      next();
    }
  } else {
    next();
  }
});

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
