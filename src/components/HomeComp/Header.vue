<template>
  <v-app-bar app color="white" elevation="2">
    <!-- Логотип и название - теперь занимают меньше места -->
    <div class="d-flex align-center" style="min-width: 180px;">
      <v-toolbar-title class="text-red-500 font-weight-bold">HeroMap</v-toolbar-title>
    </div>

    <!-- Поле поиска - сдвинуто влево и адаптивное -->
    <v-text-field :model-value="modelValue" @update:modelValue="$emit('update:modelValue', $event)"
      placeholder="Поиск кафе, достопримечательностей..." prepend-inner-icon="mdi-magnify" solo flat dense hide-details
      class="mx-2" style="max-width: 450px; min-width: 200px; flex-grow: 1;" />

    <!-- Кнопки авторизации - теперь прижимаются к правому краю -->
    <div class="d-flex" style="margin-left: auto;">
      <v-btn text color="primary" class="mr-2" @click="$emit('login')">
        <v-icon left>mdi-login</v-icon>
        Вход
      </v-btn>

      <v-btn color="primary" outlined @click="$emit('register')">
        <v-icon left>mdi-account-plus</v-icon>
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
.v-app-bar {
  padding: 0 16px;
  gap: 8px;
  /* Добавляем промежутки между элементами */
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .v-toolbar__title {
    display: none;
  }

  .v-app-bar {
    padding: 0 8px;
  }
}
</style>