import Vuex from 'vuex';
import Vue from 'vue';
import files from './modules/files';
import users from './modules/users';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    files,
    users,
  },
});
