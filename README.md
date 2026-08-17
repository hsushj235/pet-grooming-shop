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

## 部署指南（PythonAnywhere + Vercel）

> 本项目当前生产部署方案：**PythonAnywhere 托管 Django 后端**（免费、无需银行卡），**Vercel 托管 Vue 前端**。结构与知识库「前端 / API / 数据库」三件套思路一致：[cite:ada372a5-1][cite:ada372a5-2]

### 整体架构

```
用户浏览器
   │
   ▼
Vercel（前端静态站 Vue 3 + Vite）
   │  发起 POST ${VITE_API_BASE}/api/booking/
   ▼
PythonAnywhere（Django + WhiteNoise 静态资源）
   │
   ▼
SQLite 文件（项目目录下，PythonAnywhere 免费账号即可）
```

### 为什么选 PythonAnywhere

- 专门为 Django 优化，免费 Beginner 账号完全够用（1 个 Web App + 512MB 磁盘 + SQLite）。[cite:ada372a5-2]
- **不需要银行卡**（不像 Render/Railway/Fly.io 部分功能要求绑卡）。
- 自动 HTTPS（`*.pythonanywhere.com`），省去证书申请。

### 准备工作（一次性）

#### ① 把代码推送到 GitHub

```powershell
cd D:\项目1
git add -A
git commit -m "feat: 部署配置 - requirements/PythonAnywhere/生产配置/前端API_BASE"
git push origin main
```

> 仓库已存在 `origin: https://github.com/hsushj235/pet-grooming-shop.git`。

#### ② 生成 Django SECRET_KEY

在本地生成一个复杂随机串（保存到本地备用）：

```powershell
./venv/Scripts/python.exe -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 部署后端到 PythonAnywhere

#### ① 注册与控制台

1. 打开 <https://www.pythonanywhere.com/registration/>，注册免费 Beginner 账号（邮箱 + 用户名）。
2. 登录后顶部菜单 **Consoles** → **Bash**，打开一个 Bash 控制台。

#### ② 拉取代码并创建虚拟环境

在 Bash 控制台里依次执行（把 `你的用户名` 替换成 PythonAnywhere 给你的用户名，例如 `hsushj235`）：

```bash
cd ~
git clone https://github.com/hsushj235/pet-grooming-shop.git
cd pet-grooming-shop

# 创建虚拟环境并安装依赖
mkvirtualenv --python=python3.12 venv
pip install -r requirements.txt
```

> 首次使用 `mkvirtualenv` 会自动激活虚拟环境，下次进入用 `workon venv`。

#### ③ 构建前端

Django 的 collectstatic 需要前端的 `dist/` 已构建好。两种方式：

**方式 A：在本地构建并提交到仓库**（简单，但 dist 体积大）

```powershell
cd D:\项目1rontend
npm run build
cd ..
git add -A && git commit -m "build: 前端 dist" && git push
```

然后在 PythonAnywhere Bash 里 `git pull`。

**方式 B：在 PythonAnywhere 上构建**（需要 Node.js，免费账号默认没装，需要走 Task 计划或跳过；不推荐）

> **推荐方式 A**：本地构建一次提交即可，PythonAnywhere 拉到的就是带 dist 的完整代码。

#### ④ 数据库迁移与静态文件收集

继续在 PythonAnywhere Bash 里：

```bash
workon venv
cd ~/pet-grooming-shop

# 迁移数据库（SQLite 文件会自动生成在 ~/pet-grooming-shop/db.sqlite3）
python manage.py migrate

# 创建超级管理员（可选，用于登录 /admin/）
python manage.py createsuperuser

