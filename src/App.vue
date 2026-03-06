<template>
  <div id="app" class="app">
    <header class="header">
      <h1>Studio</h1>
      <nav>
        <button @click="activeTab = 'Portfolio'" :class="{ active: activeTab === 'Portfolio' }">Portfolio</button>
        <button @click="activeTab = 'Reviews'" :class="{ active: activeTab === 'Reviews' }">Reviews</button>
        <button @click="activeTab = 'Jojo'" :class="{ active: activeTab === 'Jojo' }">Jojo</button>
      </nav>
    </header>

    <main>
      <Portfolio v-show="activeTab === 'Portfolio'" />
      <Reviews v-show="activeTab === 'Reviews'" />
      <Jojo v-show="activeTab === 'Jojo'" />
    </main>
  </div>
</template>

<script>
import { ref } from 'vue'
import Portfolio from './components/Portfolio.vue'
import Reviews from './components/Reviews.vue'
import Jojo from './components/Jojo.vue'

export default {
  components: { Portfolio, Reviews, Jojo },
  setup() {
    const activeTab = ref('Portfolio')
    return { activeTab }
  }
}
</script>

<style scoped>
.app {
  min-height: 100vh;
  background: #faf8f6;
}

.header {
  background: white;
  padding: 2rem;
  border-bottom: 1px solid #e8dfd6;
}

.header h1 {
  margin: 0 0 1rem 0;
  color: #1a1a1a;
}

nav {
  display: flex;
  gap: 1rem;
}

nav button {
  background: none;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  color: #666;
  font-weight: 500;
  border-bottom: 2px solid transparent;
}

nav button.active {
  color: #d18ca6;
  border-bottom-color: #d18ca6;
}

main {
  max-width: 1400px;
  margin: 0 auto;
  padding: 3rem 2rem;
}
</style>

<style scoped>
.app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
}

.header {
  background: var(--bg-tertiary);
  border-bottom: 1px solid var(--border);
  padding: 1.5rem 0;
  box-shadow: var(--shadow-sm);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logo-icon {
  font-size: 1.5rem;
  animation: glow 2s ease-in-out infinite;
}

@keyframes glow {
  0%, 100% { filter: drop-shadow(0 0 4px rgba(209, 140, 166, 0.3)); }
  50% { filter: drop-shadow(0 0 12px rgba(209, 140, 166, 0.6)); }
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text-primary);
}

.nav-menu {
  display: flex;
  gap: 2rem;
}

.nav-link {
  background: none;
  border: none;
  font-size: 0.95rem;
  font-weight: 500;
  color: var(--text-secondary);
  cursor: pointer;
  position: relative;
  transition: color 0.3s ease;
  padding: 0.5rem 0;
}

.nav-link:hover {
  color: var(--primary);
}

.nav-link.active {
  color: var(--primary);
}

.nav-link.active::after {
  content: '';
  position: absolute;
  bottom: -0.75rem;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--primary);
  border-radius: 1px;
}

.main-content {
  flex: 1;
  max-width: 1400px;
  width: 100%;
  margin: 0 auto;
  padding: 4rem 2rem;
}

.footer {
  background: var(--bg-tertiary);
  border-top: 1px solid var(--border);
  margin-top: 4rem;
}

.footer-top {
  max-width: 1400px;
  margin: 0 auto;
  padding: 3rem 2rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 3rem;
}

.footer-col h3 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

.footer-col h4 {
  font-size: 0.95rem;
  margin-bottom: 1rem;
  color: var(--text-primary);
  font-weight: 600;
}

.footer-col p {
  color: var(--text-tertiary);
  font-size: 0.9rem;
  line-height: 1.7;
}

.footer-links {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.footer-links a {
  font-size: 0.9rem;
  color: var(--text-tertiary);
  transition: color 0.3s ease;
}

.footer-links a:hover {
  color: var(--primary);
}

.footer-bottom {
  border-top: 1px solid var(--border);
  padding: 2rem;
  text-align: center;
  color: var(--text-tertiary);
  font-size: 0.9rem;
}

.page-enter-active, .page-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
}

.page-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.page-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

@media (max-width: 768px) {
  .header-container {
    flex-direction: column;
    gap: 1.5rem;
  }

  .nav-menu {
    justify-content: center;
    gap: 1rem;
  }

  .footer-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .main-content {
    padding: 2rem 1rem;
  }
}
</style>
