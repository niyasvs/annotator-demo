import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomeView.vue"),
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
  ],
});

export default router;
