<template>
  <section class="hero-section">
    <div class="hero-content">
      <h1 class="hero-title">Найдите лучшие места в городе</h1>
      <div class="search-container">
        <div class="search-tabs">
          <button class="search-tab active">Все</button>
          <button class="search-tab">Рестораны</button>
          <button class="search-tab">Достопримечательности</button>
          <button class="search-tab">Отели</button>
        </div>
        <div class="search-bar">
          <v-text-field placeholder="Например: 'итальянская кухня'" solo flat hide-details
            prepend-inner-icon="mdi-magnify" class="search-input"></v-text-field>
          <v-btn color="red darken-1" dark large class="search-button">
            Найти
          </v-btn>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroSection'
}
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

.search-input :deep(.v-input__slot) {
  box-shadow: none !important;
  background: #fff !important;
  border: 1px solid #ddd !important;
  border-radius: 4px !important;
}

.search-button {
  margin-left: 10px;
  text-transform: none;
  font-weight: 600;
  letter-spacing: normal;
}

.popular-searches {
  margin-top: 20px;
  font-size: 0.9rem;
}

.popular-link {
  color: white;
  margin-left: 15px;
  text-decoration: underline;
}

.popular-link:hover {
  color: #f8f8f8;
}

/* Адаптивность */
@media (max-width: 768px) {
  .hero-section {
    height: 400px;
  }

  .hero-title {
    font-size: 2rem;
  }

  .search-tabs {
    overflow-x: auto;
    padding-bottom: 5px;
  }

  .search-bar {
    flex-direction: column;
  }

  .search-button {
    margin-left: 0;
    margin-top: 10px;
    width: 100%;
  }

  .popular-searches {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .popular-searches span {
    width: 100%;
    margin-bottom: 5px;
  }

  .popular-link {
    margin: 0 8px 5px 0;
  }
}
</style>