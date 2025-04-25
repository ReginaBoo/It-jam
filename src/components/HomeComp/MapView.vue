<template>
  <div>
    <h1>Карта с категорией: {{ category }}</h1>
    <!-- Здесь будет ваша карта и список мест -->
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const category = computed(() => route.query.category)
</script>