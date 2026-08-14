<template>
  <section class="testimonials">
    <div class="section-head reveal">
      <span class="section-tag" style="color:#e6a800">TESTIMONIALS</span>
      <h2>毛孩子家长们的真实评价</h2>
      <p style="color:var(--text-mid)">超过 10,000 位宠主的信赖之选</p>
    </div>
    <div class="testimonials-track">
      <div v-for="(r, i) in reviews" :key="i" class="review-card reveal" :style="{ transitionDelay: (i * 0.08) + 's' }">
        <div class="review-header">
          <div class="review-avatar">{{ r.avatar }}</div>
          <div class="review-meta">
            <strong>{{ r.name }}</strong>
            <span class="review-pet">{{ r.pet }} · {{ r.petType }}</span>
          </div>
          <div class="review-stars">
            <span v-for="s in 5" :key="s" :class="['star', { empty: s > r.rating }]">{{ s <= r.rating ? '★' : '☆' }}</span>
          </div>
        </div>
        <p class="review-text">{{ r.text }}</p>
        <div class="review-date">{{ r.date }}</div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from 'vue'
const reviews = [
  { avatar: '🐕', name: '小明的妈妈', pet: '柯基·豆豆', petType: '狗狗', rating: 5, text: '豆豆每次洗完都香香的，毛发也变得特别顺滑！美容师手法很温柔，豆豆从不抗拒。已经办了年卡，非常放心！', date: '2026-07-10' },
  { avatar: '🐈', name: '花花主人', pet: '英短·蓝猫', petType: '猫咪', rating: 5, text: '家里猫咪胆小，一开始很担心它不适应。结果美容师特别有耐心，整个过程猫咪都很放松。洗完后颜值提升了好几个档次！', date: '2026-06-28' },
  { avatar: '🐕', name: '旺财爸', pet: '金毛·旺财', rating: 5, text: '大型犬洗护真的不容易，这里的服务非常专业。旺财洗完之后像换了只狗，造型超满意！老板人也很好，经常送小礼物。', date: '2026-06-15' },
  { avatar: '🐈', name: '团团圆圆妈', pet: '布偶猫', rating: 5, text: '布偶猫毛发长，不打结真的很难。这里的深层护理做得很到位，梳毛的时候超级仔细，完全没有弄疼小圆。强烈推荐！', date: '2026-05-30' },
  { avatar: '🐕', name: '泰迪妈妈', pet: '泰迪·妞妞', rating: 4, text: '给妞妞做了造型修剪，美容师根据她的脸型设计了可爱的苹果头，朋友都说好看！下次还会来。', date: '2026-05-12' },
  { avatar: '🐇', name: 'bunny爸妈', pet: '垂耳兔·雪球', rating: 5, text: '第一次带兔子来洗护，工作人员非常专业，对兔子的处理很轻柔。洗完之后雪白雪白的，太可爱了！', date: '2026-04-20' },
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
.testimonials { padding: 100px 40px; background: linear-gradient(180deg, var(--bg-warm) 0%, var(--bg-light) 100%); }
.testimonials-track { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1200px; margin: 0 auto; }
.review-card { background: var(--white); border-radius: var(--radius-lg); padding: 28px; box-shadow: var(--shadow-sm); border: 1px solid var(--border); transition: var(--transition); }
.review-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); }
.review-header { display: flex; align-items: center; gap: 14px; margin-bottom: 16px; }
.review-avatar { width: 52px; height: 52px; background: linear-gradient(135deg, rgba(255,127,80,.15), rgba(78,205,196,.15)); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 26px; flex-shrink: 0; }
.review-meta strong { display: block; font-size: 15px; color: var(--text-dark); }
.review-pet { font-size: 12px; color: var(--text-light); }
.review-stars { margin-left: auto; display: flex; gap: 2px; }
.star { color: #FFC107; font-size: 14px; }
.star.empty { color: #E0E0E0; }
.review-text { font-size: 14px; color: var(--text-mid); line-height: 1.8; margin: 0 0 16px; min-height: 80px; }
.review-date { font-size: 12px; color: var(--text-light); }
@media (max-width: 900px) { .testimonials { padding: 80px 20px; } .testimonials-track { grid-template-columns: 1fr; max-width: 500px; } }
</style>
