import { getAPI } from '../../axios-api';

const state = {
  files: [],
  analysedData: [],
  uploadedFiles: [],
  isLoading: false,
  isUploaded: false,
  isAnalysed: false,
};

const getters = {
  getLoading: (state) => state.isLoading,
  getUploadedFiles: (state) => state.uploadedFiles,
  getUploaded: (state) => state.isUploaded,
  getAnalysed: (state) => state.isAnalysed,
  getAnalysedData: (state) => state.analysedData,
};

const actions = {
  // nahratie súborov
  async uploadFiles({ commit }, fd) {
    return new Promise((resolve, reject) => {
      // POST požiadavka na koncový bod
      getAPI
        .post('/upload-file/', fd, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then((response) => {
          // keď príde odpoveď zavolá sa mutácia, ktorá zmení nahraté súbory
          commit('setUploadedFiles', response.data);
          resolve();
        })
        .catch((err) => {
          // keď príde chyba
          console.log(err);
          reject(err);
        });
    });
  },
  // analýza súborov
  async analyseFile({ commit }, { ids }) {
    return new Promise((resolve, reject) => {
      // vyskladáme id parametre
      var query = '';
      for (let i = 0; i < ids.length; i++) {
        if (i == 0) query = query + '?';
        query = query + 'id=' + ids[i] + '&';
      }
      query = query.substring(0, query.length - 1);
      // GET požiadavka na koncový bod
      getAPI
        .get('/get-files-data' + query)
        .then((response) => {
          // keď príde odooveď zavolá sa mutácia
          commit('setAnalysedData', response.data);
          resolve();
        })
        .catch((err) => {
          // keď príde chyba
          console.log(err);
          reject(err);
        });
    });
  },
  // zavolá mutáciu na zmenu nahratých súborov
  async changeUploadedFiles({ commit }, array) {
    commit('setUploadedFiles', array);
  },
  // zavolá mutáciu na zmenu stavu isLoading
  async changeLoading({ commit }, value) {
    commit('setLoading', value);
  },
  // zavolá mutáciu na zmenu stavu isUploaded
  async changeUploaded({ commit }, value) {
    commit('setUploaded', value);
  },
  // zavolá mutáciu na zmenu stavu isAnalysed
  async changeAnalysed({ commit }, value) {
    commit('setAnalysed', value);
  },
  // zavolá mutáciu na resetovanie stavov
  async resetStates({ commit }) {
    commit('resetStates');
  },
};

const mutations = {
  resetStates: (state) => {
    // resetovanie stavov
    state.files = [];
    state.analysedData = [];
    state.uploadedFiles = [];
    state.isUploaded = false;
    state.isLoading = false;
    state.isAnalysed = false;
  },
  setLoading: (state, loading) => (state.isLoading = loading), // zmena stavu isLoading
  setUploaded: (state, uploaded) => (state.isUploaded = uploaded), // zmena stavu isUploaded
  setAnalysed: (state, analysed) => (state.isAnalysed = analysed), // zmena stavu isAnalysed
  setUploadedFiles: (state, array) => (state.uploadedFiles = array), // zmena nahratých súborov
  setAnalysedData: (state, analysedData) => (state.analysedData = analysedData), // zmena analyzovaných dát
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
