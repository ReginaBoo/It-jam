<template>
  <v-app-bar app color="white" elevation="2" class="yelp-header">
    <!-- Логотип -->
    <div class="d-flex align-center logo-container">
      <v-toolbar-title class="text-red-darken-1 font-weight-bold text-h5">HeroMap</v-toolbar-title>
    </div>



    <!-- Поле поиска -->
    <v-text-field :model-value="modelValue" @update:modelValue="$emit('update:modelValue', $event)"
      placeholder="Найти..." prepend-inner-icon="mdi-magnify" solo flat dense hide-details class="search-field mx-2"
      style="max-width: 450px; min-width: 200px;" />

    <!-- Кнопки авторизации -->
    <div class="auth-buttons">
      <v-btn text color="grey-darken-3" class="mr-2 font-weight-medium" @click="$emit('login')">
        Вход
      </v-btn>

      <v-btn color="red-darken-1" dark depressed class="signup-btn font-weight-medium" @click="$emit('register')">
        Регистрация
      </v-btn>
    </div>
  </v-app-bar>
</template>

<script setup>
defineProps({
  modelValue: String
})

defineEmits([
  'update:modelValue',
  'login',
  'register'
])
</script>

<style scoped>
.yelp-header {
  padding: 0 24px;
  gap: 16px;
}

.logo-container {
  min-width: 120px;
}

.header-links {
  gap: 4px;
}

.search-field {
  background-color: #f5f5f5 !important;
  border-radius: 4px !important;
}

.search-field :deep(.v-input__slot) {
  box-shadow: none !important;
}

.auth-buttons {
  margin-left: auto;
  display: flex;
  align-items: center;
}

.signup-btn {
  text-transform: none;
  letter-spacing: normal;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
}

/* Адаптивность для мобильных устройств */
@media (max-width: 960px) {
  .yelp-header {
    padding: 0 12px;
  }

  .header-links {
    display: none !important;
  }
}

@media (max-width: 600px) {
  .logo-container {
    min-width: auto;
    margin-right: 8px;
  }

  .v-toolbar__title {
    font-size: 1.25rem !important;
  }

  .search-field {
    min-width: 120px !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  .auth-buttons {
    margin-left: 8px;
  }

  .auth-buttons .v-btn {
    min-width: auto !important;
    padding: 0 8px !important;
  }
}
</style>