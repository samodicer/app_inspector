import axios from 'axios';

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
  allFiles: (state) => state.files,
  getAnalyzedData: (state) => state.analyzedData,
};

const actions = {
  /*async uploadFile(){
        /*const fd = new FormData();
        fd.append('title',data.title);
        fd.append('file',data.file);
        console.log("data:"+data.file);
        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/documents/',
            data: fd,
            body: fd
        })
    },*/
  async resetStates({ commit }) {
    commit('resetStates');
  },
  async fetchFiles({ commit }) {
    axios
      .get('http://127.0.0.1:8000/get-files/')
      .then((response) => {
        commit('setFiles', response.data);
        console.log(response);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  async analyzeFile({ commit }, ids) {
    console.log(ids);
    var URL = 'http://127.0.0.1:8000/get-files-data';
    for (let i = 0; i < ids.length; i++) {
      if (i == 0) URL = URL + '?';
      URL = URL + 'id=' + ids[i] + '&';
    }
    URL = URL.substring(0, URL.length - 1);

    axios({
      method: 'get',
      url: URL,
    })
      .then((response) => {
        //commit('setAnalyzedData', response.data);
        console.log(response);
        commit('setAnalyzedData', response.data);
      })
      .catch((err) => {
        console.log(err);
      });
    commit('setAnalyzedData', '');
    /*for (var id in ids) {
      console.log(id);
    }*/
    /*
    axios
      .get('http://127.0.0.1:8000/get-files-data/' + ids)
      .then((response) => {
        commit('setAnalyzedData', response.data);
        console.log(response);
      })
      .catch((err) => {
        console.log(err);
      });*/
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
  async changeUploadedFiles({ commit }, array) {
    commit('setUploadedFiles', array);
  },
};

const mutations = {
  resetStates: (state) => {
    state.files = [];
    state.analyzedData = [];
    state.uploadedFiles = [];
    state.isUploaded = false;
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
