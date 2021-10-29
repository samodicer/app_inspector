import Vuex from 'vuex';
import Vue from 'vue';
import files from './modules/files';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    files,
  },
});
