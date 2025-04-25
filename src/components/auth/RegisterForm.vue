<script setup>
  import { reactive } from 'vue'
  import { useAuthStore } from '@/stores/authStore'
  import { useRouter } from 'vue-router'
  
  const authStore = useAuthStore()
  const router = useRouter()
  const form = reactive({
    username: '',
    password: '',
    preferredLanguage: 'ru'
  })
  
  const handleRegister = async () => {
    try {
      await authStore.register(form.username, form.password, form.preferredLanguage)
      router.push('/login')
    } catch (error) {
      alert(error.response?.data?.error || 'Registration failed')
    }
  }
</script>
<template>
    <form @submit.prevent="handleRegister">
        <input v-model="form.username" placeholder="Username" required>
        <input v-model="form.password" type="password" placeholder="Password" required>
        <select v-model="form.preferredLanguage">
            <option value="ru">Русский</option>
            <option value="en">English</option>
        </select>
        <button type="submit">Register</button>
    </form>
</template>
  
  
  