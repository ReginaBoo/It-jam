<template>
  <v-app>
    <AppHeader v-model="searchQuery" @login="navigateToLogin" @register="navigateToRegister"
      @category-selected="handleCategorySelected" />

    <HeroContent @search="handleSearch" :popular-places="popularPlaces" />

    <v-container>
      <YandexMap :places="filteredPlaces" :selected-place="selectedPlace" @place-selected="selectPlace"
        @route-requested="showRoute" />

      <PlaceList :places="filteredPlaces" :loading="loading" @show-details="showDetails"
        @toggle-favorite="toggleFavorite" />
    </v-container>

    <PlaceDetailsDialog v-if="selectedPlace" :place="selectedPlace" @close="selectedPlace = null"
      @add-review="addReview" />

    <RouteDialog v-if="routeDetails" :details="routeDetails" @close="routeDetails = null" />

    <v-snackbar v-model="snackbar.show" :color="snackbar.color">
      {{ snackbar.message }}
    </v-snackbar>

    <router-view />
  </v-app>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n/dist/vue-i18n.esm-bundler.js'
import AppHeader from '@/components/HomeComp/Header.vue'
import HeroContent from '@/components/HomeComp/HeroSection.vue'
import YandexMap from '@/components/HomeComp/YandexMap.vue'
import PlaceList from '@/components/HomeComp/PlaceList.vue'
import PlaceDetailsDialog from '@/components/HomeComp/PlaceDetailsDialog.vue'
import RouteDialog from '@/components/HomeComp/RouteDialog.vue'
import { fetchPlaces, fetchPlaceDetails, calculateRoute } from '@/api/places'

const { t } = useI18n()
const router = useRouter()

// State
const searchQuery = ref('')
const filterCategory = ref('Все')
const ratingFilter = ref(0)
const selectedPlace = ref(null)
const routeDetails = ref(null)
const loading = ref(false)
const places = ref([])
const favorites = ref(JSON.parse(localStorage.getItem('favorites')) || [])
const snackbar = ref({
  show: false,
  message: '',
  color: 'success'
})

const categories = computed(() => [
  { value: 'all', text: t('categories.all') },
  { value: 'cafe', text: t('categories.cafe') },
  { value: 'restaurant', text: t('categories.restaurant') },
  { value: 'attraction', text: t('categories.attraction') },
  { value: 'pharmacy', text: t('categories.pharmacy') }
])

const popularPlaces = computed(() =>
  [...places.value]
    .sort((a, b) => b.rating - a.rating)
    .slice(0, 4)
)

const filteredPlaces = computed(() => {
  let result = places.value

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(p =>
      p.name.toLowerCase().includes(query) ||
      p.description.toLowerCase().includes(query)
    )
  }

  if (filterCategory.value !== 'all') {
    result = result.filter(p => p.category === filterCategory.value)
  }

  if (ratingFilter.value > 0) {
    result = result.filter(p => p.rating >= ratingFilter.value)
  }

  return result
})

// Methods
const navigateToLogin = () => router.push('/login')
const navigateToRegister = () => router.push('/register')

const handleCategorySelected = (category) => {
  filterCategory.value = category
  applyFilters()
}

const handleSearch = (query) => {
  searchQuery.value = query
  applyFilters()
}

const applyFilters = () => {
  loading.value = true
  // Здесь можно добавить вызов API с фильтрами
  setTimeout(() => {
    loading.value = false
  }, 500)
}

const showDetails = (place) => {
  selectedPlace.value = place
}

const toggleFavorite = (place) => {
  const index = favorites.value.findIndex(fav => fav.id === place.id)
  if (index >= 0) {
    favorites.value.splice(index, 1)
    showSnackbar(t('messages.removedFromFavorites'), 'info')
  } else {
    favorites.value.push(place)
    showSnackbar(t('messages.addedToFavorites'), 'success')
  }
  localStorage.setItem('favorites', JSON.stringify(favorites.value))
}

const showRoute = async (from, to) => {
  try {
    loading.value = true
    const route = await calculateRoute(from, to)
    routeDetails.value = route
  } catch (error) {
    showSnackbar(t('errors.routeCalculation'), 'error')
  } finally {
    loading.value = false
  }
}

const addReview = async (review) => {
  try {
    // Отправка отзыва на сервер
    showSnackbar(t('messages.reviewAdded'), 'success')
    selectedPlace.value = null
  } catch (error) {
    showSnackbar(t('errors.reviewSubmit'), 'error')
  }
}

const showSnackbar = (message, color) => {
  snackbar.value = { show: true, message, color }
}

// Lifecycle
onMounted(async () => {
  try {
    loading.value = true
    places.value = await fetchPlaces()
  } catch (error) {
    showSnackbar(t('errors.loadingPlaces'), 'error')
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.v-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}
</style>