# 收集静态文件（前端 dist + simpleui + admin 全部进入 ~/pet-grooming-shop/staticfiles/）
python manage.py collectstatic --noinput
```

#### ⑤ 配置 Web App

回到 PythonAnywhere 控制台 → **Web** → **Add a new web app**：

- **Domain**：保持默认（你的用户名 + `pythonanywhere.com`）
- **Web app type**：**Manual configuration** → **Python 3.12**

然后进入 **Web** 页面顶部，往下到 **Virtualenv** 段，填入：

```
/home/你的用户名/.virtualenvs/venv
```

#### ⑥ 编辑 WSGI 配置文件

**Web** 页面 → **Code** 段 → **WSGI configuration file** → 点击进入编辑。把全部内容**替换**为以下（记得替换所有 `你的用户名`）：

```python
import os
import sys

# 项目根目录
path = '/home/你的用户名/pet-grooming-shop'
if path not in sys.path:
    sys.path.insert(0, path)

# 激活虚拟环境
activate_this = '/home/你的用户名/.virtualenvs/venv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

# Django 生产环境变量
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
os.environ['DJANGO_PRODUCTION'] = 'true'
os.environ['DJANGO_DEBUG'] = 'false'
os.environ['DJANGO_SECRET_KEY'] = '第②步生成的随机串'
os.environ['DJANGO_ALLOWED_HOSTS'] = '你的用户名.pythonanywhere.com'
os.environ['DJANGO_CORS_ALLOWED_ORIGINS'] = 'https://你的vercel域名.vercel.app'
os.environ['DJANGO_SSL_REDIRECT'] = 'false'  # PythonAnywhere 已自动 HTTPS

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

> `DJANGO_SSL_REDIRECT=false` 是因为 PythonAnywhere 在 WSGI 层已做 HTTPS 跳转，避免重复。

保存后回到 **Web** 页面顶部，点 **Reload**。

#### ⑦ 验证后端

访问 `https://你的用户名.pythonanywhere.com/`，应看到首页。访问 `/admin/` 用 superuser 登录。访问 `/api/bookings/` 应返回 JSON。

### 部署前端到 Vercel

#### ① Vercel 上导入项目

1. 打开 <https://vercel.com> → 用 GitHub 登录。
2. **Add New… → Project** → 选择 `hsushj235/pet-grooming-shop`。
3. **Root Directory**：点击 Edit → 改成 `frontend`。

#### ② 配置环境变量

**Environment Variables** 段添加：

| Key | Value |
|-----|-------|
| `VITE_API_BASE` | `https://你的用户名.pythonanywhere.com` |

#### ③ 部署

其它保持默认（Vercel 会自动执行 `npm run build`），点击 **Deploy**。完成后会得到一个 `*.vercel.app` 地址，例如 `https://pet-grooming-shop.vercel.app`。

#### ④ 把 Vercel 域名写入后端 CORS

回到 PythonAnywhere **Web** → WSGI 配置 → 修改：

```python
os.environ['DJANGO_CORS_ALLOWED_ORIGINS'] = 'https://实际vercel域名.vercel.app'
```

保存 → **Reload**。

### 验证全链路

1. 浏览器打开 Vercel 给的地址。
2. 进入「预约」页面，填写表单提交。
3. 浏览器开发者工具 Network 应看到一条 `POST https://你的用户名.pythonanywhere.com/api/booking/`，状态码 200。
4. 返回 PythonAnywhere 后台 → `/admin/` → 预约记录，可看到新条目。

### 数据库切换（可选：到 PostgreSQL）

如果以后想把 SQLite 换成 PostgreSQL（数据更安全、更适合生产）：

1. 在任何云平台（Render 免费 PostgreSQL / Supabase / Neon / ElephantSQL）创建一个免费 PostgreSQL，得到 `DATABASE_URL`。
2. 编辑 PythonAnywhere WSGI 配置添加：
   ```python
   os.environ['DATABASE_URL'] = 'postgresql://user:pass@host:5432/dbname'
   ```
   （代码已经支持，settings.py 末尾生产块会优先用 DATABASE_URL，无需改代码）
3. 在 Bash 控制台跑 `python manage.py migrate` 建表。

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
