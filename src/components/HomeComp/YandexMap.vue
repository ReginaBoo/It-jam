<template>
  <div>
    <div ref="mapContainer" style="width: 100%; height: 500px;"></div>
    <div class="route-controls">
      <v-btn dark depressed color="red-darken-1" @click="startRouteCreation" class="route-button">
        {{ isCreatingRoute ? 'Отменить' : 'Построить маршрут' }}
      </v-btn>
      <v-btn @click="clearRoute" class="route-button">
        Очистить маршрут
      </v-btn>
      <v-select
        v-model="selectedTransport"
        label="Тип маршрута"
        :items="transportOptions"
        variant="solo"
        density="comfortable"
        hide-details
        class="transport-select"
        @update:modelValue="handleTransportChange"
      ></v-select>
      
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
let placemarks = []
const isCreatingRoute = ref(false)
const routeInfo = ref(null)
const errorMessage = ref(null)
const selectedTransport = ref('auto') // По умолчанию автомобиль
const avoidTraffic = ref(false)
let multiRoute = null

const transportOptions = [
  { title: 'Автомобиль', value: 'auto' },
  { title: 'Общественный транспорт', value: 'masstransit' },
  { title: 'Пешком', value: 'pedestrian' }
];

const hasRoute = computed(() => multiRoute !== null)

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
  
  if (multiRoute) {
    map.geoObjects.remove(multiRoute)
    multiRoute = null
  }
  
  // const MultiRoute = window.ymaps.multiRouter
  const routeType = selectedTransport.value
  
  const routeOptions = {
    referencePoints: points,
    params: {
      routingMode: routeType,
      avoidTrafficJams: routeType === 'driving' && avoidTraffic.value
    }
  }
  

  switch(routeType) {
    case 'masstransit':
      multiRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: points,
        params: {
            routingMode: 'masstransit'
        }
      }, {
        // Автоматически устанавливать границы карты так, чтобы маршрут был виден целиком.
        boundsAutoApply: true
      });
      break
    case 'pedestrian':
      multiRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: points,
        params: {
            //Тип маршрутизации - пешеходная маршрутизация.
            routingMode: 'pedestrian'
        }
    }, {
        // Автоматически устанавливать границы карты так, чтобы маршрут был виден целиком.
        boundsAutoApply: true
    });
      break
    default: // driving
      multiRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: points,
        params: {
          results: 2
        }
    }, {
        // Автоматически устанавливать границы карты так, чтобы маршрут был виден целиком.
        boundsAutoApply: true
    });
  }
  map.geoObjects.add(multiRoute)
  // updateRouteInfo()
  console.log(hasRoute)
  // Центрируем карту на маршруте
  map.setBounds(multiRoute.getBounds(), { checkZoomRange: true })

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
  if (multiRoute) {
    map.geoObjects.remove(multiRoute)
    multiRoute = null
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

/* .route-button {
  padding: 8px 16px;
  background-color: #F44336;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
} */

/* .route-button:hover {
  background-color: #45a049;
} */

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