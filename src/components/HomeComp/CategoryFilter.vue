<template>
  <v-row class="mb-4">
    <v-col cols="12" md="6">
      <v-select v-model="selectedCategory" :items="categories" label="Категория" outlined
        @update:modelValue="$emit('update:modelValue', $event)"></v-select>
    </v-col>
    <v-col cols="12" md="6">
      <v-slider v-model="ratingFilter" label="Минимальный рейтинг" min="0" max="5" step="0.5" thumb-label
        @update:modelValue="$emit('rating-changed', $event)"></v-slider>
    </v-col>
  </v-row>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  categories: Array,
  modelValue: String
})

const emit = defineEmits(['update:modelValue', 'rating-changed'])

const selectedCategory = ref('all')
const ratingFilter = ref(0)
</script>