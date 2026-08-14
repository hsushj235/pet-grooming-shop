<template>
  <section class="hero">
    <div class="deco-circle deco-1"></div>
    <div class="deco-circle deco-2"></div>
    <div class="deco-circle deco-3"></div>

    <div class="hero-inner">
      <div class="hero-left">
        <div class="hero-badge reveal">
          <span class="badge-dot"></span>
          专业宠物洗护 · 始于 2021
        </div>
        <h1 class="reveal reveal-delay-1">
          给毛孩子<br />
          <span class="text-gradient">最温柔的呵护</span>
        </h1>
        <p class="hero-desc reveal reveal-delay-2">
          资深美容师团队 · 进口天然洗护用品 · 全程透明可视操作<br />
          让每一次洗护都成为享受
        </p>
        <div class="hero-actions reveal reveal-delay-3">
          <button class="btn-primary" @click="('nav', 'booking')">
            立即预约
            <span class="btn-arrow">→</span>
          </button>
          <button class="btn-outline" @click="('nav', 'services')">
            了解服务项目
          </button>
        </div>
        <div class="hero-trust reveal reveal-delay-4">
          <div class="trust-avatars">
            <span class="avatar">🐕</span>
            <span class="avatar">🐈</span>
            <span class="avatar">🐇</span>
            <span class="avatar">🐾</span>
          </div>
          <span>已为 <strong>10,000+</strong> 只毛孩子提供专业洗护服务</span>
        </div>
      </div>

      <div class="hero-right reveal reveal-delay-2">
        <div class="hero-img-wrapper">
          <img src="https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=600&h=700&fit=crop&q=80" alt="萌宠洗护" class="hero-main-img" loading="lazy" />
          <div class="hero-floating-card card-1">
            <span class="card-icon">⭐</span>
            <div><strong>98%</strong><small>好评率</small></div>
          </div>
          <div class="hero-floating-card card-2">
            <span class="card-icon">🛁</span>
            <div><strong>5,000+</strong><small>月度服务</small></div>
          </div>
          <div class="hero-floating-card card-3">
            <span class="card-icon">👨‍⚕️</span>
            <div><strong>15+</strong><small>认证美容师</small></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="stats-bar">
    <div class="stats-inner">
      <div class="stat-item reveal">
        <div class="stat-num" data-target="10000">0</div>
        <div class="stat-label">累计服务宠物</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item reveal reveal-delay-1">
        <div class="stat-num" data-target="98">0</div>
        <div class="stat-label">客户好评率 %</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item reveal reveal-delay-2">
        <div class="stat-num" data-target="5">0</div>
        <div class="stat-label">年专业经验</div>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item reveal reveal-delay-3">
        <div class="stat-num" data-target="15">0</div>
        <div class="stat-label">认证美容师</div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted, ref } from 'vue'
defineEmits(['nav'])

const counted = ref(false)
function animateCounters() {
  if (counted.value) return
  counted.value = true
  document.querySelectorAll('.stat-num[data-target]').forEach(el => {
    const target = parseInt(el.dataset.target)
    const duration = 2000
    const start = performance.now()
    function update(now) {
      const progress = Math.min((now - start) / duration, 1)
      const eased = 1 - Math.pow(1 - progress, 3)
      el.textContent = Math.floor(eased * target).toLocaleString()
      if (progress < 1) requestAnimationFrame(update)
      else el.textContent = target.toLocaleString() + (target === 98 ? '%' : '+')
    }
    requestAnimationFrame(update)
  })
}

onMounted(() => {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) animateCounters() })
  }, { threshold: 0.3 })
  const statsBar = document.querySelector('.stats-bar')
  if (statsBar) observer.observe(statsBar)

  const reveals = document.querySelectorAll('.reveal')
  const revObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('visible') })
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' })
  reveals.forEach(el => revObserver.observe(el))
})
</script>

