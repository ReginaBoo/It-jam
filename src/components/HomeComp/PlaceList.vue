<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="6" md="4" lg="3" v-for="place in places" :key="place.id">
        <v-card @click="$emit('show-details', place)">
          <v-img :src="place.image" height="200px"></v-img>
          <v-card-title>{{ place.name }}</v-card-title>
          <v-card-subtitle>
            <v-rating :value="place.rating" readonly half-increments color="amber" dense size="18"></v-rating>
            ({{ place.rating }})
          </v-card-subtitle>
          <v-card-actions>
            <v-btn icon @click.stop="toggleFavorite(place)">
              <v-icon :color="isFavorite(place) ? 'red' : 'grey'">mdi-heart</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click.stop="$emit('show-details', place)">Подробнее</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
defineProps({
  places: Array,
  loading: Boolean
})

const emit = defineEmits(['show-details', 'toggle-favorite'])

const toggleFavorite = (place) => {
  emit('toggle-favorite', place)
}

const isFavorite = (place) => {
  // Логика проверки, есть ли место в избранном
  return false
}
</script>