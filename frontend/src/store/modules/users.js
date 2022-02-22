import { getAPI } from '../../axios-api';

const state = {
  accessToken: null,
  refreshToken: null,
  currentUser: {
    id: '',
    username: '',
    first_name: '',
    last_name: '',
  },
};

const getters = {
  getUser: (state) => state.currentUser,
};

const actions = {
  async refreshAccessToken({ commit }) {
    var refreshToken = localStorage.getItem('refreshToken');
    localStorage.removeItem('accessToken');
    return new Promise((resolve, reject) => {
      getAPI
        .post('/api-token-refresh/', {
          refresh: refreshToken,
        })
        .then((response) => {
          commit('updateStorage', {
            access: response.data.access,
            refresh: refreshToken,
          });
          resolve();
        })
        .catch((err) => {
          reject(err);
        });
    });
  },
  async userLogin({ commit }, user) {
    localStorage.removeItem('accessToken');
    return new Promise((resolve, reject) => {
      getAPI
        .post('/api-token/', {
          username: user.username,
          password: user.password,
        })
        .then((response) => {
          commit('updateStorage', {
            access: response.data.access,
            refresh: response.data.refresh,
          });
          resolve();
        })
        .catch((err) => {
          reject(err);
        });
    });
  },
  async userLogout({ commit }) {
    if (localStorage.getItem('accessToken')) {
      commit('destroyToken');
      commit('removeCurrentUser');
    }
  },
  async userCreateAccount({ commit }, user) {
    const formData = new FormData();
    formData.append('username', user.username);
    formData.append('password', user.password);
    formData.append('password2', user.confirm_password);
    formData.append('first_name', user.first_name);
    formData.append('last_name', user.last_name);
    console.log('formdata:' + formData['username']);
    commit('destroyToken');
    return new Promise((resolve, reject) => {
      getAPI
        .post('/register/', {
          username: user.username,
          password: user.password,
          password2: user.confirm_password,
          first_name: user.first_name,
          last_name: user.last_name,
          /*formData,*/
        })
        .then((response) => {
          console.log(response);

          resolve();
        })
        .catch((err) => {
          reject(err);
        });
    });
  },
  async getCurrentUser({ commit, dispatch }, token) {
    dispatch('refreshAccessToken');
    return new Promise((resolve, reject) => {
      getAPI
        .get('/get-user/?access_token=' + token)
        .then((response) => {
          console.log(response);
          commit('setCurrentUser', response.data);
          resolve();
        })
        .catch((err) => {
          reject(err);
        });
    });
  },
};

const mutations = {
  updateStorage(state, { access, refresh }) {
    state.accessToken = access;
    state.refreshToken = refresh;
    localStorage.setItem('accessToken', access);
    localStorage.setItem('refreshToken', refresh);
  },
  destroyToken(state) {
    state.accessToken = null;
    state.refreshToken = null;
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
  },
  setCurrentUser: (state, user) => {
    state.currentUser.id = user.id;
    state.currentUser.username = user.username;
    state.currentUser.first_name = user.first_name;
    state.currentUser.last_name = user.last_name;
  },
  removeCurrentUser: (state) => {
    state.currentUser.id = '';
    state.currentUser.username = '';
    state.currentUser.first_name = '';
    state.currentUser.last_name = '';
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
