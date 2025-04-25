<template>
  <v-dialog v-model="show" max-width="600px">
    <v-card v-if="place">
      <v-img :src="place.image" height="300px"></v-img>
      <v-card-title>{{ place.name }}</v-card-title>
      <v-card-subtitle>
        <v-rating :value="place.rating" readonly half-increments color="amber"></v-rating>
        {{ place.rating }} ({{ place.reviewsCount }} отзывов)
      </v-card-subtitle>

      <v-card-text>
        <v-list>
          <v-list-item>
            <v-list-item-icon><v-icon>mdi-map-marker</v-icon></v-list-item-icon>
            <v-list-item-content>{{ place.address }}</v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-icon><v-icon>mdi-clock</v-icon></v-list-item-icon>
            <v-list-item-content>{{ place.workingHours }}</v-list-item-content>
          </v-list-item>
        </v-list>

        <h3 class="mt-4">Отзывы</h3>
        <v-textarea v-model="newReview" label="Ваш отзыв" outlined class="mt-2"></v-textarea>
        <v-rating v-model="newRating"></v-rating>
        <v-btn color="primary" @click="submitReview">Отправить отзыв</v-btn>
      </v-card-text>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="$emit('close')">Закрыть</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  place: Object
})

const emit = defineEmits(['close', 'add-review'])

const newReview = ref('')
const newRating = ref(0)

const submitReview = () => {
  emit('add-review', {
    text: newReview.value,
    rating: newRating.value
  })
  newReview.value = ''
  newRating.value = 0
}
</script>