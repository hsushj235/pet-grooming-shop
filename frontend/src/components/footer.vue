<template>
  <footer class="footer">
    <div class="footer-top">
      <div class="footer-inner">
        <div class="footer-col footer-col--brand">
          <div class="footer-logo">
            <svg class="footer-logo-icon" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
              <circle cx="50" cy="50" r="46" fill="#FF7F50"/>
              <path d="M50,76 C32,76 24,60 28,46 C32,34 44,28 50,24 C56,28 68,34 72,46 C76,60 68,76 50,76Z" fill="#fff"/>
              <ellipse cx="28" cy="28" rx="10" ry="13" fill="#fff" transform="rotate(-20,28,28)"/>
              <ellipse cx="44" cy="16" rx="9" ry="12" fill="#fff" transform="rotate(-8,44,16)"/>
              <ellipse cx="56" cy="16" rx="9" ry="12" fill="#fff" transform="rotate(8,56,16)"/>
              <ellipse cx="72" cy="28" rx="10" ry="13" fill="#fff" transform="rotate(20,72,28)"/>
            </svg>
            <span>萌宠洗护</span>
          </div>
          <p class="footer-slogan">专业宠物洗护，给毛孩子最好的照顾</p>
          <p class="footer-desc">我们致力于为每一只毛孩子提供安全、舒适、高品质的洗护体验，让宠物和家人都满意。</p>
          <div class="footer-social">
            <a href="#" class="social-link" title="微信">💬</a>
            <a href="#" class="social-link" title="抖音">📱</a>
            <a href="#" class="social-link" title="小红书">📕</a>
            <a href="#" class="social-link" title="微博">🐦</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>服务项目</h4>
          <a href="#">标准沐浴SPA</a>
          <a href="#">深层除虫护理</a>
          <a href="#">造型修剪</a>
          <a href="#">深度除菌护理</a>
          <a href="#">指甲护理</a>
          <a href="#">耳朵清洁</a>
        </div>
        <div class="footer-col">
          <h4>快速链接</h4>
          <a href="#" @click.prevent="('nav', 'home')">首页</a>
          <a href="#" @click.prevent="('nav', 'services')">服务项目</a>
          <a href="#" @click.prevent="('nav', 'booking')">在线预约</a>
          <a href="#" @click.prevent="('nav', 'membership')">会员中心</a>
          <a href="#" @click.prevent="('nav', 'about')">关于我们</a>
        </div>
        <div class="footer-col">
          <h4>联系我们</h4>
          <p class="contact-item">📞 400-888-8888</p>
          <p class="contact-item">📍 某市某区宠物街88号</p>
          <p class="contact-item">🕐 营业时间：09:00 - 19:00</p>
          <p class="contact-item">📧 contact@mengchong.com</p>
          <div class="footer-map-placeholder">
            <span>🗺️ 点击查看地图</span>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-inner">
        <p class="copyright">© 2021-2026 萌宠洗护 版权所有</p>
        <p class="links">
          <a href="#">隐私政策</a>
          <a href="#">服务条款</a>
          <a href="#">网站地图</a>
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
defineEmits(['nav'])
</script>

<style scoped>
.footer { background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%); color: #a0aec0; }
.footer-top { padding: 72px 40px 48px; }
.footer-inner { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1.6fr 1fr 1fr 1.3fr; gap: 48px; }
.footer-col h4 { font-size: 13px; color: #fff; margin: 0 0 20px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; }
.footer-col--brand .footer-logo { display: flex; align-items: center; gap: 10px; font-size: 20px; font-weight: 800; color: #fff; margin-bottom: 12px; }
.footer-logo-icon { width: 36px; height: 36px; flex-shrink: 0; }
.footer-slogan { font-size: 15px; color: var(--primary); font-weight: 600; margin: 0 0 12px; }
.footer-desc { font-size: 13px; color: #718096; line-height: 1.8; margin: 0 0 20px; }
.footer-social { display: flex; gap: 10px; }
.social-link { width: 40px; height: 40px; background: rgba(255,255,255,.08); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; transition: var(--transition); }
.social-link:hover { background: var(--primary); transform: translateY(-3px); }
.footer-col a { display: block; font-size: 14px; color: #718096; text-decoration: none; padding: 6px 0; transition: color .2s; }
.footer-col a:hover { color: var(--primary); }
.contact-item { font-size: 14px; color: #718096; margin: 8px 0; line-height: 1.6; }
.footer-map-placeholder { margin-top: 16px; background: rgba(255,255,255,.05); border-radius: var(--radius-sm); padding: 16px; text-align: center; font-size: 13px; color: #4a5568; cursor: pointer; transition: var(--transition); border: 1px dashed rgba(255,255,255,.1); }
.footer-map-placeholder:hover { border-color: var(--primary); color: var(--primary); }
.footer-bottom { border-top: 1px solid rgba(255,255,255,.08); padding: 24px 40px; }
.footer-inner { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; }
.copyright { font-size: 13px; color: #4a5568; margin: 0; }
.links { display: flex; gap: 24px; }
.links a { font-size: 13px; color: #4a5568; text-decoration: none; transition: color .2s; }
.links a:hover { color: var(--primary); }

@media (max-width: 900px) {
  .footer-top { padding: 48px 20px 32px; }
  .footer-inner { grid-template-columns: 1fr 1fr; gap: 32px; }
  .footer-col--brand { grid-column: 1 / -1; }
  .footer-bottom { padding: 20px; }
  .footer-inner { flex-direction: column; text-align: center; }
  .links { justify-content: center; }
}
@media (max-width: 500px) {
  .footer-inner { grid-template-columns: 1fr; }
}
</style>
