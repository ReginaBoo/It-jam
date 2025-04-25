<template>
  <v-form @submit.prevent="handleRegister">
    <v-text-field v-model="form.username" label="Username" required></v-text-field>
    <v-text-field v-model="form.password" type="password" label="Password" required></v-text-field>
    <v-select v-model="form.preferredLanguage" :items="['ru', 'en']" label="Preferred Language" required></v-select>
    <v-btn type="submit" color="primary">Зарегистрироваться</v-btn>
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
  password: '',
  preferredLanguage: 'ru'
})

const handleRegister = async () => {
  try {
    await authStore.register(form.value.username, form.value.password, form.value.preferredLanguage)
    router.push('/login') // Перенаправление на страницу логина после регистрации
  } catch (error) {
    alert(error.response?.data?.error || 'Ошибка при регистрации')
  }
}
</script>
