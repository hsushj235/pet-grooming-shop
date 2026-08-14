# Pet Grooming Shop Website (宠物洗护店)

## 项目概述

基于 Django + Vue 3 的宠物洗护店网站，前台面向客户展示服务与预约，后台使用 django-simpleui 进行管理。

- **后端**：Django 6.1 + SQLite，语言 zh-hans，时区 Asia/Shanghai
- **前端**：Vue 3 + Vite，位于 `frontend/`
- **后台**：simpleui 主题，已中文化
- **根路径**：`D:\项目1\`

---

## 目录结构

```
D:\项目1\
├── AGENTS.md               # 本文件
├── manage.py
├── myproject/              # Django 项目配置
│   ├── settings.py         # 已在 LANGUAGE_CODE/TIME_ZONE/STATICFILES_DIRS 配置
│   ├── urls.py             # 路由：/admin/ 和 /（Vue index.html）
│   ├── wsgi.py
│   └── asgi.py
├── core/                   # Django 应用，存放业务模型与逻辑
│   ├── models.py           # 核心数据模型（服务、预约、客户、宠物等）
│   ├── views.py
│   ├── admin.py            # simpleui 后台注册
│   ├── apps.py
│   └── migrations/
├── frontend/               # Vue 3 前端源码
│   ├── src/
│   │   ├── App.vue         # 根组件
│   │   └── main.js
│   ├── dist/               # Vite 构建产物，由 Django 托管
│   ├── index.html
│   └── package.json
├── staticfiles/            # collectstatic 输出目录
└── db.sqlite3              # SQLite 数据库
```

---

## 快速启动

```powershell
# 激活虚拟环境
. D:\项目1\venv\Scripts\Activate.ps1

# 启动开发服务器
cd D:\项目1
python manage.py runserver 0.0.0.0:8000
```

- 前台首页：http://127.0.0.1:8000/
- 后台管理：http://127.0.0.1:8000/admin/ （账号 n167729 / 123456）

---

## 前端开发

```powershell
cd D:\项目1\frontend
npm install          # 首次安装依赖
npm run dev          # 本地开发服务器（热更新）
npm run build        # 构建生产版本（构建产物输出到 dist/）
```

> 每次修改前端代码后需运行 `npm run build`，然后重启 Django 服务器使新资源生效。

---

## 数据库操作

```powershell
python manage.py makemigrations   # 生成迁移文件
python manage.py migrate          # 执行迁移
python manage.py createsuperuser  # 创建超级管理员
python manage.py shell            # Django Shell
```

---

## 技术栈与依赖

| 层 | 技术 |
|----|------|
| 后端框架 | Django 6.1 |
| 前端框架 | Vue 3（Vite 构建） |
| 后台 UI | django-simpleui（中文化） |
| 数据库 | SQLite 3 |
| Python | 3.14+ |
| Node.js | 24+ |

---

## 主要功能模块（规划）

1. **首页** — 轮播 banner、服务介绍、门店信息
2. **服务页** — 洗护套餐、美容项目、价格展示
3. **预约系统** — 在线选择服务项目、日期时段、填写宠物信息
4. **会员系统** — 注册登录、储值余额、消费记录
5. **后台管理** — 订单管理、客户管理、服务商品管理、数据看板

---

## 注意事项

- Django `DEBUG=True`，禁止用于生产环境
- 前端构建产物（`frontend/dist/`）是 Django 静态文件的来源，不要手动修改 dist 目录
- 所有代码注释使用中文
- 新增 Django 应用时同步在 `myproject/settings.py` 的 `INSTALLED_APPS` 中注册
