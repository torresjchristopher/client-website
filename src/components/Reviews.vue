<template>
  <section class="reviews">
    <div class="section-header">
      <h2>Client Testimonials</h2>
      <p class="subtitle">What our clients say about our work and collaboration</p>
    </div>

    <div class="testimonials-grid">
      <div v-for="review in reviews" :key="review.id" class="testimonial-card">
        <div class="stars">
          <span v-for="n in review.rating" :key="n" class="star">★</span>
        </div>
        <p class="testimonial-text">"{{ review.text }}"</p>
        <div class="reviewer-info">
          <div class="reviewer-avatar">{{ review.initials }}</div>
          <div class="reviewer-details">
            <h4>{{ review.author }}</h4>
            <p>{{ review.title }}</p>
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
      reviews: [
        {
          id: 1,
          author: 'Sarah Mitchell',
          title: 'CEO, TechFlow Inc.',
          rating: 5,
          text: 'Exceptional work that transformed our brand identity. The attention to detail and creative problem-solving exceeded all expectations.',
          initials: 'SM'
        },
        {
          id: 2,
          author: 'James Chen',
          title: 'Director, Creative Labs',
          rating: 5,
          text: 'A true professional team that delivered on timeline and budget. Their strategic approach to design is unmatched in the industry.',
          initials: 'JC'
        },
        {
          id: 3,
          author: 'Emma Richardson',
          title: 'Founder, StartupHub',
          rating: 5,
          text: 'From concept to execution, every step was handled with precision. Our new platform has already increased engagement by 300%.',
          initials: 'ER'
        },
        {
          id: 4,
          author: 'Michael Anderson',
          title: 'CMO, Global Brands',
          rating: 5,
          text: 'The creative vision and execution quality is world-class. They understand not just design, but business strategy as well.',
          initials: 'MA'
        }
      ]
    }
  }
}
</script>

<style scoped>
.reviews {
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

.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 2rem;
}

.testimonial-card {
  background: var(--bg-tertiary);
  padding: 2rem;
  border-radius: 12px;
  border: 1px solid var(--border);
  transition: all 0.4s ease;
  display: flex;
  flex-direction: column;
}

.testimonial-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-md);
  border-color: var(--primary);
}

.stars {
  display: flex;
  gap: 0.25rem;
  margin-bottom: 1.5rem;
}

.star {
  color: var(--primary);
  font-size: 1rem;
}

.testimonial-text {
  color: var(--text-secondary);
  font-size: 1rem;
  line-height: 1.8;
  margin-bottom: 2rem;
  flex-grow: 1;
  font-style: italic;
}

.reviewer-info {
  display: flex;
  gap: 1rem;
  align-items: center;
  border-top: 1px solid var(--border);
  padding-top: 1.5rem;
}

.reviewer-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--accent-light) 0%, var(--accent) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 0.9rem;
}

.reviewer-details h4 {
  font-size: 0.95rem;
  color: var(--text-primary);
  margin: 0;
  font-weight: 600;
}

.reviewer-details p {
  font-size: 0.85rem;
  color: var(--text-tertiary);
  margin: 0.25rem 0 0 0;
}

@media (max-width: 768px) {
  .testimonials-grid {
    grid-template-columns: 1fr;
  }

  .section-header h2 {
    font-size: 2rem;
  }
}
</style>
