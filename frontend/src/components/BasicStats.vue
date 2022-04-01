<template>
  <v-container>
    <v-row id="content" align="center" justify="space-between">
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
  flex-direction: column;
  align-items: center;
  width: 490px;
  height: 300px;
}
.card_title {
  font-weight: 700;
  font-size: 20px;
  margin-top: 30px;
}
.card_number {
  cursor: default;
  font-weight: 700;
  font-size: 60px;
  margin-top: 120px;
  position: absolute;
  transition: 0.5s;
}
.card_number:hover {
  cursor: default;
  font-weight: 700;
  font-size: 60px;
  color: #26a69a;
}
@media only screen and (max-width: 1264px) {
  #content {
    justify-content: center !important;
  }
}
@media only screen and (max-width: 600px) {
  #sheet {
    width: 300px;
  }
  #content {
    justify-content: center !important;
  }
}
@media only screen and (max-width: 450px) {
  #sheet {
    width: 200px;
  }
  #content {
    justify-content: center !important;
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
