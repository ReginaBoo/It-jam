<!-- src/components/Home.vue -->
<template>
<v-app>
    <!-- Хедер с кнопками навигации -->
    <v-app-bar app color="primary">
      <v-toolbar-title class="text-white">HeroMap</v-toolbar-title>
      
      <v-spacer></v-spacer>
      
      <!-- Кнопка Войти -->
      <v-btn 
        @click="navigateToLogin"
        color="white" 
        variant="text"
        class="mr-2"
      >
        <v-icon left>mdi-login</v-icon>
        Войти
      </v-btn>
      
      <!-- Кнопка Регистрация -->
      <v-btn 
        @click="navigateToRegister"
        color="white" 
        variant="outlined"
      >
        <v-icon left>mdi-account-plus</v-icon>
        Регистрация
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <section class="p-4 flex gap-4 overflow-x-auto">
          <v-btn 
            v-for="cat in categories" 
            :key="cat" 
            :class="{ 'v-btn--active': filterCategory === cat }"
            @click="filterCategory = cat" 
            color="primary" 
            outlined
          >
            {{ cat }}
          </v-btn>
        </section>

        <v-row class="pa-4">
          <v-col 
            v-for="place in filteredPlaces" 
            :key="place.id" 
            cols="12" 
            sm="6" 
            lg="4"
          >
            <v-card class="rounded-xl" hover>
              <v-img :src="place.image" height="200px" cover />
              <v-card-title>{{ place.name }}</v-card-title>
              <v-card-subtitle>
                {{ place.category }} • {{ place.address }}
              </v-card-subtitle>
              <v-card-actions>
                <v-rating :model-value="place.rating" readonly color="yellow" size="small" />
                <v-btn @click="showDetails(place)">Подробнее</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Обработчик перехода на страницу входа
const navigateToLogin = () => {
  router.push('/login')
}

// Обработчик перехода на страницу регистрации
const navigateToRegister = () => {
  router.push('/register')
}

const searchQuery = ref('')
const filterCategory = ref('Все')

const categories = ['Все', 'Кафе', 'Рестораны', 'Достопримечательности', 'Аптеки']

const places = ref([
  {
    id: 1,
    name: 'Кафе "Бодрое утро"',
    category: 'Кафе',
    rating: 4.7,
    address: 'ул. Ленина, 12',
    review: 'Отличный кофе и уютная атмосфера.',
    image: 'https://source.unsplash.com/400x250/?coffee',
  },
  {
    id: 2,
    name: 'Парк Победы',
    category: 'Достопримечательности',
    rating: 4.5,
    address: 'пр. Мира, 8',
    review: 'Прекрасное место для прогулок.',
    image: 'https://source.unsplash.com/400x250/?park',
  },
  {
    id: 3,
    name: 'Аптека 24',
    category: 'Аптеки',
    rating: 4.2,
    address: 'ул. Гагарина, 25',
    review: 'Работает круглосуточно, всегда всё есть.',
    image: 'https://source.unsplash.com/400x250/?pharmacy',
  },
])

const filteredPlaces = computed(() => {
  return places.value.filter(p => {
    const matchesCategory = filterCategory.value === 'Все' || p.category === filterCategory.value
    const matchesSearch = p.name.toLowerCase().includes(searchQuery.value.toLowerCase())
    return matchesCategory && matchesSearch
  })
})

const showDetails = (place) => {
  alert(`Подробнее о ${place.name}`)
}
</script>
