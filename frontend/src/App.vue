<template>
  <div class="app" :class="{ 'page-loaded': pageLoaded }">
    <Navbar ref="navbarRef" @nav="handleNav" />

    <!-- 登录弹窗 -->
    <div v-if="showLoginModal" class="modal-overlay" @click.self="showLoginModal=false">
      <div class="modal">
        <div class="modal-close" @click="showLoginModal=false">✕</div>
        <div class="modal-icon">🐾</div>
        <h3>登录 / 注册</h3>
        <p class="modal-hint">登录后即可查看会员权益与订单记录</p>
        <input v-model="loginForm.name" placeholder="您的姓名" />
        <input v-model="loginForm.phone" type="tel" placeholder="手机号" />
        <input v-model="loginForm.password" type="password" placeholder="设置密码（可选）" />
        <button class="btn-modal" @click="doLogin">确认登录</button>
        <button class="btn-close" @click="showLoginModal=false">取消</button>
      </div>
    </div>

    <main>
      <template v-if="page === 'home'">
        <HeroBanner @nav="handleNav" />
        <ServicesSection @nav="handleNav" @book="openBooking" />
        <AboutSection />
        <TestimonialsSection />
        <GallerySection />
      </template>
      <template v-else-if="page === 'services'">
        <ServicesSection @nav="handleNav" @book="openBooking" />
        <AboutSection />
        <TestimonialsSection />
      </template>
      <template v-else-if="page === 'booking'">
        <BookingSection />
      </template>
      <template v-else-if="page === 'membership'">
        <MembershipSection @show-login="showLoginModal=true" />
      </template>
      <template v-else-if="page === 'about'">
        <AboutSection />
        <GallerySection />
        <TestimonialsSection />
      </template>
    </main>

    <Footer @nav="handleNav" />

    <!-- 回到顶部 -->
    <button v-show="showScrollTop" class="scroll-top" @click="scrollToTop" title="回到顶部">↑</button>
    <!-- WhatsApp 浮动按钮 -->
    <a href="#" class="float-btn" title="联系我们">💬</a>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { usePetShopStore } from './stores/petShop'
import Navbar from './components/Navbar.vue'
import HeroBanner from './components/HeroBanner.vue'
import ServicesSection from './components/services.vue'
import AboutSection from './components/about.vue'
import BookingSection from './components/booking.vue'
import MembershipSection from './components/membership.vue'
import TestimonialsSection from './components/testimonials.vue'
import GallerySection from './components/gallery.vue'
import Footer from './components/footer.vue'

const store = usePetShopStore()
const navbarRef = ref(null)
const page = ref('home')
const pageLoaded = ref(false)
const showLoginModal = ref(false)
const showScrollTop = ref(false)
const loginForm = ref({ name: '', phone: '', password: '' })

function handleNav(p) { page.value = p }
function openBooking(service) { page.value = 'booking' }
function doLogin() {
  if (!loginForm.value.name || !loginForm.value.phone) return
  store.login({ name: loginForm.value.name, phone: loginForm.value.phone, balance: 0, totalSpent: 0, member: false, plan: '银卡会员' })
  showLoginModal.value = false
  page.value = 'membership'
}
function scrollToTop() { window.scrollTo({ top: 0, behavior: 'smooth' }) }

function handleScroll() { showScrollTop.value = window.scrollY > 600 }

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  // 页面首次加载完成后，标记为已加载，触发 reveal 动画显示
  setTimeout(() => { pageLoaded.value = true }, 100)
})
onUnmounted(() => { window.removeEventListener('scroll', handleScroll) })
</script>

<style scoped>
.app { font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; color: var(--text-dark); min-height: 100vh; display: flex; flex-direction: column; background: var(--bg-warm); }
main { flex: 1; }

/* 弹窗 */
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,.5); backdrop-filter: blur(4px); display: flex; align-items: center; justify-content: center; z-index: 200; animation: scaleIn .25s ease; }
.modal { background: #fff; border-radius: 20px; padding: 40px; width: 420px; max-width: 92vw; box-shadow: 0 24px 64px rgba(0,0,0,.2); position: relative; }
.modal-close { position: absolute; top: 16px; right: 16px; width: 32px; height: 32px; background: var(--bg-light); border: none; border-radius: 50%; font-size: 14px; cursor: pointer; display: flex; align-items: center; justify-content: center; color: var(--text-mid); transition: var(--transition); }
.modal-close:hover { background: #fee; color: #c0392b; }
.modal-icon { font-size: 48px; text-align: center; margin-bottom: 8px; }
.modal h3 { margin: 0 0 8px; font-size: 22px; color: var(--text-dark); text-align: center; font-weight: 800; }
.modal-hint { font-size: 13px; color: var(--text-light); text-align: center; margin: 0 0 24px; }
.modal input { width: 100%; padding: 14px 16px; border: 1px solid var(--border); border-radius: 12px; font-size: 15px; margin-bottom: 14px; box-sizing: border-box; outline: none; transition: var(--transition); background: var(--bg-warm); }
.modal input:focus { border-color: var(--primary); background: #fff; box-shadow: 0 0 0 3px rgba(255,127,80,.1); }
.btn-modal { width: 100%; padding: 16px; background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: #fff; border: none; border-radius: 50px; font-size: 15px; font-weight: 700; cursor: pointer; margin-bottom: 10px; box-shadow: 0 4px 16px rgba(255,127,80,.3); transition: var(--transition); }
.btn-modal:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(255,127,80,.4); }
.btn-close { width: 100%; padding: 12px; background: transparent; color: var(--text-light); border: none; font-size: 14px; cursor: pointer; }
.btn-close:hover { color: var(--text-mid); }

.scroll-top { animation: scaleIn .2s ease; }
</style>
