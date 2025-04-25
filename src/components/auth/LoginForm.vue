<template>
  <v-form @submit.prevent="handleLogin">
    <v-text-field v-model="form.username" label="Username" required></v-text-field>
    <v-text-field v-model="form.password" type="password" label="Password" required></v-text-field>
    <v-btn type="submit" color="primary">Войти</v-btn>
  </v-form>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/authStore'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const form = ref({
  username: '',
  password: ''
})

const handleLogin = async () => {
  try {
    await authStore.login(form.value.username, form.value.password)
    router.push('/') // Перенаправление на главную страницу после логина
  } catch (error) {
    alert(error.response?.data?.error || 'Ошибка при входе')
  }
}
</script>
