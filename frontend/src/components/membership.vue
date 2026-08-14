<template>
  <section class="membership">
    <div class="mem-bg-deco"></div>
    <div class="membership-inner">
      <div class="section-head reveal">
        <span class="section-tag" style="color:#6366f1">MEMBERSHIP</span>
        <h2>成为萌宠会员，享受更多权益</h2>
        <p style="color:var(--text-mid)">充值即享专属折扣，让每一次洗护都更划算</p>
      </div>

      <div class="plans-grid">
        <div v-for="p in plans" :key="p.level" class="plan-card reveal" :class="{ 'plan-card--featured': p.featured }" :style="{ transitionDelay: (plans.indexOf(p) * 0.1) + 's' }">
          <div v-if="p.featured" class="plan-badge">⭐ 最受欢迎</div>
          <div class="plan-header" :style="{ background: p.gradient }">
            <div class="plan-icon-wrap">{{ p.icon }}</div>
            <h3>{{ p.level }}</h3>
            <div class="plan-price-wrap">
              <span class="plan-price">¥{{ p.price }}</span>
              <span class="plan-unit">/次洗护</span>
            </div>
            <div class="plan-original">原价 ¥{{ p.original }}</div>
          </div>
          <ul class="plan-features">
            <li v-for="f in p.features" :key="f">
              <span class="feat-check">✓</span>{{ f }}
            </li>
          </ul>
          <button class="btn-plan" :style="{ background: p.gradient, boxShadow: p.shadow }" @click="handlePlan(p)">
            {{ store.currentUser && store.currentUser.plan === p.level ? '✓ 当前等级' : '立即开通' }}
          </button>
        </div>
      </div>

      <div v-if="store.currentUser" class="member-panel reveal">
        <div class="panel-header">
          <h3>👤 我的会员中心</h3>
          <span class="member-level-badge" :style="{ background: currentPlan?.gradient }">{{ store.currentUser.plan || '普通客户' }}</span>
        </div>
        <div class="member-stats">
          <div class="m-stat">
            <div class="m-stat-num" style="color:var(--primary)">¥{{ store.currentUser.balance }}</div>
            <div class="m-stat-label">账户余额</div>
          </div>
          <div class="m-stat">
            <div class="m-stat-num">¥{{ store.currentUser.totalSpent }}</div>
            <div class="m-stat-label">累计消费</div>
          </div>
          <div class="m-stat">
            <div class="m-stat-num">{{ store.orders.filter(o=>o.member).length }}</div>
            <div class="m-stat-label">服务次数</div>
          </div>
          <div class="m-stat">
            <div class="m-stat-num">{{ store.currentUser.joinDate }}</div>
            <div class="m-stat-label">加入日期</div>
          </div>
        </div>
        <h4 class="panel-subtitle">📋 最近订单</h4>
        <div class="orders-list">
          <div v-for="o in store.orders.filter(x => x.member)" :key="o.id" class="order-row">
            <span class="o-pet">{{ o.petName }}</span>
            <span class="o-service">{{ o.service }}</span>
            <span class="o-datetime">{{ o.date }} {{ o.time }}</span>
            <span class="o-status" :class="o.status">{{ o.status }}</span>
            <span class="o-price">¥{{ o.price }}</span>
          </div>
          <div v-if="store.orders.filter(x=>x.member).length===0" class="empty-orders">暂无服务记录</div>
        </div>
      </div>

      <div v-else class="login-prompt reveal">
        <div class="prompt-icon">🐾</div>
        <p>登录后即可查看会员权益与订单记录</p>
        <button class="btn-login" @click="('show-login')">去登录 / 注册</button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { usePetShopStore } from '../stores/petShop'
import { computed, onMounted } from 'vue'
const store = usePetShopStore()
defineEmits(['show-login'])

const currentPlan = computed(() => store.currentUser?.plan ? plans.find(p=>p.level===store.currentUser.plan) : null)

const plans = [
  { level: '银卡会员', icon: '🥈', price: 115, original: 128, gradient: 'linear-gradient(135deg, #a8a8a8, #7a7a7a)', shadow: '0 4px 20px rgba(120,120,120,.3)', featured: false,
    features: ['首次洗护享 9 折', '生日月免费加项', '优先预约时段'] },
  { level: '金卡会员', icon: '🥇', price: 100, original: 128, gradient: 'linear-gradient(135deg, #f59e0b, #d97706)', shadow: '0 4px 24px rgba(245,158,11,.35)', featured: true,
    features: ['每次洗护享 8 折', '免费造型设计', '专属美容师服务', '生日月双倍积分'] },
  { level: '钻石会员', icon: '💎', price: 80, original: 128, gradient: 'linear-gradient(135deg, #818cf8, #6366f1)', shadow: '0 4px 24px rgba(99,102,241,.35)', featured: false,
    features: ['每次洗护享 6 折', '全年免费补救 2 次', 'VIP 专属通道', '优先服务权', '节日礼盒赠送'] },
]

function handlePlan(p) { if (!store.currentUser) emit('show-login') }

onMounted(() => {
  const reveals = document.querySelectorAll('.reveal')
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('visible') })
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' })
  reveals.forEach(el => observer.observe(el))
})
</script>

