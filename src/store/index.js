import { createStore } from 'vuex';

const store = createStore({
  state: {
    isAuthenticated: false,
    username: null,
    selectedCategory: null, // 新增的状态变量
    selectedPhoto: null,
  },
  mutations: {
    SET_AUTH(state, payload) {
      state.isAuthenticated = payload.isAuthenticated;
      state.username = payload.username;
    },
    LOGOUT(state) {
      state.isAuthenticated = false;
      state.username = null;
    },
    SET_SELECTED_CATEGORY(state, category) { // 新增的 mutation
      state.selectedCategory = category;
    },
    SET_SELECTED_PHOTO(state, photo) {
      state.selectedPhoto = photo;
    },
  },
  actions: {
    login({ commit }, user) {
      commit('SET_AUTH', { isAuthenticated: true , username: user.username });
    },
    logout({ commit }) {
      commit('LOGOUT');
    },
    setSelectedCategory({ commit }, category) { // 新增的 action
      commit('SET_SELECTED_CATEGORY', category);
    },
    setSelectedPhoto({ commit }, photoId) {
      commit('SET_SELECTED_PHOTO', photoId);
    },
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated,
    username: state => state.username,
    selectedCategory: state => state.selectedCategory, // 新增的 getter
    selectedPhoto: state => state.selectedPhoto,
  },
});

export default store;
