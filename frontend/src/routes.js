import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home';
import Overview from './views/Overview';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/overview',
      name: 'Overview',
      component: Overview,
    },
  ],
});
