<template>
  <v-dialog v-model="show" max-width="800px">
    <v-card v-if="details">
      <v-card-title>Маршрут</v-card-title>
      <v-card-text>
        <div v-html="details.mapHtml"></div>
        <v-list>
          <v-list-item v-for="(step, i) in details.steps" :key="i">
            <v-list-item-content>
              <v-list-item-title>{{ step.instruction }}</v-list-item-title>
              <v-list-item-subtitle>{{ step.distance }} ({{ step.duration }})</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="$emit('close')">Закрыть</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
defineProps({
  details: Object
})

const emit = defineEmits(['close'])
</script>