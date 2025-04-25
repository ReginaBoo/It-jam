<script setup>
    import { reactive } from 'vue'
    import { useAuthStore } from '@/stores/authStore'
    import { useRouter } from 'vue-router'

    const authStore = useAuthStore()
    const router = useRouter()
    const form = reactive({
    username: '',
    password: ''
    })

    const handleLogin = async () => {
    try {
        await authStore.login(form.username, form.password)
        router.push('/')
    } catch (error) {
        alert(error.response?.data?.error || 'Login failed')
    }
    }
</script>
<template>
    <form @submit.prevent="handleLogin">
      <input v-model="form.username" placeholder="Username" required>
      <input v-model="form.password" type="password" placeholder="Password" required>
      <button type="submit">Login</button>
    </form>
</template>
  

  