<style scoped>
.membership { position: relative; padding: 100px 40px; background: linear-gradient(180deg, var(--bg-light) 0%, var(--white) 100%); overflow: hidden; }
.mem-bg-deco { position: absolute; width: 600px; height: 600px; background: radial-gradient(circle, rgba(99,102,241,.06) 0%, transparent 70%); bottom: -200px; left: -100px; pointer-events: none; }
.membership-inner { max-width: 1100px; margin: 0 auto; position: relative; z-index: 1; }
.section-head { text-align: center; margin-bottom: 64px; }
.section-tag { display: inline-block; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 16px; font-weight: 700; }
.section-head h2 { font-size: clamp(24px, 3.5vw, 38px); font-weight: 900; color: var(--text-dark); margin: 0 0 12px; }

.plans-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 64px; }
.plan-card { border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-sm); background: var(--white); border: 1px solid var(--border); transition: var(--transition); position: relative; }
.plan-card:hover { transform: translateY(-6px); box-shadow: var(--shadow-lg); }
.plan-card--featured { border-color: rgba(99,102,241,.3); box-shadow: 0 4px 32px rgba(99,102,241,.15); }
.plan-badge { position: absolute; top: 12px; right: 12px; background: rgba(0,0,0,.7); color: #fff; font-size: 11px; padding: 4px 10px; border-radius: 50px; font-weight: 700; z-index: 2; }
.plan-header { padding: 32px 24px; text-align: center; color: #fff; position: relative; }
.plan-icon-wrap { font-size: 40px; margin-bottom: 8px; }
.plan-header h3 { font-size: 20px; font-weight: 800; margin: 0 0 8px; }
.plan-price-wrap { display: flex; align-items: baseline; justify-content: center; gap: 4px; }
.plan-price { font-size: 36px; font-weight: 900; }
.plan-unit { font-size: 13px; opacity: .8; }
.plan-original { font-size: 13px; opacity: .6; text-decoration: line-through; margin-top: 4px; }
.plan-features { list-style: none; padding: 24px; margin: 0; }
.plan-features li { font-size: 13px; color: var(--text-mid); padding: 8px 0; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 8px; }
.plan-features li:last-child { border: none; }
.feat-check { color: var(--secondary); font-weight: 800; }
.btn-plan { display: block; width: calc(100% - 40px); margin: 0 20px 20px; padding: 14px; border-radius: 50px; border: none; font-size: 15px; font-weight: 700; color: #fff; cursor: pointer; transition: var(--transition); }
.btn-plan:hover { transform: scale(1.03); }

.member-panel { background: var(--white); border-radius: var(--radius-lg); padding: 36px; box-shadow: var(--shadow-md); border: 1px solid var(--border); }
.panel-header { display: flex; align-items: center; gap: 16px; margin-bottom: 28px; }
.panel-header h3 { font-size: 20px; font-weight: 800; color: var(--text-dark); margin: 0; }
.member-level-badge { padding: 6px 16px; border-radius: 50px; font-size: 13px; font-weight: 700; color: #fff; }
.member-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 32px; }
.m-stat { text-align: center; background: var(--bg-light); border-radius: var(--radius-md); padding: 20px; }
.m-stat-num { font-size: 24px; font-weight: 900; color: var(--text-dark); }
.m-stat-label { font-size: 12px; color: var(--text-light); margin-top: 4px; }
.panel-subtitle { font-size: 16px; font-weight: 700; color: var(--text-dark); margin: 0 0 16px; }
.orders-list { display: flex; flex-direction: column; gap: 10px; }
.order-row { display: grid; grid-template-columns: 1fr 1.5fr 1fr 1fr 0.8fr; gap: 12px; padding: 14px 16px; background: var(--bg-light); border-radius: var(--radius-sm); font-size: 13px; align-items: center; }
.o-status { padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 700; text-align: center; }
.o-status.已完成 { background: #d8f3dc; color: #2d6a4f; }
.o-status.预约中 { background: #fef3c7; color: #d97706; }
.o-status.待服务 { background: #dbeafe; color: #2563eb; }
.o-price { font-weight: 800; color: var(--primary); }
.empty-orders { text-align: center; color: var(--text-light); padding: 24px; font-size: 14px; }

.login-prompt { text-align: center; padding: 60px 40px; background: var(--white); border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); border: 1px solid var(--border); }
.prompt-icon { font-size: 56px; margin-bottom: 16px; }
.login-prompt p { color: var(--text-mid); margin: 0 0 24px; font-size: 15px; }
.btn-login { background: linear-gradient(135deg, #6366f1, #4f46e5); color: #fff; padding: 14px 36px; border-radius: 50px; border: none; font-size: 15px; font-weight: 700; cursor: pointer; transition: var(--transition); box-shadow: 0 4px 20px rgba(99,102,241,.3); }
.btn-login:hover { transform: translateY(-2px); box-shadow: 0 6px 28px rgba(99,102,241,.4); }

@media (max-width: 900px) {
  .membership { padding: 80px 20px; }
  .plans-grid { grid-template-columns: 1fr; max-width: 400px; margin-left: auto; margin-right: auto; }
  .member-stats { grid-template-columns: repeat(2, 1fr); }
  .order-row { grid-template-columns: 1fr 1fr; }
}
</style>
