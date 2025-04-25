<template>
  <v-app-bar app color="white" elevation="2" class="yelp-header">
    <!-- Логотип -->
    <div class="d-flex align-center logo-container">
      <v-toolbar-title class="text-red-darken-1 font-weight-bold text-h5">HeroMap</v-toolbar-title>
    </div>

    <!-- Выпадающий список категорий -->
    <div class="categories-container">
      <v-menu offset-y>
        <template v-slot:activator="{ props }">
          <v-btn color="red-darken-1" dark depressed v-bind="props" class="categories-btn">
            <v-icon left>mdi-menu</v-icon>
            Категории
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="(item, index) in categories" :key="index" @click="selectCategory(item.value)">
            <v-list-item-title>
              <v-icon left :color="item.color">{{ item.icon }}</v-icon>
              {{ item.title }}
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>

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
import { useRouter } from 'vue-router'

const router = useRouter()

const categories = [
  { title: 'Рестораны', value: 'restaurants', icon: 'mdi-food', color: 'red' },
  { title: 'Кафе', value: 'cafes', icon: 'mdi-coffee', color: 'brown' },
  { title: 'Бары', value: 'bars', icon: 'mdi-glass-cocktail', color: 'amber' },
  { title: 'Достопримечательности', value: 'attractions', icon: 'mdi-landmark', color: 'blue' },
  { title: 'Отели', value: 'hotels', icon: 'mdi-hotel', color: 'purple' },
  { title: 'Парки', value: 'parks', icon: 'mdi-tree', color: 'green' },
]

const selectCategory = (category) => {
  // Эмитим событие с выбранной категорией
  emit('category-selected', category)
  // Или переходим сразу на маршрут
  router.push({
    name: 'map',
    query: { category }
  })
}

defineEmits(['login', 'register', 'category-selected'])
</script>

<style scoped>
categories-container {
  margin-left: 16px;
}

.categories-btn {
  text-transform: none;
  letter-spacing: normal;
}

.yelp-header {
  padding: 0 24px;
  gap: 16px;
}

.logo-container {
  min-width: 120px;
}

.search-container {
  display: flex;
  align-items: center;
  flex-grow: 1;
  max-width: 600px;
}

.search-field {
  background-color: #f5f5f5 !important;
  border-radius: 4px !important;
  flex-grow: 1;
}

.search-field :deep(.v-input__slot) {
  box-shadow: none !important;
}

.search-button {
  margin-left: 8px;
  height: 40px !important;
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

/* Адаптивность */
@media (max-width: 960px) {
  .yelp-header {
    padding: 0 12px;
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

  .search-container {
    flex-direction: column;
    width: 100%;
    max-width: none;
  }

  .search-field {
    width: 100%;
    min-width: auto !important;
    margin: 0 0 8px 0 !important;
  }

  .search-button {
    width: 100%;
    margin-left: 0;
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