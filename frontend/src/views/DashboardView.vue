<script setup>
import { ref, onMounted } from "vue";
import StatCard from "../components/dashboard/StatCard.vue";
import api from "../services/api";

const loading = ref(true);
const error = ref("");

const statistics = ref([
  {
    title: "Total Revenue",
    value: "$0.00",
    description: "From imported sales",
    icon: "💰",
  },
  {
    title: "Total Sales",
    value: "0",
    description: "Units sold",
    icon: "🛒",
  },
  {
    title: "Total Orders",
    value: "0",
    description: "Recorded orders",
    icon: "📦",
  },
  {
    title: "Average Order",
    value: "$0.00",
    description: "Average order value",
    icon: "📈",
  },
]);

async function loadDashboard() {
  loading.value = true;
  error.value = "";

  try {
    const response = await api.get("/api/v1/sales/summary");
    const data = response.data;

    statistics.value = [
      {
        title: "Total Revenue",
        value: `$${Number(data.total_revenue).toFixed(2)}`,
        description: "From imported sales",
        icon: "💰",
      },
      {
        title: "Total Sales",
        value: Number(data.total_sales).toLocaleString(),
        description: "Units sold",
        icon: "🛒",
      },
      {
        title: "Total Orders",
        value: Number(data.total_orders).toLocaleString(),
        description: "Recorded orders",
        icon: "📦",
      },
      {
        title: "Average Order",
        value: `$${(data.total_orders > 0
          ? data.total_revenue / data.total_orders
          : 0
        ).toFixed(2)}`,
        description: "Average order value",
        icon: "📈",
      },
    ];
  } catch (err) {
    error.value = "Unable to load dashboard data.";
    console.error(err);
  } finally {
    loading.value = false;
  }
}

onMounted(loadDashboard);
</script>

<template>
  <div>
    <div class="page-heading">
      <div>
        <h1>Dashboard</h1>
        <p>Overview of your sales performance</p>
      </div>

      <span class="demo-badge">DEVELOPMENT</span>
    </div>

    <p v-if="loading">Loading dashboard...</p>

    <div v-else>
      <p v-if="error" class="error-message">
        {{ error }}
      </p>

      <div class="stats-grid">
        <StatCard
          v-for="stat in statistics"
          :key="stat.title"
          :title="stat.title"
          :value="stat.value"
          :description="stat.description"
          :icon="stat.icon"
        />
      </div>
    </div>

    <div class="welcome-card">
      <h2>Welcome to SalesPredict AI</h2>
      <p>Your AI-powered sales analytics and forecasting platform.</p>
      <p>
        Sales data management, historical analytics and machine learning
        predictions are coming in later phases.
      </p>

      <button @click="loadDashboard">Refresh Dashboard</button>
    </div>
  </div>
</template>

<style scoped>
.page-heading {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 25px;
}

.page-heading h1 {
  margin: 0 0 8px;
  font-size: 25px;
}

.page-heading p {
  margin: 0;
  color: #6b7280;
  font-size: 13px;
}

.demo-badge {
  font-size: 11px;
  background: #dbeafe;
  color: #1e40af;
  padding: 8px 12px;
  border-radius: 6px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 18px;
}

.welcome-card {
  margin-top: 25px;
  padding: 25px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
}

.welcome-card p {
  color: #6b7280;
  line-height: 1.7;
}

.error-message {
  color: #dc2626;
}

button {
  background: #2563eb;
  color: white;
  border: 0;
  border-radius: 7px;
  padding: 10px 16px;
  cursor: pointer;
}

@media (max-width: 1000px) {
  .stats-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 500px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>
