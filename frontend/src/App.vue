<script setup>
import AppSidebar from "./components/layout/AppSidebar.vue";
import AppHeader from "./components/layout/AppHeader.vue";
</script>

<template>
    <div class="app-layout">
        <AppSidebar />
        <div class="main-section">
            <AppHeader />
            <main class="page-content">
                <RouterView />
            </main>
        </div>
    </div>
</template>


<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f3f4f6;
}

.app-layout {
    display: flex;
    min-height: 100vh;
}

.main-section {
    flex: 1;
    min-width: 0;
}

.page-content {
    padding: 30px;
}

@media (max-width: 700px) {
    .app-layout {
        flex-direction: column;
    }

    .sidebar {
        width: 100% !important;
        min-height: auto !important;
    }

    .page-content {
        padding: 16px;
    }
}
</style>