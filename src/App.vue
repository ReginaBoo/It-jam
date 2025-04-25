<template>
  <div>
    <!-- Хедер -->
    <v-app-bar app>
      <v-toolbar-title class="text-red-500">HeroMap</v-toolbar-title>
      <v-text-field v-model="searchQuery" placeholder="Поиск..." append-icon="mdi-magnify" label="Поиск" solo />
    </v-app-bar>

    <!-- Категории -->
    <section class="p-4 flex gap-4 overflow-x-auto">
      <v-btn v-for="cat in categories" :key="cat" :class="{ 'v-btn--active': filterCategory === cat }"
        @click="filterCategory = cat" color="primary" outlined>
        {{ cat }}
      </v-btn>
    </section>

    <!-- Карточки мест -->
    <main class="p-4 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <v-card v-for="place in filteredPlaces" :key="place.id" class="rounded-2xl" hover :style="{ maxWidth: '300px' }">
        <v-img :src="place.image" alt="Place photo" height="200px" />
        <v-card-title>{{ place.name }}</v-card-title>
        <v-card-subtitle>{{ place.category }} • {{ place.address }}</v-card-subtitle>
        <v-card-actions>
          <v-rating v-model="place.rating" readonly color="yellow" size="20" />
          <v-btn @click="showDetails(place)">Подробнее</v-btn>
        </v-card-actions>
      </v-card>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

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
