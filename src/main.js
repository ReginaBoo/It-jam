import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import i18n from './i18n'
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// Иконки
import '@mdi/font/css/materialdesignicons.css' // Импорт стилей иконок
import { aliases, mdi } from 'vuetify/iconsets/mdi' // Импорт набора иконок

const pinia = createPinia()

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    }
  }
})

const app = createApp(App)
app.use(pinia)
app.use(vuetify)
app.use(router)
app.use(i18n)
app.mount('#app')