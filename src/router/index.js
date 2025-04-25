// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import Home from '@/components/Home.vue' // Импорт компонента Home

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home, // Главная страница
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/components/auth/RegisterForm.vue'),
    meta: { requiresGuest: true }, // Доступ только для гостей
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/components/auth/LoginForm.vue'),
    meta: { requiresGuest: true }, // Доступ только для гостей
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('@/components/ProfileView.vue'),
    meta: { requiresAuth: true }, // Доступ только для авторизованных пользователей
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// Защита маршрутов с использованием meta
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.token) {
    next('/login') // Перенаправление на страницу логина
  } else if (to.meta.requiresGuest && authStore.token) {
    next('/') // Перенаправление на главную страницу
  } else {
    next() // Все остальные маршруты доступны
  }
})

export default router
