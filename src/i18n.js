import { createI18n } from 'vue-i18n'

const messages = {
  en: {
    categories: {
      all: 'All',
      cafe: 'Cafe',
      restaurant: 'Restaurant',
      attraction: 'Attraction',
      pharmacy: 'Pharmacy'
    },
    messages: {
      addedToFavorites: 'Added to favorites',
      removedFromFavorites: 'Removed from favorites',
      reviewAdded: 'Review added successfully'
    },
    errors: {
      loadingPlaces: 'Failed to load places',
      routeCalculation: 'Route calculation failed',
      reviewSubmit: 'Failed to submit review'
    }
  },
  ru: {
    categories: {
      all: 'Все',
      cafe: 'Кафе',
      restaurant: 'Ресторан',
      attraction: 'Достопримечательность',
      pharmacy: 'Аптека'
    },
    messages: {
      addedToFavorites: 'Добавлено в избранное',
      removedFromFavorites: 'Удалено из избранного',
      reviewAdded: 'Отзыв успешно добавлен'
    },
    errors: {
      loadingPlaces: 'Не удалось загрузить места',
      routeCalculation: 'Ошибка расчета маршрута',
      reviewSubmit: 'Не удалось отправить отзыв'
    }
  }
}

const i18n = createI18n({
  legacy: false,
  locale: 'ru', // язык по умолчанию
  fallbackLocale: 'en',
  messages
})

export default i18n