<template>
  <v-app>
    <AppHeader v-model="searchQuery" @login="navigateToLogin" @register="navigateToRegister" />
    <CategoryFilter v-model="filterCategory" :categories="categories" />
    <YandexMap :places="filteredPlaces" />
    <PlaceList :places="filteredPlaces" @show-details="showDetails" />
    <router-view />
  </v-app>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import AppHeader from '@/components/HomeComp/Header.vue'

import YandexMap from '@/components/HomeComp/YandexMap.vue'

const router = useRouter()

// Навигация
const navigateToLogin = () => router.push('/login')
const navigateToRegister = () => router.push('/register')

// Логика фильтрации
const searchQuery = ref('')
const filterCategory = ref('Все')
const categories = ['Все', 'Кафе', 'Рестораны', 'Достопримечательности', 'Аптеки']

</script>