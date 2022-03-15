import { getAPI } from '../../axios-api';

const state = {
  accessToken: null,
  refreshToken: null,
  currentUser: {
    id: null,
    username: '',
    first_name: '',
    last_name: '',
  },
  userHistory: [],
  registerErrorMessages: {
    username: [],
    first_name: [],
    last_name: [],
    password: [],
    password2: [],
  },
  loginErrorMessages: {
    username: [],
    password: [],
    detail: '',
  },
};

const getters = {
  getUser: (state) => state.currentUser,
  getHistory: (state) => state.userHistory,
  getLoginErrorMessages: (state) => state.loginErrorMessages,
  getRegisterErrorMessages: (state) => state.registerErrorMessages,
};

const actions = {
  // obnovenie prístupového tokenu
  async refreshAccessToken({ commit }) {
    // ak je obnovovací token v lokálnom úložisku
    if (localStorage.getItem('refreshToken') != null) {
      var refreshToken = localStorage.getItem('refreshToken');
      localStorage.removeItem('accessToken');
      return new Promise((resolve, reject) => {
        // POST požiadavka na koncový bod
        // ako parameter posielame obnovovací token
        getAPI
          .post('/api-token-refresh/', {
            refresh: refreshToken,
          })
          .then((response) => {
            // keď príde odooveď zavolá sa mutácia na zmenu tokenov
            commit('updateStorage', {
              access: response.data.access,
              refresh: refreshToken,
            });
            resolve();
          })
          .catch((err) => {
            // keď príde chyba odstránime tokeny z lokálneho úložiska
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            console.log(err);
            reject(err);
          });
      });
    }
  },
  // prihlásenie
  async userLogin({ commit }, user) {
    localStorage.removeItem('accessToken');
    return new Promise((resolve, reject) => {
      // POST požiadavka na koncový bod
      // posielame parametre username a password objektu user
      getAPI
        .post('/api-token/', {
          username: user.username,
          password: user.password,
        })
        .then((response) => {
          // keď príde odooveď zavolá sa mutácia na zmenu tokenov
          commit('updateStorage', {
            access: response.data.access,
            refresh: response.data.refresh,
          });
          resolve();
        })
        .catch((err) => {
          // keď príde chyba odstránime token a zavoláme mutáciu na zmenu chybových hlásení
          if (err.response) {
            localStorage.removeItem('accessToken');
            commit('setLoginErrorMessages', err.response.data);
          }
          console.log(err);
          reject(err);
        });
    });
  },
  // odhlásenie
  async userLogout({ commit }) {
    if (localStorage.getItem('accessToken')) {
      // zavoláme mutácie na vymazanie tokenov a objektu používateľa
      commit('destroyToken');
      commit('removeCurrentUser');
    }
  },
  // registrácia
  async userCreateAccount({ commit }, user) {
    commit('destroyToken');
    return new Promise((resolve, reject) => {
      // POST požiadavka na koncový bod
      // posielame parametre username, password,
      // confirm_password, first_name a last_name objektu user
      getAPI
        .post('/register/', {
          username: user.username,
          password: user.password,
          password2: user.confirm_password,
          first_name: user.first_name,
          last_name: user.last_name,
        })
        .then(() => {
          // keď príde odpoveď
          resolve();
        })
        .catch((err) => {
          // keď príde chyba zavoláme mutáciu na zmenu chybových hlásení
          if (err.response) {
            commit('setRegisterErrorMessages', err.response.data);
          }
          console.log(err);
          reject(err);
        });
    });
  },
  // údaje o používateľovi
  async getCurrentUser({ commit }, token) {
    if (localStorage.getItem('accessToken') != null) {
      return new Promise((resolve, reject) => {
        // GET požiadavka na koncový bod
        // posielame prístupový token
        getAPI
          .get('/get-user/?access_token=' + token)
          .then((response) => {
            // keď príde odpoveď zavolá sa mutácia na zmenu používateľských údajov
            commit('setCurrentUser', response.data);
            resolve();
          })
          .catch((err) => {
            // keď príde chyba zmažeme tokeny
            if (err.response.status == 500) {
              commit('destroyToken');
            }
            console.log(err);
            reject(err);
          });
      });
    }
  },
  // história nahratých súborov používateľa
  async getUserHistory({ commit }, uid) {
    return new Promise((resolve, reject) => {
      // GET požiadavka na koncový bod
      // posielame id používateľa
      getAPI
        .get('/get-user-history/?uid=' + uid)
        .then((response) => {
          // keď príde odpoveď zavolá sa mutácia na zmenu údajov o histórii používateľa
          commit('setUserHistory', response.data);
          resolve();
        })
        .catch((err) => {
          // keď príde chyba
          console.log(err);
          reject(err);
        });
    });
  },
  // zavolá sa mutácia na resetnovanie chybových hlásení
  async refreshMessages({ commit }) {
    commit('removeMessages');
  },
};

const mutations = {
  updateStorage(state, { access, refresh }) {
    // zmena tokenov
    state.accessToken = access;
    state.refreshToken = refresh;
    localStorage.setItem('accessToken', access);
    localStorage.setItem('refreshToken', refresh);
  },
  destroyToken(state) {
    // zmazanie tokenov
    state.accessToken = null;
    state.refreshToken = null;
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
  },
  setCurrentUser: (state, user) => {
    // zmena používateľských údajov
    state.currentUser.id = user.id;
    state.currentUser.username = user.username;
    state.currentUser.first_name = user.first_name;
    state.currentUser.last_name = user.last_name;
  },
  removeCurrentUser: (state) => {
    // zmazanie používateľských údajov
    state.currentUser.id = null;
    state.currentUser.username = '';
    state.currentUser.first_name = '';
    state.currentUser.last_name = '';
  },
  setUserHistory: (state, analyses) => {
    // zmena používateľskej histórie
    state.userHistory = JSON.parse(analyses);
  },
  setLoginErrorMessages: (state, errors) => {
    // zmena chybových hlásení pri prihlasovaní
    state.loginErrorMessages.username = [];
    state.loginErrorMessages.password = [];
    state.loginErrorMessages.detail = '';
    if (errors.username != null) {
      errors.username.forEach((username_error) => {
        state.loginErrorMessages.username.push(username_error);
      });
    }
    if (errors.password != null) {
      errors.password.forEach((password_error) => {
        state.loginErrorMessages.password.push(password_error);
      });
    }
    if (errors.detail != null) {
      state.loginErrorMessages.detail = errors.detail;
    }
  },
  setRegisterErrorMessages: (state, messages) => {
    // zmena chybových hlásení pri registrácii
    state.registerErrorMessages.username = [];
    state.registerErrorMessages.first_name = [];
    state.registerErrorMessages.last_name = [];
    state.registerErrorMessages.password = [];
    state.registerErrorMessages.password2 = [];
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
    if (messages.password2 != null) {
      messages.password2.forEach((password2_error) => {
        state.registerErrorMessages.password2.push(password2_error);
      });
    }
  },
  removeMessages: (state) => {
    // zmazanie chybových hlásení
    state.loginErrorMessages.username = [];
    state.loginErrorMessages.password = [];
    state.loginErrorMessages.detail = '';
    state.registerErrorMessages.username = [];
    state.registerErrorMessages.first_name = [];
    state.registerErrorMessages.last_name = [];
    state.registerErrorMessages.password = [];
    state.registerErrorMessages.password2 = [];
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
