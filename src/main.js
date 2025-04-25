import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Добавьте эту строку
import { createPinia } from 'pinia' // Добавьте для работы хранилища
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { createPinia } from 'pinia' // Импортируем Pinia
import router from './router' // Подключаем маршрутизатор

const pinia = createPinia() // Создаем экземпляр Pinia
const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)

app.use(pinia) // Подключаем Pinia
app.use(vuetify) // Подключаем Vuetify
app.use(router) // Подключаем Vue Router

app.mount('#app') // Монтируем приложение

