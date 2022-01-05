<template>
  <v-container>
    <v-row align="center" justify="center">
      <div v-for="(number, title) in data" :key="title">
        <v-col id="col">
          <v-sheet id="sheet" rounded="lg" color="#F7F7F7" elevation="2">
            <div class="card_title">{{ title }}</div>
            <div class="card_number">{{ number }}</div>
          </v-sheet>
        </v-col>
      </div>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'BasicStats',
  props: ['data'],
  data() {
    return {
      dataLoaded: false,
    };
  },
};
</script>

<style scoped>
#sheet {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 400px;
  height: 300px;
}
.card_title {
  position: absolute;
  font-weight: 700;
  font-size: 20px;
  margin-bottom: 200px;
}
.card_number {
  cursor: default;
  font-weight: 700;
  font-size: 60px;
  transition: 0.5s;
}
.card_number:hover {
  cursor: default;
  font-weight: 700;
  font-size: 60px;
  color: #26a69a;
}
@media only screen and (max-width: 600px) {
  #sheet {
    width: 300px;
  }
}
@media only screen and (max-width: 450px) {
  #sheet {
    width: 200px;
  }
  .card_title {
    font-size: 14px;
  }
  .card_number {
    font-size: 50px;
  }
  .card_number:hover {
    font-size: 50px;
    color: #26a69a;
  }
}
</style>
