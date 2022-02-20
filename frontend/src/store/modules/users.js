import { getAPI } from '../../axios-api';

const state = {
  accessToken: null,
  refreshToken: null,
};

const getters = {
  isLoggedIn(state) {
    return state.accessToken != null;
  },
};

const actions = {
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
      console.log('remove');
      commit('destroyToken');
    }
  },
  async userCreateAccount(user) {
    console.log('create');
    return new Promise((resolve, reject) => {
      getAPI
        .post('/create-account/', {
          username: user.username,
          password: user.password,
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
};

const mutations = {
  updateStorage(state, { access, refresh }) {
    state.accessToken = access;
    state.refreshToken = refresh;
    localStorage.setItem('accessToken', access);
  },
  destroyToken(state) {
    state.accessToken = null;
    state.refreshToken = null;
    localStorage.removeItem('accessToken');
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
