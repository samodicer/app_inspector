<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat height="80px">
      <v-container class="py-0 fill-height">
        <router-link v-bind:to="'/'">
          <img src="../assets/images/logo2.png" height="70px" />
        </router-link>
        <v-spacer></v-spacer>
        <v-btn v-for="link in links" :key="link" text>
          {{ link }}
        </v-btn>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <!--<v-col cols="2">
            <v-sheet rounded="lg">
              <v-list color="transparent">
                <v-list-item v-for="n in 5" :key="n" link>
                  <v-list-item-content>
                    <v-list-item-title> List Item {{ n }} </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>

                <v-divider class="my-2"></v-divider>

                <v-list-item link color="grey lighten-4">
                  <v-list-item-content>
                    <v-list-item-title> Refresh </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>-->
          <v-col>
            <v-sheet
              id="sheet"
              min-height="70vh"
              rounded="lg"
              v-if="this.renderChart"
            >
              <v-col>
                <p>Build-in blocks</p>
                <BarChart
                  :chartData="this.chartData"
                  :chartOptions="this.chartOptions"
                  class="bar-chart"
                ></BarChart>
              </v-col>
              <v-col>
                <p>Component blocks</p>
                <BarChart
                  :chartData="this.chartData"
                  :chartOptions="this.chartOptions"
                  class="bar-chart"
                ></BarChart>
              </v-col>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex';
import BarChart from '../components/BarChart.vue';

export default {
  name: 'Overview',
  components: {
    BarChart,
  },
  data() {
    return {
      //analyzedData: Object,
      renderChart: false,
      links: ['Dashboard', 'Messages', 'Profile', 'Updates'],
      chartData: {
        labels: [],
        datasets: [
          {
            data: [],
            backgroundColor: [
              '#FBA92A',
              '#F54141',
              '#FFF80B',
              '#4BF148',
              '#EA2FCD',
              '#8934C8',
              '#1A90E7',
              '#0AD68F',
            ],
          },
        ],
      },
      chartOptions: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
          position: 'right',
          align: 'middle',
        },
      },
    };
  },
  computed: {
    ...mapGetters({
      getAnalyzedData: 'files/getAnalyzedData',
    }),
  },
  watch: {
    getAnalyzedData: function (val) {
      if (val) {
        for (const [key, value] of Object.entries(val[0].builtInBlocks)) {
          console.log(key, value);
          this.chartData.labels.push(key);
          this.chartData.datasets[0].data.push(value);
          this.renderChart = true;
        }
      }
    },
  },
};
</script>

<style scoped>
#inspire {
  text-align: center;
}
#sheet {
  padding: 30px;
}
.row {
  margin-bottom: 50px;
}
.bar-chart {
}
</style>
