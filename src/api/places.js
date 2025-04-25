// src/api/places.js

// Моковые данные для мест
const mockPlaces = [
  {
    id: 1,
    name: "Кофейня 'Уют'",
    category: "cafe",
    rating: 4.5,
    address: "ул. Примерная, 10",
    workingHours: "08:00 - 22:00",
    image: "https://source.unsplash.com/random/300x200/?cafe",
    reviews: [
      { id: 1, author: "Анна", rating: 5, text: "Отличный кофе!" },
      { id: 2, author: "Иван", rating: 4, text: "Уютное место" }
    ]
  },
  {
    id: 2,
    name: "Ресторан 'Гурман'",
    category: "restaurant",
    rating: 4.8,
    address: "ул. Центральная, 25",
    workingHours: "10:00 - 23:00",
    image: "https://source.unsplash.com/random/300x200/?restaurant",
    reviews: [
      { id: 3, author: "Мария", rating: 5, text: "Вкусная еда" }
    ]
  },
  // Добавьте другие места по аналогии
]

// Функция для получения мест с возможностью фильтрации
export const fetchPlaces = async (filters = {}) => {
  // Имитация задержки API
  await new Promise(resolve => setTimeout(resolve, 500));

  let result = [...mockPlaces];

  if (filters.category && filters.category !== 'all') {
    result = result.filter(place => place.category === filters.category);
  }

  if (filters.rating) {
    result = result.filter(place => place.rating >= filters.rating);
  }

  if (filters.searchQuery) {
    const query = filters.searchQuery.toLowerCase();
    result = result.filter(place =>
      place.name.toLowerCase().includes(query) ||
      place.address.toLowerCase().includes(query)
    );
  }

  return result;
}

// Функция для получения деталей места по ID
export const fetchPlaceDetails = async (id) => {
  await new Promise(resolve => setTimeout(resolve, 300));
  return mockPlaces.find(place => place.id === id);
}

// Функция для расчета маршрута (заглушка)
export const calculateRoute = async (from, to) => {
  await new Promise(resolve => setTimeout(resolve, 700));
  return {
    distance: "2.5 км",
    duration: "15 мин",
    steps: [
      { instruction: "Идите на север", distance: "200 м", duration: "3 мин" },
      { instruction: "Поверните направо", distance: "1 км", duration: "10 мин" },
      { instruction: "Место назначения слева", distance: "300 м", duration: "2 мин" }
    ],
    mapHtml: "<div style='color:gray;padding:20px;background:#f5f5f5;text-align:center;'>Здесь будет карта маршрута</div>"
  };
}