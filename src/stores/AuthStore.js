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
      const response = await axios.post('http://localhost:5000/api/auth/register', {
        username,
        password,
        preferredLanguage
      })
      return response.data
    },
    async login(username, password) {
      const response = await axios.post('http://localhost:5000/api/auth/login', {
        username,
        password
      })
      this.token = response.data.access_token
      localStorage.setItem('token', this.token)
      await this.fetchUser()
    },
    async fetchUser() {
      if (this.token) {
        const response = await axios.get('http://localhost:5000/api/auth/me', {
          headers: { 'Authorization': `Bearer ${this.token}` }
        })
        this.user = response.data
      }
    },
    logout() {
      this.user = null
      this.token = null
      localStorage.removeItem('token')
    }
  }
})
