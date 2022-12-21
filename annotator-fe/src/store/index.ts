import { createStore } from "vuex";
import type { Image, State, User } from "./types";

const state = {
  user: { name: "" },
  images: [],
};

const mutations = {
  SET_USER: (state: State, value: User) => (state.user = value),
  SET_IMAGES: (state: State, value: Image[]) => (state.images = value),
};

const store = createStore({
  state(): State {
    return state;
  },
  mutations,
});

export default store;
