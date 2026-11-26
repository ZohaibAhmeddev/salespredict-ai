import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "../views/DashboardView.vue";
import ForecastView from "../views/ForecastView.vue";
import SettingsView from "../views/SettingsView.vue";
import SalesView from "../views/SalesView.vue";

const routes = [
  {
    path: "/",
    name: "Dashboard",
    component: DashboardView,
  },
  {
    path: "/forecast",
    name: "Forecast",
    component: ForecastView,
  },
  {
    path: "/settings",
    name: "Settings",
    component: SettingsView,
  },
  {
    path: "/sales",
    name: "Sales",
    component: SalesView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
