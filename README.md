# 萌宠洗护店网站（Pet Grooming Shop）

基于 **Django + Vue 3** 的宠物洗护店网站。前台面向客户展示服务与在线预约，后台使用 django-simpleui 进行管理。

- **后端**：Django 6.1 + SQLite，语言 `zh-hans`，时区 `Asia/Shanghai`
- **前端**：Vue 3 + Vite（Pinia 状态管理），位于 `frontend/`
- **后台**：django-simpleui 主题，已中文化
- **数据库**：SQLite 3

---

## 目录结构

```
D:\项目1\
├── README.md                 # 本文件（项目说明 + 部署指南）
├── AGENTS.md                 # 项目协作说明
├── manage.py                 # Django 管理入口
├── myproject/                # Django 项目配置
│   ├── settings.py           # 全局配置（已注册 core 应用、静态资源等）
│   ├── urls.py               # 路由：/admin/、/ 与 /api/booking/
│   ├── wsgi.py
│   └── asgi.py
├── core/                     # Django 业务应用
│   ├── models.py             # 核心数据模型（Contract 预约记录）
│   ├── views.py              # 预约接口（提交/查询）
│   ├── admin.py              # simpleui 后台注册
│   ├── apps.py
│   └── migrations/
│       ├── 0001_initial.py
│       └── __init__.py
├── frontend/                 # Vue 3 前端源码
│   ├── src/
│   │   ├── App.vue           # 根组件
│   │   ├── main.js           # 入口
│   │   ├── style.css         # 全局样式
│   │   ├── components/       # Navbar、HeroBanner、services、about、booking、
│   │   │                     # membership、gallery、testimonials、footer、admin 等组件
│   │   └── stores/
│   │       └── petShop.js    # Pinia 状态（服务数据、会员信息等）
│   ├── dist/                 # Vite 构建产物，由 Django 托管
│   ├── public/               # 静态公共资源（图片、图标等）
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── staticfiles/              # collectstatic 输出目录
├── venv/                     # Python 虚拟环境（不入库）
└── db.sqlite3                # SQLite 数据库（不入库）
```

---

## 本地快速启动

### 1. 后端（Django）

```powershell
# 激活虚拟环境
. D:\项目1\venv\Scripts\Activate.ps1

# 安装依赖（首次）
pip install -r requirements.txt   # 若已生成依赖清单

# 数据库迁移
cd D:\项目1
python manage.py makemigrations
python manage.py migrate

# 创建超级管理员（后台登录用）
python manage.py createsuperuser

# 启动开发服务器
python manage.py runserver 0.0.0.0:8000
```

### 2. 前端（Vue 3）

```powershell
cd D:\项目1\frontend
npm install          # 首次安装依赖
npm run dev          # 本地开发服务器（热更新）
npm run build        # 构建生产版本（产物输出到 dist/）
```

> **重要**：每次修改前端代码后，需运行 `npm run build` 重新构建，然后重启 Django 服务器使新静态资源生效。

### 3. 访问地址

| 入口 | 地址 |
|------|------|
| 前台首页 | <http://127.0.0.1:8000/> |
| 后台管理 | <http://127.0.0.1:8000/admin/> |

> 后台默认账号：`n167729` / `123456`

---

## 核心功能接口

### 预约提交接口 `POST /api/booking/`

接收 JSON 请求体（已做 CSRF 豁免）：

```json
{
  "petName": "旺财",
  "petType": "dog",
  "service": "基础洗护",
  "date": "2026-08-18",
  "time": "10:00-11:00",
  "phone": "13800000000",
  "remark": "麻烦剪短一些"
}
```

成功返回：

```json
{ "code": 200, "msg": "预约成功！我们将短信通知您确认信息。", "data": { "id": 1, ... } }
```

必填字段：`petName`、`service`、`date`、`time`、`phone`；缺失时返回 `code: 400` 与错误提示。[cite:ada372a5-1]

### 预约列表接口 `GET /api/bookings/`

返回所有预约记录（用于后台管理页面），包括 `petName`、`service`、`date`、`time`、`phone`、`remark`、`created_at` 等字段。[cite:ada372a5-2]

---

## 数据模型

### Contract（预约记录）

| 字段 | 类型 | 说明 |
|------|------|------|
| `pet_name` | CharField | 宠物姓名 |
| `pet_type` | CharField | 宠物类型（dog 狗狗 / cat 猫咪 / other 其他） |
| `service` | CharField | 服务项目 |
| `date` | DateField | 预约日期 |
| `time` | CharField | 预约时段 |
| `phone` | CharField | 主人手机号 |
| `remark` | TextField | 备注信息（可空） |
| `created_at` | DateTimeField | 创建时间（自动） |

表名：`contract`；verbose_name：预约记录。

---

## 主要功能模块（规划 / 已落地）

