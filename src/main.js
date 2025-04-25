import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // Добавьте эту строку
import { createPinia } from 'pinia' // Добавьте для работы хранилища
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)

app.use(createPinia()) // Должно быть перед router
app.use(router) // Подключите роутер
app.use(vuetify)

app.mount('#app')