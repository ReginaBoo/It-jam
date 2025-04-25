import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const routes = [
  {
    path: '/register',
    name: 'register',
    component: () => import('@/components/auth/RegisterForm.vue'),
    meta: { requiresGuest: true }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/components/auth/LoginForm.vue'),
    meta: { requiresGuest: true }
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('@/components/ProfileView.vue'),
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  
  if (to.meta.requiresAuth && !authStore.token) {
    next('/login')
  } else if (to.meta.requiresGuest && authStore.token) {
    next('/')
  } else {
    next()
  }
})

export default router
