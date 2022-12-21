import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Annotate from "../components/Annotate.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/Login.vue"),
      meta: {
        layout: "AuthLayout",
      },
    },
    {
      path: "/register",
      name: "register",
      component: () => import("../views/Register.vue"),
      meta: {
        layout: "AuthLayout",
      },
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/home",
      name: "home-view",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/project/:projectId",
      name: "project",
      component: () => import("../views/ProjectView.vue"),
    },
    {
      path: "/image/:imageId",
      name: "image",
      component: () => import("../views/AnnotateView.vue"),
    },
    {
      path: "/annotate",
      name: "home",
      component: Annotate,
    },
  ],
});

export default router;
