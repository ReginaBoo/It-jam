<template>
  <div class="d-flex flex-column align-center justify-center" style="min-height: 100vh;">
    <h1 class="mb-6" style="color: #333; font-weight: 500;">Вход в систему</h1>
    
    <v-form 
      @submit.prevent="handleLogin" 
      class="pa-6" 
      style="
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 500px;
        background: white;
      "
    >
      <v-text-field 
        v-model="form.username" 
        label="Username" 
        required
        class="mb-4"
      ></v-text-field>
      
      <v-text-field 
        v-model="form.password" 
        type="password" 
        label="Password" 
        required
        class="mb-4"
      ></v-text-field>
      
      <div class="text-center mt-4">
        <v-btn 
          type="submit" 
          rounded="xl" 
          color="#88a35b"
          block
        >
          Войти
        </v-btn>
      </div>
    </v-form>
  </div>
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
