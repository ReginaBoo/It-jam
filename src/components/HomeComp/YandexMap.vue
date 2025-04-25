<template>
  <div ref="mapContainer" style="width: 100%; height: 400px;"></div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const mapContainer = ref(null)

onMounted(() => {
  // Дождёмся, пока библиотека ymaps полностью загрузится
  if (window.ymaps) {
    window.ymaps.ready(initMap)
  } else {
    // Подключим скрипт вручную
    const script = document.createElement('script')
    script.src = 'https://api-maps.yandex.ru/2.1/?apikey=35689e51-1bf8-426c-85e1-6c9e928816d5&lang=ru_RU'
    script.type = 'text/javascript'
    script.onload = () => window.ymaps.ready(initMap)
    document.head.appendChild(script)
  }
})

function initMap() {
  new window.ymaps.Map(mapContainer.value, {
    center: [55.76, 37.64], // Москва
    zoom: 10
  })
}
</script>
