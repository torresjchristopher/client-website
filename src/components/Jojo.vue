<template>
  <section class="jojo">
    <div class="section-header">
      <h2>Meet Jojo</h2>
      <p class="subtitle">Our beloved companion and studio mascot</p>
    </div>

    <div class="jojo-hero">
      <div class="jojo-visual">
        <div class="jojo-image-container">
          <div class="jojo-emoji">🐕</div>
        </div>
      </div>
      <div class="jojo-content">
        <div class="intro-text">
          <p>
            Jojo is more than just a pet—she's the heart and soul of our studio. With boundless enthusiasm, unwavering loyalty, and an infectious joy, Jojo brings warmth and creativity to every project we undertake.
          </p>
          <p>
            Whether it's morning walks that spark new ideas, afternoon cuddles during brainstorming sessions, or late-night energy boosts during crunch time, Jojo is always there, reminding us what truly matters in life.
          </p>
        </div>

        <div class="stats-container">
          <div v-for="stat in stats" :key="stat.label" class="stat-card">
            <div class="stat-icon">{{ stat.icon }}</div>
            <h4>{{ stat.label }}</h4>
            <p>{{ stat.value }}</p>
          </div>
        </div>

        <div class="jojo-gallery">
          <h3>Favorite Moments</h3>
          <div class="gallery-grid">
            <div v-for="moment in moments" :key="moment" class="gallery-item">
              <div class="gallery-placeholder">{{ moment }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      stats: [
        { label: 'Favorite Treat', value: 'Peanut Butter', icon: '🥜' },
        { label: 'Best Quality', value: 'Loyalty & Love', icon: '❤️' },
        { label: 'Personality', value: 'Playful & Sweet', icon: '😊' }
      ],
      moments: ['🎾 Playtime', '🏃 Adventures', '😴 Nap Time', '🎉 Celebrations']
    }
  }
}
</script>

<style scoped>
.jojo {
  width: 100%;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-header h2 {
  font-size: 3rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
}

.subtitle {
  font-size: 1.1rem;
  color: var(--text-secondary);
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.8;
}

.jojo-hero {
  background: var(--bg-tertiary);
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--border);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  padding: 3rem;
  box-shadow: var(--shadow-sm);
}

.jojo-visual {
  display: flex;
  align-items: center;
  justify-content: center;
}

.jojo-image-container {
  position: relative;
  width: 100%;
  aspect-ratio: 1;
  background: linear-gradient(135deg, var(--accent-light) 0%, var(--bg-secondary) 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.jojo-emoji {
  font-size: 180px;
  animation: float 4s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-30px) scale(1.05); }
}

.jojo-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.intro-text p {
  color: var(--text-secondary);
  font-size: 1rem;
  line-height: 1.9;
  margin-bottom: 1.5rem;
}

.stats-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin: 2rem 0;
}

.stat-card {
  background: linear-gradient(135deg, var(--accent-light) 0%, var(--bg-secondary) 100%);
  padding: 1.5rem;
  border-radius: 12px;
  text-align: center;
  border: 1px solid var(--border);
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

.stat-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.stat-card h4 {
  font-size: 0.85rem;
  color: var(--primary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.stat-card p {
  font-size: 0.95rem;
  color: var(--text-primary);
  font-weight: 500;
  margin: 0;
}

.jojo-gallery {
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid var(--border);
}

.jojo-gallery h3 {
  color: var(--text-primary);
  font-size: 1.1rem;
  margin-bottom: 1rem;
  font-weight: 600;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}

.gallery-item {
  aspect-ratio: 1;
  background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--border) 100%);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  border: 1px solid var(--border);
}

.gallery-item:hover {
  transform: scale(1.05);
  box-shadow: var(--shadow-md);
}

.gallery-placeholder {
  font-size: 2rem;
}

@media (max-width: 1024px) {
  .jojo-hero {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .stats-container {
    grid-template-columns: 1fr;
  }

  .gallery-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .jojo-hero {
    padding: 2rem;
  }

  .section-header h2 {
    font-size: 2rem;
  }

  .jojo-emoji {
    font-size: 120px;
  }

  .gallery-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>
