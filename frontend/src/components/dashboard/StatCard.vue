<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
  value: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    default: "",
  },
  icon: {
    type: String,
    default: "📊",
  },
});
</script>
<template>
  <div class="stat-card">
    <div class="card-top">
      <span>{{ title }}</span>
      <span class="icon">{{ icon }}</span>
    </div>

    <h2>{{ value }}</h2>

    <p>{{ description }}</p>
  </div>
</template>

<style scoped>
.stat-card {
  background: white;
  padding: 22px;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
}

.card-top {
  display: flex;
  justify-content: space-between;
  color: #6b7280;
  font-size: 13px;
}

.icon {
  font-size: 22px;
}

.stat-card h2 {
  font-size: 27px;
  margin: 20px 0 8px;
}

.stat-card p {
  color: #6b7280;
  font-size: 12px;
  margin: 0;
}
</style>
