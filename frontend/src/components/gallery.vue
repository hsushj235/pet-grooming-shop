<template>
  <section class="gallery">
    <div class="section-head reveal">
      <span class="section-tag" style="color:var(--primary)">GALLERY</span>
      <h2>萌宠秀场</h2>
      <p style="color:var(--text-mid)">来看看洗护后的毛孩子们有多可爱</p>
    </div>
    <div class="gallery-grid">
      <div v-for="(img, i) in photos" :key="i" class="gallery-item reveal" :class="'gallery-item--' + (i % 4)" :style="{ transitionDelay: (i * 0.06) + 's' }">
        <img :src="img.url" :alt="img.alt" class="gallery-img" loading="lazy" />
        <div class="gallery-overlay">
          <span class="gallery-emoji">{{ img.emoji }}</span>
          <span class="gallery-name">{{ img.name }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue'
const photos = [
  { url: 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=500&h=400&fit=crop&q=80', emoji: '🐕', name: '柯基·豆豆', alt: '柯基洗护' },
  { url: 'https://images.unsplash.com/photo-1574158622682-e40e69881006?w=500&h=500&fit=crop&q=80', emoji: '🐈', name: '布偶猫·雪球', alt: '布偶猫' },
  { url: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=500&h=400&fit=crop&q=80', emoji: '🐕', name: '金毛·旺财', alt: '金毛洗护' },
  { url: 'https://images.unsplash.com/photo-1592194996308-7b43878e84a6?w=500&h=600&fit=crop&q=80', emoji: '🐈', name: '英短·蓝蓝', alt: '英短' },
  { url: 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=500&h=400&fit=crop&q=80', emoji: '🐕', name: '哈士奇·二哈', alt: '哈士奇' },
  { url: 'https://images.unsplash.com/photo-1583531352515-8884af319dc1?w=500&h=400&fit=crop&q=80', emoji: '🐩', name: '贵宾·妞妞', alt: '贵宾造型' },
  { url: 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=500&h=500&fit=crop&q=80', emoji: '🐱', name: '橘猫·大橘', alt: '橘猫' },
  { url: 'https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?w=500&h=400&fit=crop&q=80', emoji: '🐕', name: '柴犬·小太郎', alt: '柴犬' },
]
onMounted(() => {
  const reveals = document.querySelectorAll('.reveal')
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('visible') })
  }, { threshold: 0.05, rootMargin: '0px 0px -20px 0px' })
  reveals.forEach(el => observer.observe(el))
})
</script>

<style scoped>
.gallery { padding: 100px 40px; background: var(--white); }
.gallery-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(4, 1fr); grid-auto-rows: 200px; gap: 16px; }
.gallery-item { position: relative; border-radius: var(--radius-md); overflow: hidden; cursor: pointer; box-shadow: var(--shadow-sm); }
.gallery-item--0 { grid-row: span 2; }
.gallery-item--1 { grid-column: span 2; }
.gallery-item--2 { grid-row: span 2; }
.gallery-item--3 { grid-column: span 2; }
.gallery-img { width: 100%; height: 100%; object-fit: cover; transition: transform .6s ease; }
.gallery-item:hover .gallery-img { transform: scale(1.1); }
.gallery-overlay { position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,.6) 0%, transparent 60%); display: flex; flex-direction: column; justify-content: flex-end; padding: 20px; opacity: 0; transition: opacity .3s ease; }
.gallery-item:hover .gallery-overlay { opacity: 1; }
.gallery-emoji { font-size: 28px; margin-bottom: 4px; }
.gallery-name { color: #fff; font-size: 15px; font-weight: 700; }

@media (max-width: 900px) { .gallery { padding: 80px 20px; } .gallery-grid { grid-template-columns: repeat(2, 1fr); grid-auto-rows: 180px; } .gallery-item--0, .gallery-item--2 { grid-row: span 1; } .gallery-item--1, .gallery-item--3 { grid-column: span 1; } }
@media (max-width: 500px) { .gallery-grid { grid-template-columns: 1fr; grid-auto-rows: 220px; } }
</style>
