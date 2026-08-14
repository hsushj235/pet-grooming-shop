<template>
  <nav class="navbar" :class="{ 'navbar--scrolled': scrolled }">
    <div class="nav-inner">
      <div class="logo" @click="go('home')">
        <svg class="logo-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="46" fill="#FF7F50"/>
          <path d="M50,76 C32,76 24,60 28,46 C32,34 44,28 50,24 C56,28 68,34 72,46 C76,60 68,76 50,76Z" fill="#fff"/>
          <ellipse cx="28" cy="28" rx="10" ry="13" fill="#fff" transform="rotate(-20,28,28)"/>
          <ellipse cx="44" cy="16" rx="9" ry="12" fill="#fff" transform="rotate(-8,44,16)"/>
          <ellipse cx="56" cy="16" rx="9" ry="12" fill="#fff" transform="rotate(8,56,16)"/>
          <ellipse cx="72" cy="28" rx="10" ry="13" fill="#fff" transform="rotate(20,72,28)"/>
        </svg>
        <span class="logo-text">萌宠洗护</span>
      </div>
      <div class="nav-links">
        <a href="#" @click.prevent="go('home')" :class="{ 'nav-active': page === 'home' }">首页</a>
        <a href="#" @click.prevent="go('services')" :class="{ 'nav-active': page === 'services' }">服务项目</a>
        <a href="#" @click.prevent="go('booking')" :class="{ 'nav-active': page === 'booking' }">在线预约</a>
        <a href="#" @click.prevent="go('membership')" :class="{ 'nav-active': page === 'membership' }">会员中心</a>
        <a href="#" @click.prevent="go('about')" :class="{ 'nav-active': page === 'about' }">关于我们</a>
      </div>
      <div class="nav-right">
        <template v-if="store.currentUser">
          <span class="member-badge">{{ store.currentUser.name }}</span>
          <button class="btn-logout" @click="store.logout()">退出</button>
        </template>
        <button v-else class="btn-login" @click="go('membership')">登录 / 注册</button>
      </div>
      <button class="hamburger" @click="mobileOpen = !mobileOpen">
        <span></span><span></span><span></span>
      </button>
    </div>
    <div v-if="mobileOpen" class="mobile-menu">
      <a href="#" @click.prevent="go('home'); mobileOpen=false">首页</a>
      <a href="#" @click.prevent="go('services'); mobileOpen=false">服务项目</a>
      <a href="#" @click.prevent="go('booking'); mobileOpen=false">在线预约</a>
      <a href="#" @click.prevent="go('membership'); mobileOpen=false">会员中心</a>
      <a href="#" @click.prevent="go('about'); mobileOpen=false">关于我们</a>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { usePetShopStore } from '../stores/petShop'
const store = usePetShopStore()
const emit = defineEmits(['nav'])
const page = ref('home')
const scrolled = ref(false)
const mobileOpen = ref(false)

defineExpose({ setPage: p => { page.value = p; mobileOpen.value = false } })

function go(p) { page.value = p; mobileOpen.value = false; emit('nav', p) }

function handleScroll() {
  scrolled.value = window.scrollY > 50
}

onMounted(() => { window.addEventListener('scroll', handleScroll) })
onUnmounted(() => { window.removeEventListener('scroll', handleScroll) })
</script>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255,255,255,.96);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  transition: var(--transition);
  box-shadow: var(--shadow-sm);
}
.nav-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  padding: 0 40px;
  height: 72px;
}
.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 19px;
  font-weight: 800;
  color: var(--text-dark);
  cursor: pointer;
  letter-spacing: .5px;
}
.logo-icon { width: 42px; height: 42px; flex-shrink: 0; }
.nav-links {
  flex: 1;
  display: flex;
  justify-content: center;
  gap: 8px;
  margin: 0 40px;
}
.nav-links a {
  text-decoration: none;
  color: var(--text-mid);
  font-size: 14px;
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 50px;
  transition: var(--transition);
}
.nav-links a:hover, .nav-links a.nav-active {
  color: var(--primary);
  background: rgba(255,127,80,.08);
}
.nav-right { display: flex; align-items: center; gap: 12px; }
.member-badge {
  background: linear-gradient(135deg, rgba(255,127,80,.1), rgba(78,205,196,.1));
  color: var(--primary);
  padding: 7px 16px;
  border-radius: 50px;
  font-size: 13px;
  font-weight: 600;
}
button { border: none; font-size: 13px; font-weight: 600; border-radius: 50px; transition: var(--transition); }
.btn-login { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: #fff; padding: 10px 24px; box-shadow: 0 2px 12px rgba(255,127,80,.3); }
.btn-login:hover { transform: translateY(-1px); box-shadow: 0 4px 20px rgba(255,127,80,.4); }
.btn-logout { background: var(--bg-light); color: var(--text-mid); padding: 10px 24px; }
.btn-logout:hover { background: #fee; color: var(--primary-dark); }

.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
  margin-left: auto;
}
.hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text-dark);
  border-radius: 2px;
  transition: var(--transition);
}

.mobile-menu {
  display: none;
  flex-direction: column;
  background: rgba(255,255,255,.98);
  backdrop-filter: blur(20px);
  padding: 16px 40px 24px;
  border-top: 1px solid var(--border);
  gap: 4px;
}
.mobile-menu a {
  padding: 12px 16px;
  color: var(--text-mid);
  font-size: 15px;
  font-weight: 500;
  border-radius: var(--radius-sm);
  transition: var(--transition);
}
.mobile-menu a:hover { background: rgba(255,127,80,.08); color: var(--primary); }

@media (max-width: 900px) {
  .nav-links { display: none; }
  .hamburger { display: flex; }
  .navbar { padding: 0; }
  .nav-inner { padding: 0 20px; }
  .mobile-menu { padding: 16px 20px 24px; }
}
</style>
