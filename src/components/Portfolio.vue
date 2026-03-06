<template>
  <section class="portfolio">
    <div class="section-header">
      <h2>Featured Work</h2>
      <p class="subtitle">A curated selection of our finest projects and creative endeavors</p>
    </div>

    <div class="projects-showcase">
      <div v-for="project in projects" :key="project.id" class="project-item">
        <div class="project-preview">
          <div class="preview-bg" :style="{ background: project.color }"></div>
          <div class="project-overlay">
            <button class="view-btn">View Project →</button>
          </div>
        </div>
        <div class="project-details">
          <h3>{{ project.title }}</h3>
          <p class="project-description">{{ project.description }}</p>
          <div class="project-meta">
            <span v-for="tag in project.tags" :key="tag" class="tag">{{ tag }}</span>
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
      projects: [
        {
          id: 1,
          title: 'Brand Identity System',
          description: 'Comprehensive visual identity including logo, color palette, typography, and complete brand guidelines for a modern tech startup.',
          color: 'linear-gradient(135deg, #f9d5e5 0%, #f4a6c1 100%)',
          tags: ['Branding', 'Design System', 'Identity']
        },
        {
          id: 2,
          title: 'Digital Experience Platform',
          description: 'Full-stack web application featuring real-time collaboration, responsive design, and seamless user experience across all devices.',
          color: 'linear-gradient(135deg, #faf8f6 0%, #e8dfd6 100%)',
          tags: ['Web Design', 'UI/UX', 'Frontend']
        },
        {
          id: 3,
          title: 'Mobile Application Suite',
          description: 'Native and cross-platform mobile applications with intuitive interfaces, optimized performance, and engaging user interactions.',
          color: 'linear-gradient(135deg, #f5f1ed 0%, #d18ca6 100%)',
          tags: ['Mobile', 'App Design', 'iOS/Android']
        },
        {
          id: 4,
          title: 'E-Commerce Ecosystem',
          description: 'End-to-end commerce platform with advanced filtering, personalized recommendations, and streamlined checkout experience.',
          color: 'linear-gradient(135deg, #f9d5e5 0%, #faf8f6 100%)',
          tags: ['E-Commerce', 'Design', 'Strategy']
        }
      ]
    }
  }
}
</script>

<style scoped>
.portfolio {
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

.projects-showcase {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
  gap: 2.5rem;
}

.project-item {
  background: var(--bg-tertiary);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  border: 1px solid var(--border);
}

.project-item:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary);
}

.project-preview {
  position: relative;
  width: 100%;
  padding-bottom: 66.67%;
  overflow: hidden;
  background: var(--bg-secondary);
}

.preview-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.project-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.4s ease;
}

.project-item:hover .project-overlay {
  background: rgba(0, 0, 0, 0.4);
}

.view-btn {
  background: var(--bg-tertiary);
  color: var(--primary);
  border: 2px solid var(--primary);
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
  opacity: 0;
  transform: translateY(10px);
}

.project-item:hover .view-btn {
  opacity: 1;
  transform: translateY(0);
}

.view-btn:hover {
  background: var(--primary);
  color: white;
}

.project-details {
  padding: 2rem;
}

.project-details h3 {
  font-size: 1.3rem;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
  font-weight: 600;
}

.project-description {
  color: var(--text-secondary);
  font-size: 0.95rem;
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.project-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.tag {
  display: inline-block;
  background: linear-gradient(135deg, var(--accent-light) 0%, var(--bg-secondary) 100%);
  color: var(--primary);
  padding: 0.4rem 1rem;
  border-radius: 24px;
  font-size: 0.8rem;
  font-weight: 500;
  border: 1px solid var(--border);
  transition: all 0.3s ease;
}

.tag:hover {
  background: var(--accent);
  color: white;
  border-color: var(--primary);
}

@media (max-width: 768px) {
  .projects-showcase {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .section-header h2 {
    font-size: 2rem;
  }
}
</style>
