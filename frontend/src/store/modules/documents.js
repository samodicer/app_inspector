import axios from 'axios';

const state = {
  files: [],
  analyzed_data: [],
};

const getters = {
  allFiles: (state) => state.files,
  getAnalyzedData: (state) => state.analyzed_data,
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
  async analyzeFile({ commit }, id) {
    axios
      .get('http://127.0.0.1:8000/get-file-data/' + id)
      .then((response) => {
        commit('setAnalyzedData', response.data);
        console.log(response);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};

const mutations = {
  setFiles: (state, files) => (state.files = files),
  setAnalyzedData: (state, analyzed_data) =>
    (state.analyzed_data = analyzed_data),
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
