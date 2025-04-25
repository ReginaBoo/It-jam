import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null
  }),
  actions: {
    async register(username, password, preferredLanguage = 'ru') {
      try {
        const response = await axios.post('http://localhost:5000/api/auth/register', {
          username,
          password,
          preferredLanguage
        })
        return response.data
      } catch (error) {
        throw new Error(error.response?.data?.message || 'Registration failed')
      }
    },
    async login(username, password) {
      try {
        const response = await axios.post('http://localhost:5000/api/auth/login', {
          username,
          password
        })
        this.token = response.data.access_token
        localStorage.setItem('token', this.token)
        await this.fetchUser()
      } catch (error) {
        throw new Error(error.response?.data?.message || 'Login failed')
      }
    },
    async fetchUser() {
      if (this.token) {
        try {
          const response = await axios.get('http://localhost:5000/api/auth/me', {
            headers: { 'Authorization': `Bearer ${this.token}` }
          })
          this.user = response.data
        } catch (error) {
          this.logout() // Если ошибка при получении данных пользователя, возможно токен невалиден
        }
      }
    },
    logout() {
      this.user = null
      this.token = null
      localStorage.removeItem('token')
    }
  },
  persist: true, // Добавить persistence, если используешь vue-persistedstate или подобное для сохранения состояния
})
