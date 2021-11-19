<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat height="80px">
      <v-container class="py-0 fill-height">
        <router-link v-bind:to="'/'">
          <img
            src="../assets/images/logo2.png"
            height="70px"
            @click="reloadPage"
          />
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
              <v-row>
                <v-col>
                  <v-sheet id="sheet" rounded="lg" color="#F7F7F7">
                    <p>Built-in blocks</p>
                    <DoughnutChart
                      :chartData="this.chartDataBuiltInBlocks"
                      :chartOptions="this.chartOptionsBuiltInBlocks"
                      class="doughnut-chart"
                    ></DoughnutChart>
                  </v-sheet>
                </v-col>
                <v-col>
                  <v-sheet id="sheet" rounded="lg" color="#F7F7F7">
                    <p>Component blocks</p>
                    <DoughnutChart
                      :chartData="this.chartDataComponentBlocks"
                      :chartOptions="this.chartOptionsComponentBlocks"
                      class="doughnut-chart"
                    ></DoughnutChart>
                  </v-sheet>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-sheet id="sheet" rounded="lg" color="#F7F7F7">
                    <p>Categories of component blocks</p>
                    <BarChart
                      :chartData="this.chartDataComponentBlocksCategories"
                      :chartOptions="this.chartOptionsComponentBlocksCategories"
                      class="doughnut-chart"
                    ></BarChart>
                  </v-sheet>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-sheet id="sheet" rounded="lg" color="#F7F7F7">
                    <p>User Interface component blocks</p>
                    <BarChart
                      :chartData="this.chartDataUIComponentBlocks"
                      :chartOptions="this.chartOptionsUIComponentBlocks"
                      class="doughnut-chart"
                    ></BarChart>
                  </v-sheet>
                </v-col>
              </v-row>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex';
import DoughnutChart from '../components/DoughnutChart.vue';
import BarChart from '../components/BarChart.vue';

export default {
  name: 'Overview',
  components: {
    DoughnutChart,
    BarChart,
  },
  data() {
    return {
      //analyzedData: Object,
      renderChart: false,
      links: ['Dashboard', 'Messages', 'Profile', 'Updates'],
      chartDataBuiltInBlocks: {
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
      chartDataComponentBlocks: {
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
      chartDataComponentBlocksCategories: {
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
              '#04B9C8',
              '#9D9D9D',
              '#E670B8',
              '#764903',
              '#C296E1',
              '#000000',
              '#F15757',
            ],
          },
        ],
      },

      chartDataUIComponentBlocks: {
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
              '#04B9C8',
              '#9D9D9D',
              '#E670B8',
              '#764903',
              '#C296E1',
              '#000000',
              '#F15757',
            ],
          },
        ],
      },
      chartOptionsBuiltInBlocks: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
          position: 'right',
          align: 'middle',
        },
      },
      chartOptionsComponentBlocks: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
          position: 'right',
          align: 'middle',
        },
      },
      chartOptionsComponentBlocksCategories: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
          display: false,
        },
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },

      chartOptionsUIComponentBlocks: {
        maintainAspectRatio: false,
        responsive: true,
        legend: {
          display: false,
        },
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
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
          this.chartDataBuiltInBlocks.labels.push(key);
          this.chartDataBuiltInBlocks.datasets[0].data.push(value);
        }
        for (const [key, value] of Object.entries(val[0].componentBlocks)) {
          console.log(key, value);
          this.chartDataComponentBlocks.labels.push(key);
          this.chartDataComponentBlocks.datasets[0].data.push(value);
        }
        for (const [key, value] of Object.entries(
          val[0].componentBlocksCategories
        )) {
          console.log(key, value);
          this.chartDataComponentBlocksCategories.labels.push(key);
          this.chartDataComponentBlocksCategories.datasets[0].data.push(value);
        }
        for (const [key, value] of Object.entries(
          val[0].userInterfaceComponentBlocks
        )) {
          console.log(key, value);
          this.chartDataUIComponentBlocks.labels.push(key);
          this.chartDataUIComponentBlocks.datasets[0].data.push(value);
        }
        this.renderChart = true;
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
</style>
