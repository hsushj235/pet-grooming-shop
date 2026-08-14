<template>
  <section class="services" id="services">
    <div class="section-head reveal">
      <span class="section-tag" style="color:var(--primary)">SERVICES</span>
      <h2>专业洗护套餐</h2>
      <p style="color:var(--text-mid)">针对不同类型宠物与毛发需求，精心打造个性化护理方案</p>
    </div>

    <div class="services-grid">
      <div v-for="(s, i) in services" :key="s.id" class="svc-card reveal" :class="{ 'svc-card--popular': s.popular }" :style="{ transitionDelay: (i * 0.1) + 's' }">
        <div class="svc-img-wrapper">
          <img :src="s.image" :alt="s.name" class="svc-img" loading="lazy" />
          <div class="svc-img-overlay"></div>
          <div v-if="s.popular" class="popular-tag">🔥 热门</div>
          <div class="svc-duration">{{ s.duration }}</div>
        </div>
        <div class="svc-body">
          <div class="svc-icon-wrap">{{ s.icon }}</div>
          <h3>{{ s.name }}</h3>
          <p class="svc-desc">{{ s.desc }}</p>
          <div class="svc-features">
            <span v-for="f in s.features" :key="f" class="svc-feat">{{ f }}</span>
          </div>
          <div class="svc-footer">
            <div class="svc-price">
              <span class="price-symbol">¥</span>{{ s.price }}
            </div>
            <button class="btn-book" @click="('book', s)">立即预约</button>
          </div>
        </div>
      </div>
    </div>

    <div class="service-process reveal">
      <div class="process-inner">
        <div class="process-step">
          <div class="step-num">01</div>
          <div class="step-label">选择服务</div>
        </div>
        <div class="process-line"></div>
        <div class="process-step">
          <div class="step-num">02</div>
          <div class="step-label">在线预约</div>
        </div>
        <div class="process-line"></div>
        <div class="process-step">
          <div class="step-num">03</div>
          <div class="step-label">到店体验</div>
        </div>
        <div class="process-line"></div>
        <div class="process-step">
          <div class="step-num">04</div>
          <div class="step-label">满意好评</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { usePetShopStore } from '../stores/petShop'
import { onMounted } from 'vue'
const store = usePetShopStore()
const services = store.services
defineEmits(['book', 'nav'])

onMounted(() => {
  const reveals = document.querySelectorAll('.reveal')
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('visible') })
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' })
  reveals.forEach(el => observer.observe(el))
})
</script>

<style scoped>
.services { padding: 100px 40px; background: var(--bg-warm); }
.section-head { text-align: center; margin-bottom: 64px; }
.section-tag { display: inline-block; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 16px; font-weight: 700; }
.section-head h2 { font-size: clamp(28px, 4vw, 40px); font-weight: 900; color: var(--text-dark); margin: 0 0 12px; }

.services-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
  max-width: 1200px;
  margin: 0 auto 80px;
}

.svc-card {
  background: var(--white);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
  border: 1px solid var(--border);
}
.svc-card:hover { transform: translateY(-8px); box-shadow: var(--shadow-lg); border-color: rgba(255,127,80,.2); }
.svc-card--popular { border-color: rgba(255,127,80,.3); box-shadow: 0 4px 24px rgba(255,127,80,.12); }

.svc-img-wrapper { position: relative; height: 180px; overflow: hidden; }
.svc-img { width: 100%; height: 100%; object-fit: cover; transition: transform .6s ease; }
.svc-card:hover .svc-img { transform: scale(1.08); }
.svc-img-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,.3) 0%, transparent 60%);
}
.popular-tag {
  position: absolute; top: 12px; right: 12px;
  background: rgba(255,255,255,.95); color: var(--primary);
  font-size: 12px; padding: 4px 12px; border-radius: 50px;
  font-weight: 700; backdrop-filter: blur(8px);
}
.svc-duration {
  position: absolute; bottom: 12px; left: 12px;
  background: rgba(0,0,0,.6); color: #fff;
  font-size: 12px; padding: 4px 10px; border-radius: 50px;
  backdrop-filter: blur(8px);
}

.svc-body { padding: 24px; }
.svc-icon-wrap { font-size: 32px; width: 56px; height: 56px; background: var(--bg-light); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.svc-card h3 { font-size: 18px; font-weight: 800; color: var(--text-dark); margin: 0 0 8px; }
.svc-desc { font-size: 13px; color: var(--text-light); line-height: 1.7; margin: 0 0 16px; min-height: 44px; }
.svc-features { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 20px; }
.svc-feat { font-size: 11px; color: var(--secondary); background: rgba(78,205,196,.1); padding: 3px 10px; border-radius: 50px; font-weight: 600; }
.svc-footer { display: flex; align-items: center; justify-content: space-between; padding-top: 16px; border-top: 1px solid var(--border); }
.svc-price { font-size: 26px; font-weight: 900; color: var(--primary); }
.svc-price .price-symbol { font-size: 14px; font-weight: 600; }
.btn-book { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: #fff; padding: 10px 24px; border-radius: 50px; font-size: 13px; font-weight: 600; border: none; transition: var(--transition); box-shadow: 0 2px 12px rgba(255,127,80,.25); }
.btn-book:hover { transform: scale(1.05); box-shadow: 0 4px 20px rgba(255,127,80,.4); }

.service-process { max-width: 800px; margin: 0 auto; }
.process-inner { display: flex; align-items: center; justify-content: center; background: var(--white); border-radius: var(--radius-lg); padding: 40px 48px; box-shadow: var(--shadow-sm); border: 1px solid var(--border); }
.process-step { text-align: center; flex: 1; }
.step-num { font-size: 28px; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 8px; }
.step-label { font-size: 14px; color: var(--text-mid); font-weight: 600; }
.process-line { width: 60px; height: 2px; background: linear-gradient(90deg, var(--primary), var(--secondary)); opacity: .3; flex-shrink: 0; }

@media (max-width: 900px) {
  .services { padding: 80px 20px; }
  .services-grid { grid-template-columns: 1fr; max-width: 440px; }
  .process-inner { flex-direction: column; gap: 20px; padding: 32px 24px; }
  .process-line { width: 2px; height: 32px; }
}
@media (min-width: 901px) and (max-width: 1100px) {
  .services-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>
