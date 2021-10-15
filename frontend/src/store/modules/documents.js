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
