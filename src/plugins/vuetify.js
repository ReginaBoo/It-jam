import 'vuetify/styles' // Global CSS
import { createVuetify } from 'vuetify'
import { mdi } from 'vuetify/iconsets/mdi-svg' // Или используйте шрифтовые иконки

// Импорт Material Design Icons
import '@mdi/font/css/materialdesignicons.min.css'

export default createVuetify({
  icons: {
    defaultSet: 'mdi',
    sets: {
      mdi,
    }
  },
  theme: {
    defaultTheme: 'light'
  }
})