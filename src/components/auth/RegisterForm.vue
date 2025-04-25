<template>
  <div class="d-flex flex-column align-center justify-center" style="min-height: 100vh;">
    <h1 class="mb-6" style="color: #333; font-weight: 500;">Регистрация</h1>
    
    <v-form 
      @submit.prevent="handleRegister" 
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
      ></v-text-field>
      <v-text-field 
        v-model="form.password" 
        type="password" 
        label="Password" 
        required
      ></v-text-field>
      <v-select 
        v-model="form.preferredLanguage" 
        :items="['ru', 'en']" 
        label="Preferred Language" 
        required
      ></v-select>
      <div class="text-center mt-4">
        <v-btn 
          type="submit" 
          rounded="xl" 
          color="#88a35b"
          block
        >
          Зарегистрироваться
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
