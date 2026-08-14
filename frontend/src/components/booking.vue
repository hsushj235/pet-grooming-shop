<template>
  <section class="booking">
    <div class="booking-bg-deco"></div>
    <div class="booking-inner">
      <div class="section-head reveal">
        <span class="section-tag" style="color:var(--primary)">BOOKING</span>
        <h2>在线预约</h2>
        <p style="color:var(--text-mid)">选择服务、日期和时段，只需三步即可完成预约</p>
      </div>

      <!-- 步骤进度 -->
      <div class="stepper reveal">
        <div class="step" :class="{ active: step >= 1, completed: step > 1 }">
          <div class="step-num">1</div>
          <div class="step-label">选择宠物</div>
        </div>
        <div class="step-line" :class="{ active: step > 1 }"></div>
        <div class="step" :class="{ active: step >= 2, completed: step > 2 }">
          <div class="step-num">2</div>
          <div class="step-label">选择服务</div>
        </div>
        <div class="step-line" :class="{ active: step > 2 }"></div>
        <div class="step" :class="{ active: step >= 3 }">
          <div class="step-num">3</div>
          <div class="step-label">确认信息</div>
        </div>
      </div>

      <div class="form-card reveal reveal-delay-1">
        <!-- 步骤1：宠物信息 -->
        <template v-if="step === 1">
          <h3 class="form-title">🐾 宠物信息</h3>
          <div class="form-row">
            <div class="fg"><label>宠物姓名 *</label><input v-model="form.petName" type="text" placeholder="给毛孩子起个名字吧" /></div>
            <div class="fg"><label>宠物类型 *</label>
              <select v-model="form.petType">
                <option value="dog">🐶 狗狗</option>
                <option value="cat">🐱 猫咪</option>
                <option value="other">🐰 其他</option>
              </select>
            </div>
          </div>
          <div class="form-row">
            <div class="fg"><label>品种</label><input v-model="form.breed" type="text" placeholder="如：金毛、英短..." /></div>
            <div class="fg"><label>体重(kg)</label><input v-model="form.weight" type="number" placeholder="约多少公斤" /></div>
          </div>
          <button class="btn-next" @click="step = 2" :disabled="!form.petName">
            下一步 <span>→</span>
          </button>
        </template>

        <!-- 步骤2：选择服务 -->
        <template v-else-if="step === 2">
          <h3 class="form-title">✨ 选择服务</h3>
          <div class="service-select-grid">
            <div v-for="s in services" :key="s.id" class="svc-option" :class="{ chosen: form.service && form.service.id === s.id }" @click="form.service = s">
              <img :src="s.image" :alt="s.name" class="svc-opt-img" />
              <div class="svc-opt-body">
                <div class="svc-opt-top">
                  <span class="svc-opt-icon">{{ s.icon }}</span>
                  <strong>{{ s.name }}</strong>
                  <span class="svc-opt-price">¥{{ s.price }}</span>
                </div>
                <span class="svc-opt-desc">{{ s.desc }}</span>
                <span class="svc-opt-duration">⏱ {{ s.duration }}</span>
              </div>
              <div v-if="form.service && form.service.id === s.id" class="svc-opt-check">✓</div>
            </div>
          </div>
          <div class="form-btns">
            <button class="btn-prev" @click="step = 1">← 上一步</button>
            <button class="btn-next" @click="step = 3" :disabled="!form.service">
              下一步 <span>→</span>
            </button>
          </div>
        </template>

        <!-- 步骤3：确认信息 -->
        <template v-else-if="step === 3">
          <h3 class="form-title">📋 确认预约</h3>
          <div class="confirm-summary">
            <div class="summary-item"><span class="label">宠物</span><span class="value">{{ form.petName }}（{{ form.petType === 'dog' ? '🐶' : form.petType === 'cat' ? '🐱' : '🐰' }}）</span></div>
            <div class="summary-item"><span class="label">服务</span><span class="value">{{ form.service?.icon }} {{ form.service?.name }}</span></div>
            <div class="summary-item"><span class="label">日期</span><span class="value">{{ form.date }}</span></div>
            <div class="summary-item"><span class="label">时段</span><span class="value">{{ form.time }}</span></div>
            <div class="summary-item"><span class="label">电话</span><span class="value">{{ form.phone }}</span></div>
            <div class="summary-item total-row"><span class="label">合计金额</span><span class="value total-price">¥{{ form.service?.price || 0 }}</span></div>
          </div>
          <div class="form-row">
            <div class="fg"><label>预约日期 *</label><input v-model="form.date" type="date" /></div>
            <div class="fg"><label>预约时段 *</label>
              <select v-model="form.time">
                <option :value="null">请选择时段</option>
                <option v-for="t in timeSlots" :key="t">{{ t }}</option>
              </select>
            </div>
          </div>
          <div class="fg full"><label>主人手机号 *</label><input v-model="form.phone" type="tel" placeholder="请输入手机号" /></div>
          <div class="fg full"><label>备注信息</label><textarea v-model="form.remark" rows="2" placeholder="如有特殊需求请在此说明（如：毛发打结、皮肤敏感等）"></textarea></div>
          <div class="form-btns">
            <button class="btn-prev" @click="step = 2">← 上一步</button>
            <button class="btn-submit" :disabled="!isValid || submitting" @click="submit">
              {{ submitting ? '提交中...' : '🎉 确认预约' }}
            </button>
          </div>
          <div v-if="msg" class="msg success">{{ msg }}</div>
          <div v-else-if="err" class="msg error">{{ err }}</div>
        </template>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'
