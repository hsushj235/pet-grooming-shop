<template>
  <section class="admin">
    <div class="admin-inner">
      <h2>📊 数据看板</h2>
      <div class="stats-grid">
        <div class="stat-card"><div class="stat-num">{{ orders.length }}</div><div class="stat-label">总订单</div></div>
        <div class="stat-card"><div class="stat-num">{{ customers.length }}</div><div class="stat-label">客户数</div></div>
        <div class="stat-card"><div class="stat-num">¥{{ totalRevenue }}</div><div class="stat-label">总收入</div></div>
        <div class="stat-card"><div class="stat-num">{{ pendingOrders }}</div><div class="stat-label">待处理</div></div>
      </div>
      <div class="panel"><h3>📋 订单管理</h3>
        <table><thead><tr><th>ID</th><th>宠物</th><th>服务</th><th>日期</th><th>价格</th><th>状态</th></tr></thead>
        <tbody><tr v-for="o in orders" :key="o.id"><td>#{{ o.id }}</td><td>{{ o.petName }}</td><td>{{ o.service }}</td><td>{{ o.date }}</td><td>¥{{ o.price }}</td><td><span class="badge" :class="o.status">{{ o.status }}</span></td></tr></tbody>
        </table>
      </div>
      <div class="panel"><h3>👥 客户管理</h3>
        <table><thead><tr><th>ID</th><th>姓名</th><th>手机</th><th>余额</th><th>会员</th><th>加入日期</th></tr></thead>
        <tbody><tr v-for="cu in customers" :key="cu.id"><td>#{{ cu.id }}</td><td>{{ cu.name }}</td><td>{{ cu.phone }}</td><td>¥{{ cu.balance }}</td><td><span v-if="cu.member" class="badge member">是</span><span v-else class="badge">否</span></td><td>{{ cu.joinDate }}</td></tr></tbody>
        </table>
      </div>
    </div>
  </section>
</template>
<script setup>
import { computed } from 'vue'
import { usePetShopStore } from '../stores/petShop'
const store = usePetShopStore()
const orders = computed(() => store.orders)
const customers = computed(() => store.customers)
const totalRevenue = computed(() => store.orders.reduce((sum, o) => sum + o.price, 0))
const pendingOrders = computed(() => store.orders.filter(o => o.status !== '已完成').length)
</script>
<style scoped>
.admin { padding: 40px 24px; background: #f0f4f8; min-height: 60vh; }
.admin-inner { max-width: 1100px; margin: 0 auto; }
.admin h2 { font-size: 24px; color: #1e293b; margin: 0 0 24px; }
.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 32px; }
.stat-card { background: #fff; border-radius: 12px; padding: 24px; text-align: center; box-shadow: 0 1px 4px rgba(0,0,0,.06); }
.stat-num { font-size: 32px; font-weight: 800; color: #2d6a4f; }
.stat-label { font-size: 14px; color: #888; margin-top: 4px; }
.panel { background: #fff; border-radius: 12px; padding: 24px; margin-bottom: 24px; box-shadow: 0 1px 4px rgba(0,0,0,.06); }
.panel h3 { font-size: 18px; color: #333; margin: 0 0 16px; }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 12px 16px; text-align: left; border-bottom: 1px solid #f0f0f0; font-size: 14px; }
th { background: #f8faf9; font-weight: 600; color: #555; }
.badge { display: inline-block; padding: 3px 10px; border-radius: 8px; font-size: 12px; font-weight: 600; }
.badge.已完成 { background: #d8f3dc; color: #2d6a4f; }
.badge.预约中 { background: #fef3c7; color: #d97706; }
.badge.待服务 { background: #dbeafe; color: #2563eb; }
.badge.member { background: #d8f3dc; color: #2d6a4f; }
</style>