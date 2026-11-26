<script setup>
import { useRoute } from "vue-router";

const route = useRoute();

const menuItems = [
  { name: "Dashboard", path: "/", icon: "▦" },
  { name: "Sales", path: "/sales", icon: "▤" },
  { name: "Forecasts", path: "/forecasts", icon: "⌁" },
  { name: "Settings", path: "/settings", icon: "⚙" },
];
</script>

<template>
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-logo">SP</div>
      <div>
        <h2>SalesPredict</h2>
        <span>AI Platform</span>
      </div>
    </div>
    <p class="menu-label">MAIN MENU</p>

    <nav>
      <RouterLink
        v-for="item in menuItems"
        :key="item.name"
        :to="item.path"
        class="menu-item"
        :class="{ active: route.path === item.path }"
      >
        <span class="menu-icon">{{ item.icon }}</span>
        {{ item.name }}
      </RouterLink>
    </nav>
    <div class="sidebar-footer">
      <span class="status-dot"></span>
      System Online
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 245px;
  min-height: 100vh;
  background: #111827;
  color: #fff;
  padding: 25px 18px;
  display: flex;
  flex-direction: column;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 45px;
}

.brand-logo {
  background: #2563eb;
  padding: 12px;
  border-radius: 10px;
  font-weight: bold;
}

.brand h2 {
  font-size: 17px;
  margin: 0;
}

.brand span {
  color: #9ca3af;
  font-size: 12px;
}

.menu-label {
  color: #9ca3af;
  font-size: 11px;
  margin-bottom: 15px;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  color: #d1d5db;
  text-decoration: none;
  padding: 13px;
  border-radius: 8px;
  margin-bottom: 7px;
  font-size: 14px;
}

.menu-item:hover,
.menu-item.active {
  background: #2563eb;
  color: white;
}

.menu-icon {
  width: 20px;
  text-align: center;
}

.sidebar-footer {
  margin-top: auto;
  color: #9ca3af;
  font-size: 12px;
  padding: 15px 5px;
}

.status-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
  margin-right: 7px;
}
</style>
