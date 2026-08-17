import { defineStore } from 'pinia'
import { ref } from 'vue'

// API 基础地址：本地默认走相对路径（与后端同域）；部署到独立后端时设置 VITE_API_BASE
const API_BASE = import.meta.env.VITE_API_BASE || ''

export const usePetShopStore = defineStore('petShop', {
  state: () => ({
    currentUser: null,
    customers: [
      { id: 1, name: '张三', phone: '138****1234', balance: 500, member: true, joinDate: '2025-03-15', plan: '金卡会员' },
      { id: 2, name: '李四', phone: '139****5678', balance: 200, member: true, joinDate: '2025-07-20', plan: '银卡会员' },
      { id: 3, name: '王五', phone: '137****9999', balance: 0, member: false, joinDate: '2026-01-10', plan: null },
    ],
    services: [
      { id: 1, name: '标准沐浴SPA', price: 98, duration: '45分钟', desc: '专业洗护，含护毛素护理，适合日常清洁', popular: true, icon: '🛁', image: 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=600&h=400&fit=crop&q=80', features: ['深层清洁', '护毛素护理', '芳香除臭'] },
      { id: 2, name: '深层除虫护理', price: 168, duration: '60分钟', desc: '彻底除螨除虫，呵护宠物皮肤健康', popular: false, icon: '🦠', image: 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=600&h=400&fit=crop&q=80', features: ['除螨除虫', '皮肤护理', '抑菌防护'] },
      { id: 3, name: '造型修剪', price: 198, duration: '90分钟', desc: '专业美容师精心设计时尚造型', popular: true, icon: '✂️', image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=600&h=400&fit=crop&q=80', features: ['品种造型', '时尚修剪', '颜值提升'] },
      { id: 4, name: '深度除菌护理', price: 258, duration: '120分钟', desc: 'SPA级深层清洁，除菌抑菌，适合敏感肌肤', popular: false, icon: '🌿', image: 'https://images.unsplash.com/photo-1585409677983-0f6c41ca9c3b?w=600&h=400&fit=crop&q=80', features: ['SPA级清洁', '除菌抑菌', '敏感肌适用'] },
      { id: 5, name: '指甲护理', price: 38, duration: '15分钟', desc: '专业修剪打磨，防止抓伤家人', popular: false, icon: '💅', image: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=600&h=400&fit=crop&q=80', features: ['专业修剪', '打磨光滑', '防抓伤人'] },
      { id: 6, name: '耳朵清洁', price: 48, duration: '15分钟', desc: '专业清耳护理，预防耳朵炎症', popular: false, icon: '👂', image: 'https://images.unsplash.com/photo-1592194996308-7b43878e84a6?w=600&h=400&fit=crop&q=80', features: ['深度清洁', '预防炎症', '温和护理'] },
    ],
    orders: [
      { id: 1, petName: '豆豆', service: '标准沐浴SPA', date: '2026-07-10', time: '10:00', price: 128, status: '已完成', member: true },
      { id: 2, petName: '雪球', service: '造型修剪', date: '2026-07-08', time: '14:30', price: 198, status: '预约中', member: true },
      { id: 3, petName: '旺财', service: '深层除菌护理', date: '2026-07-05', time: '09:00', price: 258, status: '待服务', member: true },
    ],
  }),
  actions: {
    login(user) { this.currentUser = { ...user }; if (!this.currentUser.plan) this.currentUser.plan = '银卡会员' },
    logout() { this.currentUser = null; },
    addCustomer(customer) { this.customers.unshift(customer); },
    async submitBooking(booking) {
      const res = await fetch(`${API_BASE}/api/booking/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(booking),
      })
      return await res.json()
    },
  }
})
