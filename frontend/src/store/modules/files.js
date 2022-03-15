import { getAPI } from '../../axios-api';

const state = {
  files: [],
  analyzedData: [],
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
  getAnalyzedData: (state) => state.analyzedData,
};

const actions = {
  async uploadFiles({ commit }, fd) {
    return new Promise((resolve, reject) => {
      getAPI
        .post('/upload-file/', fd, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then((response) => {
          commit('setUploadedFiles', response.data);
          resolve();
        })
        .catch((err) => {
          console.log(err);
          reject(err);
        });
    });
  },
  async analyzeFile({ commit }, { ids }) {
    return new Promise((resolve, reject) => {
      var query = '';
      for (let i = 0; i < ids.length; i++) {
        if (i == 0) query = query + '?';
        query = query + 'id=' + ids[i] + '&';
      }
      query = query.substring(0, query.length - 1);
      getAPI
        .get('/get-files-data' + query)
        .then((response) => {
          commit('setAnalyzedData', response.data);
          resolve();
        })
        .catch((err) => {
          console.log(err);
          reject(err);
        });
    });
  },
  async changeUploadedFiles({ commit }, array) {
    commit('setUploadedFiles', array);
  },
  async changeLoading({ commit }, value) {
    commit('setLoading', value);
  },
  async changeUploaded({ commit }, value) {
    commit('setUploaded', value);
  },
  async changeAnalysed({ commit }, value) {
    commit('setAnalysed', value);
  },
  async resetStates({ commit }) {
    commit('resetStates');
  },
};

const mutations = {
  resetStates: (state) => {
    state.files = [];
    state.analyzedData = [];
    state.uploadedFiles = [];
    state.isUploaded = false;
    state.isLoading = false;
    state.isAnalysed = false;
  },
  setLoading: (state, loading) => (state.isLoading = loading),
  setUploaded: (state, uploaded) => (state.isUploaded = uploaded),
  setAnalysed: (state, analysed) => (state.isAnalysed = analysed),
  setUploadedFiles: (state, array) => (state.uploadedFiles = array),
  setFiles: (state, files) => (state.files = files),
  setAnalyzedData: (state, analyzedData) => (state.analyzedData = analyzedData),
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
