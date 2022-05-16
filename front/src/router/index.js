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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