import { usePetShopStore } from '../stores/petShop'
const store = usePetShopStore()
const services = computed(() => store.services)
const step = ref(1)
const form = ref({ petName: '', petType: 'dog', breed: '', weight: '', service: null, date: '', time: null, phone: '', remark: '' })
const msg = ref('')
const err = ref('')
const submitting = ref(false)
const timeSlots = ['09:00', '09:30', '10:00', '10:30', '11:00', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00']
const isValid = computed(() => form.value.petName && form.value.service && form.value.date && form.value.time && form.value.phone)

async function submit() {
  if (!isValid.value) { err.value = '请填写完整信息'; return }
  submitting.value = true
  err.value = ''; msg.value = ''
  try {
    const payload = {
      petName: form.value.petName, petType: form.value.petType,
      service: form.value.service.name, date: form.value.date,
      time: form.value.time, phone: form.value.phone, remark: form.value.remark,
    }
    const result = await store.submitBooking(payload)
    if (result.code === 200) {
      msg.value = '🎉 预约成功！我们将短信通知您确认信息。'
      setTimeout(() => { step.value = 1; form.value = { petName:'',petType:'dog',breed:'',weight:'',service:null,date:'',time:null,phone:'',remark:'' } }, 2500)
    } else { err.value = result.msg || '提交失败，请重试' }
  } catch (e) { err.value = '网络错误，请稍后重试' }
  finally { submitting.value = false }
}
</script>

<style scoped>
.booking { position: relative; padding: 100px 40px; background: linear-gradient(135deg, var(--bg-warm) 0%, #FFF0EB 50%, var(--bg-light) 100%); overflow: hidden; }
.booking-bg-deco { position: absolute; width: 500px; height: 500px; background: radial-gradient(circle, rgba(255,127,80,.06) 0%, transparent 70%); top: -100px; right: -100px; pointer-events: none; }
.booking-inner { max-width: 760px; margin: 0 auto; position: relative; z-index: 1; }
.section-head { text-align: center; margin-bottom: 48px; }
.section-tag { display: inline-block; font-size: 11px; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 16px; font-weight: 700; }
.section-head h2 { font-size: 36px; font-weight: 900; color: var(--text-dark); margin: 0 0 12px; }

/* 步骤条 */
.stepper { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; }
.step { display: flex; flex-direction: column; align-items: center; gap: 8px; }
.step-num { width: 44px; height: 44px; border-radius: 50%; background: var(--white); border: 2px solid var(--border); display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 800; color: var(--text-light); transition: var(--transition); }
.step.active .step-num { background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: #fff; border-color: var(--primary); box-shadow: 0 4px 16px rgba(255,127,80,.3); }
.step.completed .step-num { background: var(--secondary); color: #fff; border-color: var(--secondary); }
.step-label { font-size: 13px; color: var(--text-light); font-weight: 600; }
.step.active .step-label { color: var(--primary); }
.step-line { flex: 1; height: 2px; background: var(--border); margin: 0 12px; margin-bottom: 28px; transition: var(--transition); }
.step-line.active { background: linear-gradient(90deg, var(--secondary), var(--primary)); }

.form-card { background: var(--white); border-radius: var(--radius-lg); padding: 40px; box-shadow: var(--shadow-md); border: 1px solid var(--border); }
.form-title { font-size: 18px; font-weight: 800; color: var(--text-dark); margin: 0 0 28px; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px; }
.fg { display: flex; flex-direction: column; gap: 8px; }
.fg.full { grid-column: 1 / -1; }
label { font-size: 13px; font-weight: 600; color: var(--text-mid); letter-spacing: .3px; }
input, select, textarea { border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 14px 16px; font-size: 15px; transition: var(--transition); outline: none; background: var(--bg-warm); font-family: inherit; }
input:focus, select:focus, textarea:focus { border-color: var(--primary); background: #fff; box-shadow: 0 0 0 3px rgba(255,127,80,.1); }

/* 服务选择网格 */
.service-select-grid { display: grid; grid-template-columns: 1fr; gap: 12px; margin-bottom: 24px; }
.svc-option { display: flex; gap: 16px; align-items: center; padding: 14px; border-radius: var(--radius-md); border: 2px solid var(--border); cursor: pointer; transition: var(--transition); background: var(--bg-warm); }
.svc-option:hover { border-color: rgba(255,127,80,.3); background: #fff; }
.svc-option.chosen { border-color: var(--primary); background: rgba(255,127,80,.04); box-shadow: 0 2px 12px rgba(255,127,80,.12); }
.svc-opt-img { width: 72px; height: 72px; border-radius: 12px; object-fit: cover; flex-shrink: 0; }
.svc-opt-body { flex: 1; min-width: 0; }
.svc-opt-top { display: flex; align-items: center; gap: 8px; margin-bottom: 4px; flex-wrap: wrap; }
.svc-opt-icon { font-size: 20px; }
.svc-opt-top strong { font-size: 15px; color: var(--text-dark); font-weight: 700; }
.svc-opt-price { font-size: 16px; font-weight: 800; color: var(--primary); margin-left: auto; }
.svc-opt-desc { font-size: 12px; color: var(--text-light); display: block; margin-bottom: 4px; }
.svc-opt-duration { font-size: 11px; color: var(--text-light); }
.svc-opt-check { width: 28px; height: 28px; background: var(--primary); color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 800; flex-shrink: 0; }

/* 按钮 */
.form-btns { display: flex; gap: 16px; margin-top: 8px; }
.btn-next, .btn-submit { flex: 1; padding: 16px; background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: #fff; border: none; border-radius: 50px; font-size: 15px; font-weight: 700; cursor: pointer; transition: var(--transition); box-shadow: 0 4px 20px rgba(255,127,80,.3); }
.btn-next:hover:not(:disabled), .btn-submit:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 6px 28px rgba(255,127,80,.4); }
.btn-next:disabled, .btn-submit:disabled { background: #ccc; cursor: not-allowed; box-shadow: none; }
.btn-prev { padding: 16px 28px; background: var(--bg-light); color: var(--text-mid); border: 1px solid var(--border); border-radius: 50px; font-size: 15px; font-weight: 600; cursor: pointer; transition: var(--transition); white-space: nowrap; }
.btn-prev:hover { background: var(--white); color: var(--text-dark); }

/* 确认摘要 */
.confirm-summary { background: var(--bg-light); border-radius: var(--radius-md); padding: 20px; margin-bottom: 24px; border: 1px solid var(--border); }
.summary-item { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid var(--border); font-size: 14px; }
.summary-item:last-child { border: none; }
.summary-item .label { color: var(--text-light); }
.summary-item .value { color: var(--text-dark); font-weight: 600; }
.total-row .label { font-weight: 700; color: var(--text-dark); }
.total-price { font-size: 22px; font-weight: 900; color: var(--primary); }

.msg { text-align: center; margin-top: 16px; font-size: 14px; padding: 12px; border-radius: var(--radius-sm); }
.msg.success { background: #e8f5e9; color: #2e7d32; }
.msg.error { background: #fff3e0; color: #c0392b; }

@media (max-width: 600px) {
  .booking { padding: 80px 20px; }
  .form-card { padding: 24px; }
  .form-row { grid-template-columns: 1fr; }
  .form-btns { flex-direction: column; }
  .stepper { gap: 0; }
  .step-label { font-size: 11px; }
}
</style>
