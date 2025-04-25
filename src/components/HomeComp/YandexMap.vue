<template>
  <div>
    <div ref="mapContainer" style="width: 100%; height: 500px;"></div>
    <div class="route-controls">
      <button @click="startRouteCreation" class="route-button">
        {{ isCreatingRoute ? 'Отменить' : 'Построить маршрут' }}
      </button>
      <button @click="clearRoute" class="route-button">
        Очистить маршрут
      </button>
      <div v-if="routeInfo" class="route-info">
        <p>Расстояние: {{ routeInfo.distance }}</p>
        <p>Время в пути: {{ routeInfo.duration }}</p>
        <p v-if="routeInfo.jam">Пробки: {{ routeInfo.jam }}</p>
      </div>
    </div>
    <div v-if="errorMessage" class="error-message">
      {{ errorMessage }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'

const mapContainer = ref(null)
let map = null
let route = null
let placemarks = []
const isCreatingRoute = ref(false)
const routeInfo = ref(null)
const errorMessage = ref(null)

const hasRoute = computed(() => route !== null)

onMounted(() => {
  loadYmaps()
})

function loadYmaps() {
  if (window.ymaps) {
    window.ymaps.ready(initMap)
  } else {
    const script = document.createElement('script')
    script.src = 'https://api-maps.yandex.ru/2.1/?apikey=35689e51-1bf8-426c-85e1-6c9e928816d5&lang=ru_RU'
    script.onload = () => window.ymaps.ready(initMap)
    script.onerror = () => {
      errorMessage.value = 'Ошибка загрузки Яндекс.Карт'
    }
    document.head.appendChild(script)
  }
}

function initMap() {
  try {
    map = new window.ymaps.Map(mapContainer.value, {
      center: [56.8389, 60.6057], // Екатеринбург
      zoom: 10,
      controls: ['zoomControl', 'typeSelector', 'trafficControl']
    })
    
    map.controls.get('trafficControl').state.set('providerKey', 'traffic#actual')
    map.events.add('click', onMapClick)
  } catch (error) {
    errorMessage.value = 'Ошибка инициализации карты'
    console.error('Map init error:', error)
  }
}

function startRouteCreation() {
  isCreatingRoute.value = !isCreatingRoute.value
  if (!isCreatingRoute.value) {
    clearPlacemarks()
  }
}

function onMapClick(e) {
  if (!isCreatingRoute.value) return
  
  if (placemarks.length >= 2) {
    clearPlacemarks()
  }
  
  const coords = e.get('coords')
  createPlacemark(coords)
  
  if (placemarks.length === 2) {
    buildRoute()
    isCreatingRoute.value = false
  }
}

function createPlacemark(coords) {
  const placemark = new window.ymaps.Placemark(
    coords,
    { hintContent: `Точка ${placemarks.length + 1}` },
    { preset: 'islands#blueDotIcon' }
  )
  
  map.geoObjects.add(placemark)
  placemarks.push(placemark)
}

async function buildRoute() {
  errorMessage.value = null
  
  const points = placemarks.map(p => p.geometry.getCoordinates())
  
  // Удаляем предыдущий маршрут
  if (route) {
    map.geoObjects.remove(route)
    route = null
  }
  
  // Строим новый маршрут
  route = await window.ymaps.route(points, {
    mapStateAutoApply: true,
    boundsAutoApply: true,
    routingMode: 'auto',
    avoidTrafficJams: true
  })
  
  // Настраиваем отображение маршрута
  route.options.set({
    routeStrokeWidth: 5,
    routeStrokeColor: '#88a35b',
    routeActiveStrokeWidth: 7,
    routeActiveStrokeColor: '#6a7f46'
  })
  
  map.geoObjects.add(route)
  // updateRouteInfo()
  console.log(hasRoute)
  // Центрируем карту на маршруте
  map.setBounds(route.getBounds(), { checkZoomRange: true })

}

// function updateRouteInfo() {
//   if (!route) return
  
//   const activeRoute = route.get(0)
//   routeInfo.value = {
//     distance: activeRoute.properties.get('distance').text,
//     duration: activeRoute.properties.get('duration').text,
//     jam: getJamLevel(activeRoute.properties.get('jamFactor'))
//   }
// }

function getJamLevel(factor) {
  if (factor === undefined) return 'нет данных'
  if (factor < 0.3) return 'лёгкие'
  if (factor < 0.6) return 'средние'
  return 'сильные'
}

function clearPlacemarks() {
  placemarks.forEach(pm => map.geoObjects.remove(pm))
  placemarks = []
}

function clearRoute() {
  if (route) {
    map.geoObjects.remove(route)
    route = null
  }
  clearPlacemarks()
  routeInfo.value = null
}
</script>

<style>
.route-controls {
  margin-top: 15px;
  display: flex;
  gap: 10px;
  align-items: center;
  flex-wrap: wrap;
}

.route-button {
  padding: 8px 16px;
  background-color: #88a35b;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.route-button:hover {
  background-color: #45a049;
}

.route-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.route-info {
  margin-left: 20px;
  padding: 10px;
  background-color: #f5f5f5;
  border-radius: 4px;
}

.route-info p {
  margin: 5px 0;
}

.error-message {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 20px;
  background-color: #ff4444;
  color: white;
  border-radius: 4px;
  z-index: 1000;
  animation: fadeIn 0.3s;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>