<style scoped>
.hero {
  position: relative;
  min-height: 680px;
  display: flex;
  align-items: center;
  overflow: hidden;
  background: linear-gradient(135deg, #FFF9F5 0%, #FEF0E8 40%, #F0FFFE 100%);
  padding: 60px 40px 80px;
}
.deco-circle { position: absolute; pointer-events: none; border-radius: 50%; }
.deco-1 { width: 400px; height: 400px; background: radial-gradient(circle, rgba(255,127,80,.12) 0%, transparent 70%); top: -100px; right: -80px; animation: float 8s ease-in-out infinite; }
.deco-2 { width: 300px; height: 300px; background: radial-gradient(circle, rgba(78,205,196,.1) 0%, transparent 70%); bottom: -60px; left: 10%; animation: floatReverse 10s ease-in-out infinite; }
.deco-3 { width: 160px; height: 160px; background: radial-gradient(circle, rgba(255,230,109,.2) 0%, transparent 70%); top: 30%; left: 5%; animation: float 6s ease-in-out infinite; }

.hero-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
  position: relative;
  z-index: 1;
  width: 100%;
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255,255,255,.8);
  border: 1px solid var(--border);
  padding: 8px 18px;
  border-radius: 50px;
  font-size: 12px;
  color: var(--text-mid);
  letter-spacing: 1px;
  margin-bottom: 28px;
  backdrop-filter: blur(10px);
}
.badge-dot { width: 8px; height: 8px; background: var(--primary); border-radius: 50%; animation: pulse 2s ease-in-out infinite; }
.hero h1 { font-size: clamp(40px, 5vw, 64px); font-weight: 900; color: var(--text-dark); line-height: 1.1; margin: 0 0 24px; letter-spacing: -1px; }
.text-gradient {
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.hero-desc { font-size: 16px; color: var(--text-mid); line-height: 1.9; margin: 0 0 36px; max-width: 460px; }
.hero-actions { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 40px; }
.btn-arrow { display: inline-block; margin-left: 6px; transition: transform .3s; }
.btn-primary:hover .btn-arrow { transform: translateX(4px); }
.hero-trust { display: flex; align-items: center; gap: 12px; font-size: 13px; color: var(--text-light); }
.trust-avatars { display: flex; }
.trust-avatars .avatar {
  width: 32px; height: 32px; border-radius: 50%; background: var(--white);
  border: 2px solid var(--white); margin-left: -8px; display: flex;
  align-items: center; justify-content: center; font-size: 16px;
  box-shadow: var(--shadow-sm);
}
.trust-avatars .avatar:first-child { margin-left: 0; }
.hero-trust strong { color: var(--text-dark); }
.hero-right { position: relative; display: flex; justify-content: center; }
.hero-img-wrapper { position: relative; width: 100%; max-width: 500px; }
.hero-main-img { width: 100%; height: 520px; object-fit: cover; border-radius: 32px; box-shadow: var(--shadow-lg); display: block; }
.hero-floating-card {
  position: absolute; background: rgba(255,255,255,.95); backdrop-filter: blur(16px);
  border-radius: var(--radius-md); padding: 16px 20px; display: flex; align-items: center;
  gap: 12px; box-shadow: var(--shadow-md); border: 1px solid rgba(255,255,255,.6);
}
.card-1 { top: 40px; left: -40px; animation: float 5s ease-in-out infinite; }
.card-2 { bottom: 80px; right: -30px; animation: floatReverse 6s ease-in-out infinite; }
.card-3 { bottom: -10px; left: 20px; animation: float 7s ease-in-out infinite .5s; }
.card-icon { font-size: 24px; }
.hero-floating-card strong { display: block; font-size: 18px; color: var(--text-dark); font-weight: 800; }
.hero-floating-card small { font-size: 11px; color: var(--text-light); }

.stats-bar { background: var(--white); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); padding: 48px 40px; }
.stats-inner { max-width: 1080px; margin: 0 auto; display: flex; align-items: center; justify-content: center; gap: 0; }
.stat-item { text-align: center; flex: 1; }
.stat-num { font-size: 44px; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--primary-dark)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1; margin-bottom: 8px; }
.stat-label { font-size: 13px; color: var(--text-light); letter-spacing: .5px; }
.stat-divider { width: 1px; height: 56px; background: var(--border); margin: 0 32px; }

@keyframes float { 0%,100%{transform:translateY(0) rotate(0deg)} 50%{transform:translateY(-20px) rotate(3deg)} }
@keyframes floatReverse { 0%,100%{transform:translateY(0) rotate(0deg)} 50%{transform:translateY(16px) rotate(-3deg)} }
@keyframes pulse { 0%,100%{transform:scale(1)} 50%{transform:scale(1.05)} }

@media (max-width: 900px) {
  .hero-inner { grid-template-columns: 1fr; text-align: center; }
  .hero-desc { margin-left: auto; margin-right: auto; }
  .hero-actions { justify-content: center; }
  .hero-trust { justify-content: center; }
  .hero-right { order: -1; margin-bottom: 20px; }
  .hero-main-img { height: 320px; border-radius: 24px; }
  .hero-floating-card { display: none; }
  .deco-1 { width: 200px; height: 200px; }
  .deco-2 { width: 150px; height: 150px; }
  .stats-inner { flex-wrap: wrap; gap: 24px; }
  .stat-divider { display: none; }
  .stat-num { font-size: 32px; }
}
</style>
