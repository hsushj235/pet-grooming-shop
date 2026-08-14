<template>
  <section class="about">
    <div class="about-inner">
      <div class="about-left reveal">
        <span class="section-tag" style="color:var(--secondary)">ABOUT US</span>
        <h2>让每一份毛茸茸<br /><span class="text-gradient">都闪闪发光</span></h2>
        <p class="lead">
          萌宠洗护成立于 2021 年，是一家专注于宠物洗护美容的专业机构。我们拥有 15 位认证美容师，
          平均从业经验超过 5 年，坚持使用进口天然洗护用品，致力于为每一只毛孩子提供安全、
          舒适、高品质的洗护体验。
        </p>
        <div class="about-features">
          <div v-for="f in features" :key="f.title" class="about-feat">
            <div class="feat-icon">{{ f.icon }}</div>
            <div>
              <strong>{{ f.title }}</strong>
              <span>{{ f.desc }}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="about-right reveal reveal-delay-2">
        <div class="about-img-grid">
          <img src="https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=500&h=600&fit=crop&q=80" alt="宠物洗护" class="about-img-1" loading="lazy" />
          <img src="https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400&h=350&fit=crop&q=80" alt="宠物互动" class="about-img-2" loading="lazy" />
          <img src="https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=350&h=300&fit=crop&q=80" alt="专业美容" class="about-img-3" loading="lazy" />
        </div>
      </div>
    </div>
  </section>

  <section class="team">
    <div class="section-head reveal">
      <span class="section-tag" style="color:var(--primary)">OUR TEAM</span>
      <h2>专业美容师团队</h2>
      <p style="color:var(--text-mid)">每位美容师均持有国家认证资质，平均从业经验 5 年以上</p>
    </div>
    <div class="team-grid">
      <div v-for="(m, i) in team" :key="i" class="team-card reveal" :style="{ transitionDelay: (i * 0.1) + 's' }">
        <div class="team-img-wrap">
          <img :src="m.image" :alt="m.name" class="team-img" loading="lazy" />
          <div class="team-social">
            <a href="#">📱</a><a href="#">💬</a>
          </div>
        </div>
        <div class="team-info">
          <h3>{{ m.name }}</h3>
          <span class="team-title">{{ m.title }}</span>
          <p class="team-bio">{{ m.bio }}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="process">
    <div class="section-head reveal">
      <span class="section-tag" style="color:var(--secondary)">PROCESS</span>
      <h2>洗护服务流程</h2>
      <p style="color:var(--text-mid)">标准化操作流程，确保每一只宠物都得到细致周到的护理</p>
    </div>
    <div class="process-grid">
      <div v-for="(step, i) in steps" :key="i" class="process-card reveal" :style="{ transitionDelay: (i * 0.12) + 's' }">
        <div class="process-num">{{ String(i + 1).padStart(2, '0') }}</div>
        <div class="process-icon">{{ step.icon }}</div>
        <h3>{{ step.title }}</h3>
        <p>{{ step.desc }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue'
const features = [
  { icon: '🌿', title: '天然洗护', desc: '进口植物配方，无刺激不过敏，温和呵护宠物肌肤' },
  { icon: '👨‍⚕️', title: '专业团队', desc: '持证美容师，平均5年以上从业经验，技术精湛' },
  { icon: '🏠', title: '全程可视', desc: '透明操作间，客户可随时观看服务全过程' },
  { icon: '🛡️', title: '品质保证', desc: '服务不满意全额退款，让您完全放心' },
]
const team = [
  { name: '王美丽', title: '首席美容师', bio: '10年宠物美容经验，擅长贵宾造型修剪', image: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=300&h=360&fit=crop&crop=face&q=80' },
  { name: '李秀英', title: '资深美容师', bio: '8年从业经验，擅长大型犬洗护造型', image: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=300&h=360&fit=crop&crop=face&q=80' },
  { name: '张专业', title: '宠物理容师', bio: '6年经验，专注猫咪洗护与SPA护理', image: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=300&h=360&fit=crop&crop=face&q=80' },
  { name: '陈细心', title: '宠物健康管理师', bio: '5年经验，擅长宠物皮肤护理与除虫', image: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=360&fit=crop&crop=face&q=80' },
]
const steps = [
  { icon: '📋', title: '到店接待', desc: '登记宠物信息，了解健康状况与服务需求' },
  { icon: '🛁', title: '洗护SPA', desc: '专业洗护产品，温水SPA深度清洁毛发' },
  { icon: '✂️', title: '造型修剪', desc: '根据宠物品种与主人喜好精心造型' },
  { icon: '💅', title: '精细护理', desc: '修剪指甲、清理耳道、检查皮肤状况' },
  { icon: '✨', title: '吹整造型', desc: '专业吹风梳理，呈现完美造型效果' },
  { icon: '📸', title: '拍照交付', desc: '拍摄美照，向主人展示最终效果' },
]

onMounted(() => {
  const reveals = document.querySelectorAll('.reveal')
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('visible') })
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' })
  reveals.forEach(el => observer.observe(el))
})
</script>

<style scoped>
.about { padding: 100px 40px; background: var(--white); }
.about-inner { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1.2fr 1fr; gap: 80px; align-items: center; }
.section-tag { display: inline-block; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 16px; font-weight: 700; }
.about-left h2 { font-size: clamp(28px, 3.5vw, 44px); font-weight: 900; color: var(--text-dark); line-height: 1.2; margin: 0 0 24px; }
.lead { font-size: 15px; color: var(--text-mid); line-height: 2; margin: 0 0 40px; }
.about-features { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.about-feat { display: flex; gap: 14px; align-items: flex-start; }
.feat-icon { width: 48px; height: 48px; background: linear-gradient(135deg, rgba(255,127,80,.1), rgba(78,205,196,.1)); border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 22px; flex-shrink: 0; }
.about-feat strong { display: block; font-size: 14px; color: var(--text-dark); margin-bottom: 4px; }
.about-feat span { font-size: 12px; color: var(--text-light); line-height: 1.6; }

.about-img-grid { position: relative; }
.about-img-1 { width: 100%; border-radius: 24px; box-shadow: var(--shadow-lg); display: block; }
.about-img-2 { position: absolute; width: 55%; bottom: -40px; left: -20px; border-radius: 20px; border: 5px solid var(--white); box-shadow: var(--shadow-md); }
.about-img-3 { position: absolute; width: 45%; top: -20px; right: -16px; border-radius: 18px; border: 5px solid var(--white); box-shadow: var(--shadow-md); }

/* 团队 */
.team { padding: 100px 40px; background: var(--bg-warm); }
.team-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 28px; max-width: 1200px; margin: 0 auto; }
.team-card { background: var(--white); border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-sm); transition: var(--transition); border: 1px solid var(--border); }
.team-card:hover { transform: translateY(-6px); box-shadow: var(--shadow-lg); }
.team-img-wrap { position: relative; overflow: hidden; height: 240px; }
.team-img { width: 100%; height: 100%; object-fit: cover; transition: transform .5s ease; }
.team-card:hover .team-img { transform: scale(1.06); }
.team-social { position: absolute; bottom: 12px; right: 12px; display: flex; gap: 6px; opacity: 0; transform: translateY(8px); transition: var(--transition); }
.team-card:hover .team-social { opacity: 1; transform: translateY(0); }
.team-social a { width: 36px; height: 36px; background: rgba(255,255,255,.95); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; }
.team-info { padding: 20px; text-align: center; }
.team-info h3 { font-size: 17px; font-weight: 800; color: var(--text-dark); margin: 0 0 4px; }
.team-title { display: block; font-size: 12px; color: var(--primary); font-weight: 600; margin-bottom: 10px; }
.team-bio { font-size: 13px; color: var(--text-light); line-height: 1.6; margin: 0; }

/* 流程 */
.process { padding: 100px 40px; background: var(--white); }
.process-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1100px; margin: 0 auto; }
.process-card { background: var(--bg-light); border-radius: var(--radius-lg); padding: 36px 28px; text-align: center; border: 1px solid var(--border); transition: var(--transition); position: relative; overflow: hidden; }
.process-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--primary), var(--secondary)); transform: scaleX(0); transition: transform .4s ease; }
.process-card:hover::before { transform: scaleX(1); }
.process-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); background: var(--white); }
.process-num { font-size: 42px; font-weight: 900; background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; opacity: .2; line-height: 1; margin-bottom: 12px; }
.process-icon { font-size: 40px; margin-bottom: 16px; }
.process-card h3 { font-size: 17px; font-weight: 800; color: var(--text-dark); margin: 0 0 8px; }
.process-card p { font-size: 13px; color: var(--text-light); line-height: 1.7; margin: 0; }

@media (max-width: 900px) {
  .about-inner { grid-template-columns: 1fr; gap: 60px; }
  .about-img-2, .about-img-3 { display: none; }
  .about-features { grid-template-columns: 1fr; }
  .team-grid { grid-template-columns: repeat(2, 1fr); }
  .process-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .about, .team, .process { padding: 80px 20px; }
  .team-grid { grid-template-columns: 1fr; max-width: 360px; margin-left: auto; margin-right: auto; }
  .process-grid { grid-template-columns: 1fr; max-width: 360px; margin-left: auto; margin-right: auto; }
}
</style>