1. **首页** — Navbar 毛玻璃导航、HeroBanner 轮播 banner、服务介绍、门店信息、访客数滚动统计
2. **服务页** — 洗护套餐、美容项目、价格展示、预约流程步骤
3. **预约系统** — 分步预约表单、服务图片预览、提交到 `/api/booking/`
4. **会员系统** — 会员等级渐变卡片、储值面板、订单记录美化
5. **后台管理** — simpleui 订单/预约管理、客户管理等（`/admin/`）

此外还包含 **about（团队介绍 + 6 步洗护流程）**、**testimonials（用户评价）**、**gallery（瀑布流萌宠照片墙）**、**footer（深色渐变页脚）** 等页面组件。

---

## 技术栈与依赖

| 层 | 技术 |
|----|------|
| 后端框架 | Django 6.1 |
| 前端框架 | Vue 3（Vite 构建，Pinia 状态管理） |
| 后台 UI | django-simpleui（中文化） |
| 数据库 | SQLite 3 |
| Python | 3.14+ |
| Node.js | 24+ |

---

## 部署指南

> 本部分参考前后端分离部署的通用思路（前端 / API / 数据库分三部分部署）。本项目为 Django 托管 Vite 构建产物的一体化结构，可在「一体化部署」与「前后端分离」两种模式中选择。

### 方案 A：单服务器一体化部署（推荐，结构最简单）

本项目前端构建产物由 Django 直接托管，因此可直接作为单一 Web 服务部署到一台服务器。

1. **构建前端**：
   ```powershell
   cd D:\项目1\frontend
   npm run build          # 产物输出到 frontend/dist/
   ```
2. **关闭 DEBUG 并配置安全项**（`myproject/settings.py`）：
   - `DEBUG = False`
   - 设置真实的 `SECRET_KEY`
   - `ALLOWED_HOSTS = ['你的域名或IP']`
3. **收集静态文件**：
   ```powershell
   python manage.py collectstatic
   ```
4. **迁移数据库**：
   ```powershell
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. **启用生产级 WSGI 服务器**（如 Gunicorn）：
   ```powershell
   pip install gunicorn
   gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
   ```
6. **反向代理**：用 **Nginx** 将 80/443 端口转发到 8000，并托管 `staticfiles/` 与 `frontend/dist/assets/` 等静态资源。

> ⚠️ `DEBUG=True` 仅用于开发，**禁止用于生产环境**。

### 方案 B：前后端分离部署（参考知识库通用三件套）

如果希望复用「前端 / API / 数据库」分开部署的思路（如部署到 Vercel / Render / 云数据库），可按以下拆解：前端部署后，将其所有 `axios`/`fetch` 请求地址从 `http://localhost:8000/...` 改为你后端的线上地址（`https://你的后端地址/api/...`）。[cite:ada372a5-1]

#### ① 数据库层
- 后端连接线上数据库（如 PostgreSQL），把 `settings.py` 的 `DATABASES` 指向云数据库连接串（`postgresql://user:password@xxx:/postgres` 形式），并通过环境变量注入，避免明文写在代码里。

#### ② 后端 API 层
- 把后端代码推送到 GitHub，托管平台（如 Render）读取仓库后指定启动命令，例如 `gunicorn myproject.wsgi:application`。
- 通过平台的环境变量面板配置 `DATABASE_URL`、`SECRET_KEY`、`DEBUG=False` 等。[cite:ada372a5-2]

#### ③ 前端层
- 将 `frontend/` 部署到 Vercel 等静态托管平台（Vite 项目会自动执行 `npm run build` 并发布 `dist/`）。

#### ④ 跨域 CORS
因为前端域名与后端域名不同，浏览器会阻止跨域请求，需在后端启用 CORS。Django 中可安装 `django-cors-headers` 并在 `settings.py` 配置允许的来源（对应 Node 方案的 `app.use(cors())`）。[cite:ada372a5-1]

#### 完整请求链路
```
用户浏览器
   │
   ▼
前端静态站（Vercel 等）
   │  发起 POST /api/booking/
   ▼
后端 API（Gunicorn / Render 等）
   │
   ▼
数据库（SQLite 或 PostgreSQL）
   │
   ▼
返回 JSON → 页面显示预约结果
```

---

## 数据库操作命令

```powershell
python manage.py makemigrations   # 生成迁移文件
python manage.py migrate          # 执行迁移
python manage.py createsuperuser  # 创建超级管理员
python manage.py collectstatic    # 收集静态文件到 staticfiles/
python manage.py shell            # Django Shell
```

---

## 注意事项

- Django `DEBUG=True` 仅用于开发，生产环境必须关闭。
- 前端构建产物（`frontend/dist/`）是 Django 静态文件的来源，**不要手动修改 dist 目录**。
- 所有代码注释使用中文。
- 新增 Django 应用时，需在 `myproject/settings.py` 的 `INSTALLED_APPS` 中注册。
- `db.sqlite3`、`staticfiles/`、`venv/`、`node_modules/` 等目录已加入 `.gitignore`，不入库。
