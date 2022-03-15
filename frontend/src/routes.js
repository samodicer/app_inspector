import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home';
import Overview from './views/Overview';
import SignIn from './views/SignIn';
import CreateAccount from './views/CreateAccount';
import Account from './views/Account';

Vue.use(VueRouter);

// k cestám priradíme komponenty
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
      meta: {
        requiresLogout: true,
      },
    },
    {
      path: '/create-account',
      name: 'CreateAccount',
      component: CreateAccount,
      meta: {
        requiresLogout: true,
      },
    },
    {
      path: '/account',
      name: 'Account',
      component: Account,
      meta: {
        requiresLogin: true,
      },
    },
  ],
});
