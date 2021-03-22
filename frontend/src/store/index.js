import Vuex from 'vuex';
import Vue from 'vue';
import documents from './modules/documents';

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        documents
    }
});