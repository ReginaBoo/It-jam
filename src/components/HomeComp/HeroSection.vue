<template>
  <section class="hero-section">
    <div class="hero-content">
      <h1 class="hero-title">Найдите лучшие места в городе</h1>
      <div class="search-container">
        <div class="search-tabs">
          <button class="search-tab" :class="{ active: selectedCategory === 'all' }" @click="selectedCategory = 'all'">
            Все
          </button>
          <button class="search-tab" :class="{ active: selectedCategory === 'restaurant' }"
            @click="selectedCategory = 'restaurant'">
            Рестораны
          </button>
          <button class="search-tab" :class="{ active: selectedCategory === 'attraction' }"
            @click="selectedCategory = 'attraction'">
            Достопримечательности
          </button>
          <button class="search-tab" :class="{ active: selectedCategory === 'hotel' }"
            @click="selectedCategory = 'hotel'">
            Отели
          </button>
        </div>

        <div class="rating-slider-container">
          <label class="rating-label">Минимальный рейтинг: {{ minRating }}</label>
          <v-slider v-model="minRating" :min="0" :max="5" :step="0.1" thumb-label class="rating-slider"></v-slider>
        </div>
      </div>

      <div v-if="filteredPosts.length > 0" class="posts-container">
        <div v-for="post in filteredPosts" :key="post.id" class="post">
          <h3>{{ post.title }}</h3>
          <v-map :center="post.location" :zoom="13" class="mini-map">
            <v-marker :position="post.location"></v-marker>
          </v-map>
          <p>Рейтинг: {{ post.rating }}</p>
        </div>
      </div>
      <div v-else class="no-posts">
        <p>Посты не найдены для выбранной категории или рейтинга.</p>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'HeroSection',
  data() {
    return {
      selectedCategory: 'all',
      searchQuery: '',
      minRating: 0, // ← Добавлен фильтр по рейтингу
      posts: [
        { id: 1, title: 'Лучший ресторан', category: 'restaurant', location: { lat: 55.7558, lng: 37.6173 }, rating: 4.5 },
        { id: 2, title: 'Туристическая достопримечательность', category: 'attraction', location: { lat: 55.751244, lng: 37.618423 }, rating: 4.8 },
        { id: 3, title: 'Уютный отель', category: 'hotel', location: { lat: 55.755, lng: 37.6177 }, rating: 4.2 },
        { id: 4, title: 'Знаменитый ресторан', category: 'restaurant', location: { lat: 55.756, lng: 37.618 }, rating: 4.7 }
      ]
    };
  },
  computed: {
    filteredPosts() {
      return this.posts.filter(post => {
        const matchesCategory = this.selectedCategory === 'all' || post.category === this.selectedCategory;
        const matchesQuery = post.title.toLowerCase().includes(this.searchQuery.toLowerCase());
        const matchesRating = post.rating >= this.minRating;
        return matchesCategory && matchesQuery && matchesRating;
      });
    }
  }
};
</script>
<style scoped>
.hero-section {
  background-image: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)),
    url('@/assets/Hero.jpg');
  background-position: center;
  height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-align: center;
  padding: 0 20px;
}

.hero-content {
  max-width: 800px;
  width: 100%;
}

.hero-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 30px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.search-container {
  background: white;
  border-radius: 4px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  overflow: hidden;
}

.search-tabs {
  display: flex;
  background: #f5f5f5;
  padding: 0 10px;
}

.search-tab {
  padding: 12px 16px;
  background: none;
  border: none;
  font-weight: 600;
  color: #333;
  cursor: pointer;
  position: relative;
}

.search-tab.active {
  color: #d32323;
}

.search-tab.active:after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: #d32323;
}

.search-bar {
  display: flex;
  padding: 10px;
}

.search-input {
  flex-grow: 1;
}

.search-button {
  margin-left: 10px;
  text-transform: none;
  font-weight: 600;
  letter-spacing: normal;
}

.posts-container {
  margin-top: 20px;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
  padding: 0 20px;
}

.post {
  width: 100%;
  max-width: 300px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 15px;
  box-sizing: border-box;
  color: #333;
  /* Основной цвет текста для поста */
}

.post h3 {
  color: #d32323;
  /* Цвет для заголовков */
}

.post p {
  color: #666;
  /* Цвет для параграфов */
}

.mini-map {
  height: 200px;
  width: 100%;
  border-radius: 4px;
}

.no-posts {
  margin-top: 20px;
  font-size: 1.2rem;
  color: #999;
}

.rating-slider-container {
  margin: 10px 0;
}

.rating-label {
  margin-top: 5px;
  margin: 0 0;
  font-size: 1.0rem;
  color: #333;
  align-self: flex-start;
}

.rating-slider {
  margin: 0 0;
}
</style>