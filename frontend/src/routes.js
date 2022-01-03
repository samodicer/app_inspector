import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home';
import Overview from './views/Overview';
import SignIn from './views/SignIn';
import CreateAccount from './views/CreateAccount';

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
    {
      path: '/sign-in',
      name: 'SignIn',
      component: SignIn,
    },
    {
      path: '/create-account',
      name: 'CreateAccount',
      component: CreateAccount,
    },
  ],
});
