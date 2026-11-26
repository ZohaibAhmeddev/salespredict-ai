<template>
  <header class="header">
    <div>
      <h2>SalesPredict AI</h2>
      <p>AI-powered business intelligence</p>
    </div>

    <div class="user-profile">
      <div class="avatar">ZA</div>
      <div>
        <strong>Administrator</strong>
        <span>Project Demo</span>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header {
  height: 80px;
  background: white;
  border-bottom: 1px solid #e5e7eb;
  padding: 15px 30px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header h2 {
  margin: 0;
  font-size: 19px;
}

.header p {
  margin: 4px 0 0;
  font-size: 12px;
  color: #6b7280;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
}

.user-profile strong,
.user-profile span {
  display: block;
  font-size: 12px;
}

.user-profile span {
  color: #6b7280;
  margin-top: 4px;
}

.avatar {
  background: #dbeafe;
  color: #1d4ed8;
  width: 38px;
  height: 38px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-weight: bold;
}
</style>
