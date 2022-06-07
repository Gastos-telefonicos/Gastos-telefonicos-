import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/pages/home/HomePage.vue"),
  },
  {
    path: "/bill",
    name: "Bill",
    component: () => import("@/pages/home/BillPage.vue"),
  },
  {
    path: "/projects",
    name: "Projects",
    component: () => import("@/pages/home/ProjectPage.vue"),
  },
  {
    path: "/:catchAll(.*)",
    name: "404",
    component: () => import("@/pages/home/404Page.vue"),
  },
  // {
  //   path: "*",
  //   redirect: "/404",
  // },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
