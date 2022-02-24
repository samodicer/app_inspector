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
  loginErrorMessage: '',
  registerErrorMessages: {
    username: [],
    first_name: [],
    last_name: [],
    password: [],
  },
};

const getters = {
  getUser: (state) => state.currentUser,
  getLoginErrorMessage: (state) => state.loginErrorMessage,
  getRegisterErrorMessages: (state) => state.registerErrorMessages,
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
          if (err.response) {
            commit('setLoginErrorMessage', err.response.data.detail);
          }
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
    commit('destroyToken');
    return new Promise((resolve, reject) => {
      getAPI
        .post('/register/', {
          username: user.username,
          password: user.password,
          password2: user.confirm_password,
          first_name: user.first_name,
          last_name: user.last_name,
        })
        .then(() => {
          resolve();
        })
        .catch((err) => {
          if (err.response) {
            commit('setRegisterErrorMessages', err.response.data);
          }
          reject(err);
        });
    });
  },
  async getCurrentUser({ commit, dispatch }, token) {
    if (localStorage.getItem('accessToken') != null) {
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
    }
  },
  async refreshMessages({ commit }) {
    commit('removeMessages');
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
  setLoginErrorMessage: (state, message) => {
    state.loginErrorMessage = message;
  },
  setRegisterErrorMessages: (state, messages) => {
    state.registerErrorMessages.username = [];
    state.registerErrorMessages.first_name = [];
    state.registerErrorMessages.last_name = [];
    state.registerErrorMessages.password = [];
    if (messages.username != null) {
      messages.username.forEach((username_error) => {
        state.registerErrorMessages.username.push(username_error);
      });
    }
    if (messages.first_name != null) {
      messages.first_name.forEach((first_name_error) => {
        state.registerErrorMessages.first_name.push(first_name_error);
      });
    }
    if (messages.last_name != null) {
      messages.last_name.forEach((last_name_error) => {
        state.registerErrorMessages.last_name.push(last_name_error);
      });
    }
    if (messages.password != null) {
      messages.password.forEach((password_error) => {
        state.registerErrorMessages.password.push(password_error);
      });
    }
  },
  removeMessages: (state) => {
    state.loginErrorMessage = '';
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
