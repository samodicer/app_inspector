<template>
  <v-app id="inspire">
    <Navbar></Navbar>
    <v-main id="main" class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col>
            <v-sheet
              id="sheet"
              min-height="70vh"
              rounded="lg"
              v-if="this.renderChart"
            >
              <v-row style="margin-bottom: 0px">
                <v-col class="text-right">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <v-icon
                        id="icon"
                        x-large
                        v-bind="attrs"
                        v-on="on"
                        @click="openSettings()"
                      >
                        mdi-cog
                      </v-icon>
                    </template>
                    <span style="font-size: 12px">Settings</span>
                  </v-tooltip>
                  <div v-if="settingsDialog">
                    <v-dialog
                      v-model="settingsDialog"
                      fullscreen
                      hide-overlay
                      transition="dialog-bottom-transition"
                    >
                      <v-card>
                        <v-toolbar dark color="#26a69a">
                          <v-toolbar-title>Settings</v-toolbar-title>
                          <v-spacer></v-spacer>
                          <v-toolbar-items>
                            <v-btn dark text @click="settingsDialog = false">
                              <v-icon>mdi-close</v-icon>
                            </v-btn>
                          </v-toolbar-items>
                        </v-toolbar>
                        <div class="selectFiles">
                          <SelectFiles></SelectFiles>
                        </div>
                      </v-card>
                    </v-dialog>
                  </div>
                </v-col>
              </v-row>
              <v-divider id="divider"></v-divider>
              <v-row>
                <v-col>
                  <v-card id="card">
                    <v-row
                      style="
                        display: flex;
                        justify-content: end;
                        align-items: center;
                        flex-direction: row;
                        margin-bottom: 0px;
                      "
                    >
                      <v-tooltip bottom>
                        <template v-slot:activator="{ on, attrs }">
                          <v-icon
                            id="icon"
                            x-large
                            @click="downloadOverallStats()"
                            v-bind="attrs"
                            v-on="on"
                          >
                            mdi-download
                          </v-icon>
                        </template>
                        <span style="font-size: 12px"
                          >Export overall statistics to CSV</span
                        >
                      </v-tooltip>
                    </v-row>
                    <h1 id="heading">
                      <v-icon large color="#26a69a">
                        mdi-chart-timeline-variant
                      </v-icon>
                      Overall statistics
                    </h1>

                    <v-row v-if="this.basicStats != null">
                      <v-col>
                        <BasicStats :data="this.basicStats"></BasicStats>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-sheet
                          id="sheet"
                          rounded="lg"
                          color="#F7F7F7"
                          height="100%"
                          elevation="2"
                        >
                          <p class="card_title">Built-in blocks</p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataBuiltInBlocks.data
                              ) != 0
                            "
                          >
                            <DoughnutChart
                              :chartData="this.chartDataBuiltInBlocks.data"
                              :chartLabels="this.chartDataBuiltInBlocks.labels"
                              class="doughnut-chart"
                            ></DoughnutChart>
                          </div>
                          <div id="noData" v-else>
                            <v-icon x-large> mdi-eye-off </v-icon>
                            <p>No data to analyse</p>
                          </div>
                        </v-sheet>
                      </v-col>
                      <v-col>
                        <v-sheet
                          id="sheet"
                          rounded="lg"
                          color="#F7F7F7"
                          height="100%"
                          elevation="2"
                        >
                          <p class="card_title">Component blocks</p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataComponentBlocks.data
                              ) != 0
                            "
                          >
                            <DoughnutChart
                              :chartData="this.chartDataComponentBlocks.data"
                              :chartLabels="
                                this.chartDataComponentBlocks.labels
                              "
                              class="doughnut-chart"
                            ></DoughnutChart>
                          </div>
                          <div id="noData" v-else>
                            <v-icon x-large> mdi-eye-off </v-icon>
                            <p>No data to analyse</p>
                          </div>
                        </v-sheet>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-sheet
                          id="sheet"
                          rounded="lg"
                          color="#F7F7F7"
                          height="100%"
                          elevation="2"
                        >
                          <p class="card_title">Component blocks types</p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataComponentBlocksCategories.data
                              ) != 0
                            "
                          >
                            <LineChart
                              :chartData="
                                this.chartDataComponentBlocksCategories.data
                              "
                              :chartLabels="
                                this.chartDataComponentBlocksCategories.labels
                              "
                              class="bar-chart"
                            ></LineChart>
                          </div>
                          <div id="noData" v-else>
                            <v-icon x-large> mdi-eye-off </v-icon>
                            <p>No data to analyse</p>
                          </div>
                        </v-sheet>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-sheet
                          id="sheet"
                          rounded="lg"
                          color="#F7F7F7"
                          height="100%"
                          elevation="2"
                        >
                          <p class="card_title">
                            User Interface component blocks
                          </p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataUIComponentBlocks.data
                              ) != 0
                            "
                          >
                            <LineChart
                              :chartData="this.chartDataUIComponentBlocks.data"
                              :chartLabels="
                                this.chartDataUIComponentBlocks.labels
                              "
                              class="bar-chart"
                            ></LineChart>
                          </div>
                          <div id="noData" v-else>
                            <v-icon x-large> mdi-eye-off </v-icon>
                            <p>No data to analyse</p>
                          </div>
                        </v-sheet>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-sheet
                          id="sheet"
                          rounded="lg"
                          color="#F7F7F7"
                          height="100%"
                          elevation="2"
                        >
                          <p class="card_title">
                            Drawing and Animation component blocks
                          </p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataDrawAndAnimComponentBlocks.data
                              ) != 0
                            "
                          >
                            <PieChart
                              :chartData="
                                this.chartDataDrawAndAnimComponentBlocks.data
                              "
                              :chartLabels="
                                this.chartDataDrawAndAnimComponentBlocks.labels
                              "
                              class="pie-chart"
                            ></PieChart>
                          </div>
                          <div id="noData" v-else>
                            <v-icon x-large> mdi-eye-off </v-icon>
                            <p>No data to analyse</p>
                          </div>
                        </v-sheet>
                      </v-col>
                      <v-col>
                        <v-sheet
                          id="sheet"
                          rounded="lg"
                          color="#F7F7F7"
                          height="100%"
                          elevation="2"
                        >
                          <p class="card_title">
                            Storage and Experimental component blocks
                          </p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataStorageAndExpComponentBlocks.data
                              ) != 0
                            "
                          >
                            <PieChart
                              :chartData="
                                this.chartDataStorageAndExpComponentBlocks.data
                              "
                              :chartLabels="
                                this.chartDataStorageAndExpComponentBlocks
                                  .labels
                              "
                              class="pie-chart"
                            ></PieChart>
                          </div>
                          <div id="noData" v-else>
                            <v-icon x-large> mdi-eye-off </v-icon>
                            <p>No data to analyse</p>
                          </div>
                        </v-sheet>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-sheet
                          id="sheet"
                          rounded="lg"
                          color="#F7F7F7"
                          height="100%"
                          elevation="2"
                        >
                          <p class="card_title">Control blocks types</p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataControlBlocksTypes.data
                              ) != 0
                            "
                          >
                            <PieChart
                              :chartData="this.chartDataControlBlocksTypes.data"
                              :chartLabels="
                                this.chartDataControlBlocksTypes.labels
                              "
                              class="pie-chart"
                            ></PieChart>
                          </div>
                          <div id="noData" v-else>
                            <v-icon x-large> mdi-eye-off </v-icon>
                            <p>No data to analyse</p>
                          </div>
                        </v-sheet>
                      </v-col>
                      <v-col>
                        <v-sheet
                          id="sheet"
                          rounded="lg"
                          color="#F7F7F7"
                          height="100%"
                          elevation="2"
                        >
                          <p class="card_title">Procedure blocks types</p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataProcedureBlocksTypes.data
                              ) != 0
                            "
                          >
                            <PieChart
                              :chartData="
                                this.chartDataProcedureBlocksTypes.data
                              "
                              :chartLabels="
                                this.chartDataProcedureBlocksTypes.labels
                              "
                              class="pie-chart"
                            ></PieChart>
                          </div>
                          <div id="noData" v-else>
                            <v-icon x-large> mdi-eye-off </v-icon>
                            <p>No data to analyse</p>
                          </div>
                        </v-sheet>
                      </v-col>
                    </v-row>
                  </v-card>
                  <v-card id="card" v-if="this.numberOfProjects > 1">
                    <v-row
                      style="
                        display: flex;
                        justify-content: end;
                        align-items: center;
                        flex-direction: row;
                        margin-bottom: 0px;
                      "
                    >
                      <v-tooltip bottom>
                        <template v-slot:activator="{ on, attrs }">
                          <v-icon
                            id="icon"
                            x-large
                            @click="downloadProjectComparison()"
                            v-bind="attrs"
                            v-on="on"
                          >
                            mdi-download
                          </v-icon>
                        </template>
                        <span style="font-size: 12px"
                          >Export project comparison to CSV</span
                        >
                      </v-tooltip>
                    </v-row>
                    <h1 id="heading">
                      <v-icon large color="#26a69a"> mdi-compare </v-icon>
                      Project comparison
                    </h1>
                    <v-row>
                      <v-col>
                        <v-sheet
                          id="sheet"
                          rounded="lg"
                          color="#F7F7F7"
                          height="100%"
                          elevation="2"
                        >
                          <v-select
                            :items="items"
                            color="#26a69a"
                            label="Compare by"
                            v-model="compareBy"
                          ></v-select>
                          <p class="card_title">{{ compareBy }}</p>
                          <div
                            v-if="
                              this.sumOfArray(this.chartCompareBy.data) != 0
                            "
                          >
                            <BarChart
                              :chartData="this.chartCompareBy.data"
                              :chartLabels="this.chartCompareBy.labels"
                              class="bar-chart"
                            ></BarChart>
                          </div>
                          <div id="noData" style="margin-bottom: 60px" v-else>
                            <v-icon x-large> mdi-eye-off </v-icon>
                            <p>No data to compare</p>
                          </div>
                        </v-sheet>
                      </v-col>
                    </v-row>
                  </v-card>
                </v-col>
              </v-row>
            </v-sheet>
            <v-sheet id="sheet" min-height="63vh" rounded="lg" v-else>
              <v-icon style="margin-top: 50px" x-large> mdi-eye-off</v-icon>
              <p>No data to analyse</p>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
      <Footer></Footer>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import Navbar from '../components/Navbar.vue';
import DoughnutChart from '../components/DoughnutChart.vue';
import BarChart from '../components/BarChart.vue';
import SelectFiles from '../components/SelectFiles.vue';
import BasicStats from '../components/BasicStats.vue';
import PieChart from '../components/PieChart.vue';
import LineChart from '../components/LineChart.vue';
import Footer from '../components/Footer.vue';
import exportFromJSON from 'export-from-json';

export default {
  name: 'Overview',
  components: {
    Navbar,
    Footer,
    DoughnutChart,
    BarChart,
    PieChart,
    LineChart,
    SelectFiles,
    BasicStats,
  },
  data() {
    return {
      numberOfProjects: 0,
      renderChart: false,
      settingsDialog: false,
      sumValues: (obj) => Object.values(obj).reduce((a, b) => a + b),
      items: [],
      compareBy: '',
      chartDataBuiltInBlocks: {
        labels: [],
        data: [],
      },
      chartDataComponentBlocks: {
        labels: [],
        data: [],
      },
      chartDataComponentBlocksCategories: {
        labels: [],
        data: [],
      },
      chartDataUIComponentBlocks: {
        labels: [],
        data: [],
      },
      chartDataDrawAndAnimComponentBlocks: {
        labels: [],
        data: [],
      },
      chartDataStorageAndExpComponentBlocks: {
        labels: [],
        data: [],
      },
      chartDataControlBlocksTypes: {
        labels: [],
        data: [],
      },
      chartDataProcedureBlocksTypes: {
        labels: [],
        data: [],
      },
      chartDataBlocksPerProject: {
        labels: [],
        data: [],
      },
      chartDataComponentsPerProject: {
        labels: [],
        data: [],
      },
      chartDataScreensPerProject: {
        labels: [],
        data: [],
      },
      chartCompareBy: {
        labels: [],
        data: [],
      },
      exportProjectComparison: [],
      exportOverallStats: [],
    };
  },
  computed: {
    ...mapGetters({
      getAnalysedData: 'files/getAnalysedData',
      getAnalysed: 'files/getAnalysed',
    }),
  },
  methods: {
    ...mapActions({
      changeAnalysed: 'files/changeAnalysed',
    }),
    setChartData(val) {
      this.basicStats = val[0].basicStats;

      // naplníme názvy a hodnoty pomocou dát zo servera
      for (const [key, value] of Object.entries(val[0].basicStats)) {
        if (key == 'Number of projects') {
          this.numberOfProjects = value;
        }
        const obj = {};
        obj.Parameter = 'Basic stats - ' + key;
        obj.Value = value;
        this.exportOverallStats.push(obj);
      }

      for (const [key, value] of Object.entries(val[0].builtInBlocks)) {
        this.chartDataBuiltInBlocks.labels.push(key);
        this.chartDataBuiltInBlocks.data.push(value);
        const obj = {};
        obj.Parameter = 'Built-in blocks - ' + key;
        obj.Value = value;
        this.exportOverallStats.push(obj);
      }

      for (const [key, value] of Object.entries(val[0].componentBlocks)) {
        this.chartDataComponentBlocks.labels.push(key);
        this.chartDataComponentBlocks.data.push(value);
        const obj = {};
        obj.Parameter = 'Component blocks - ' + key;
        obj.Value = value;
        this.exportOverallStats.push(obj);
      }

      for (const [key, value] of Object.entries(
        val[0].componentBlocksCategories
      )) {
        this.chartDataComponentBlocksCategories.labels.push(key);
        this.chartDataComponentBlocksCategories.data.push(value);
        const obj = {};
        obj.Parameter = 'Component blocks types - ' + key;
        obj.Value = value;
        this.exportOverallStats.push(obj);
      }

      for (const [key, value] of Object.entries(
        val[0].userInterfaceComponentBlocks
      )) {
        this.chartDataUIComponentBlocks.labels.push(key);
        this.chartDataUIComponentBlocks.data.push(value);
        const obj = {};
        obj.Parameter = 'User Interface component blocks - ' + key;
        obj.Value = value;
        this.exportOverallStats.push(obj);
      }

      for (const [key, value] of Object.entries(
        val[0].drawingAndAnimationComponentBlocks
      )) {
        this.chartDataDrawAndAnimComponentBlocks.labels.push(key);
        this.chartDataDrawAndAnimComponentBlocks.data.push(value);
        const obj = {};
        obj.Parameter = 'Drawing and Animation component blocks - ' + key;
        obj.Value = value;
        this.exportOverallStats.push(obj);
      }

      for (const [key, value] of Object.entries(
        val[0].storageAndExperimentalComponentBlocks
      )) {
        this.chartDataStorageAndExpComponentBlocks.labels.push(key);
        this.chartDataStorageAndExpComponentBlocks.data.push(value);
        const obj = {};
        obj.Parameter = 'Storage and Experimental component blocks - ' + key;
        obj.Value = value;
        this.exportOverallStats.push(obj);
      }

      for (const [key, value] of Object.entries(val[0].controlBlocksTypes)) {
        this.chartDataControlBlocksTypes.labels.push(key);
        this.chartDataControlBlocksTypes.data.push(value);
        const obj = {};
        obj.Parameter = 'Control blocks types - ' + key;
        obj.Value = value;
        this.exportOverallStats.push(obj);
      }

      for (const [key, value] of Object.entries(val[0].procedureBlocksTypes)) {
        this.chartDataProcedureBlocksTypes.labels.push(key);
        this.chartDataProcedureBlocksTypes.data.push(value);
        const obj = {};
        obj.Parameter = 'Procedure blocks types - ' + key;
        obj.Value = value;
        this.exportOverallStats.push(obj);
      }

      for (const [key, value] of Object.entries(val[0].blocksPerProject)) {
        this.chartDataBlocksPerProject.labels.push(key);
        this.chartDataBlocksPerProject.data.push(value);
      }

      for (const [key, value] of Object.entries(val[0].componentsPerProject)) {
        this.chartDataComponentsPerProject.labels.push(key);
        this.chartDataComponentsPerProject.data.push(value);
      }

      for (const [key, value] of Object.entries(val[0].screensPerProject)) {
        this.chartDataScreensPerProject.labels.push(key);
        this.chartDataScreensPerProject.data.push(value);
      }
    },
    sortData(type, labels, data) {
      // vytvoríme objekt
      var chartObj = labels.map(function (d, i) {
        return {
          label: d,
          data: data[i] || 0,
        };
      });

      // zoradíme dáta
      var sortedChartObj = chartObj.sort(function (a, b) {
        return b.data - a.data;
      });

      // naplníme polia usporiadanými názvami a hodnotami
      var sortedLabels = [];
      var sortedData = [];
      sortedChartObj.forEach(function (d) {
        sortedLabels.push(d.label);
        sortedData.push(d.data);
      });

      // nastavíme dáta pre každý typ
      switch (type) {
        case 'builtInBlocks':
          this.chartDataBuiltInBlocks.labels = sortedLabels;
          this.chartDataBuiltInBlocks.data = sortedData;
          break;
        case 'componentBlocks':
          this.chartDataComponentBlocks.labels = sortedLabels;
          this.chartDataComponentBlocks.data = sortedData;
          break;
        case 'componentBlocksCategories':
          this.chartDataComponentBlocksCategories.labels = sortedLabels;
          this.chartDataComponentBlocksCategories.data = sortedData;
          break;
        case 'userInterfaceComponentBlocks':
          this.chartDataUIComponentBlocks.labels = sortedLabels;
          this.chartDataUIComponentBlocks.data = sortedData;
          break;
        case 'drawingAndAnimationComponentBlocks':
          this.chartDataDrawAndAnimComponentBlocks.labels = sortedLabels;
          this.chartDataDrawAndAnimComponentBlocks.data = sortedData;
          break;
        case 'storageAndExperimentalComponentBlocks':
          this.chartDataStorageAndExpComponentBlocks.labels = sortedLabels;
          this.chartDataStorageAndExpComponentBlocks.data = sortedData;
          break;
        case 'controlBlocksTypes':
          this.chartDataControlBlocksTypes.labels = sortedLabels;
          this.chartDataControlBlocksTypes.data = sortedData;
          break;
        case 'procedureBlocksType':
          this.chartDataProcedureBlocksTypes.labels = sortedLabels;
          this.chartDataProcedureBlocksTypes.data = sortedData;
          break;
        case 'blocksPerProject':
          this.chartDataBlocksPerProject.labels = sortedLabels;
          this.chartDataBlocksPerProject.data = sortedData;
          break;
        case 'componentsPerProject':
          this.chartDataComponentsPerProject.labels = sortedLabels;
          this.chartDataComponentsPerProject.data = sortedData;
          break;
        case 'screensPerProject':
          this.chartDataScreensPerProject.labels = sortedLabels;
          this.chartDataScreensPerProject.data = sortedData;
          break;
        case 'compareBy':
          this.chartCompareBy.labels = sortedLabels;
          this.chartCompareBy.data = sortedData;
          break;
      }
    },
    setData(val) {
      // nastavíme dáta pre názvy a hodnoty grafov
      this.setChartData(val);

      // usporidame všetky dáta
      this.sortData(
        'builtInBlocks',
        this.chartDataBuiltInBlocks.labels,
        this.chartDataBuiltInBlocks.data
      );
      this.sortData(
        'componentBlocks',
        this.chartDataComponentBlocks.labels,
        this.chartDataComponentBlocks.data
      );
      this.sortData(
        'componentBlocksCategories',
        this.chartDataComponentBlocksCategories.labels,
        this.chartDataComponentBlocksCategories.data
      );
      this.sortData(
        'userInterfaceComponentBlocks',
        this.chartDataUIComponentBlocks.labels,
        this.chartDataUIComponentBlocks.data
      );
      this.sortData(
        'drawingAndAnimationComponentBlocks',
        this.chartDataDrawAndAnimComponentBlocks.labels,
        this.chartDataDrawAndAnimComponentBlocks.data
      );
      this.sortData(
        'storageAndExperimentalComponentBlocks',
        this.chartDataStorageAndExpComponentBlocks.labels,
        this.chartDataStorageAndExpComponentBlocks.data
      );
      this.sortData(
        'controlBlocksTypes',
        this.chartDataControlBlocksTypes.labels,
        this.chartDataControlBlocksTypes.data
      );

      this.sortData(
        'procedureBlocksType',
        this.chartDataProcedureBlocksTypes.labels,
        this.chartDataProcedureBlocksTypes.data
      );

      this.sortData(
        'blocksPerProject',
        this.chartDataBlocksPerProject.labels,
        this.chartDataBlocksPerProject.data
      );

      this.sortData(
        'componentsPerProject',
        this.chartDataComponentsPerProject.labels,
        this.chartDataComponentsPerProject.data
      );

      this.sortData(
        'screensPerProject',
        this.chartDataScreensPerProject.labels,
        this.chartDataScreensPerProject.data
      );
      // vykreslíme grafy
      this.renderChart = true;
    },
    renderProjectComparison(val) {
      this.chartCompareBy.labels = [];
      this.chartCompareBy.data = [];
      switch (this.compareBy) {
        case 'Blocks per project':
          for (const [key, value] of Object.entries(val[0].blocksPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Components per project':
          for (const [key, value] of Object.entries(
            val[0].componentsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Screens per project':
          for (const [key, value] of Object.entries(val[0].screensPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - Button blocks per project':
          for (const [key, value] of Object.entries(val[0].buttonsPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - Checkbox blocks per project':
          for (const [key, value] of Object.entries(
            val[0].checkboxesPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - DatePicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].datepickersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - Image blocks per project':
          for (const [key, value] of Object.entries(val[0].imagesPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - Label blocks per project':
          for (const [key, value] of Object.entries(val[0].labelsPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - ListPicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].listpickersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - ListView blocks per project':
          for (const [key, value] of Object.entries(
            val[0].listviewsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - Notifier blocks per project':
          for (const [key, value] of Object.entries(
            val[0].notifiersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - PasswordTextBox blocks per project':
          for (const [key, value] of Object.entries(
            val[0].passwordtextboxesPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - Slider blocks per project':
          for (const [key, value] of Object.entries(val[0].slidersPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - Spinner blocks per project':
          for (const [key, value] of Object.entries(
            val[0].spinnersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - Switch blocks per project':
          for (const [key, value] of Object.entries(
            val[0].switchesPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - TextBox blocks per project':
          for (const [key, value] of Object.entries(
            val[0].textboxesPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - TimePicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].timepickersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'User Interface - WebViewer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].webviewersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Layout - HorizontalArrangment blocks per project':
          for (const [key, value] of Object.entries(
            val[0].horizontalArrangmentPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Layout - HorizontalScrollArrangment blocks per project':
          for (const [key, value] of Object.entries(
            val[0].horizontalScrollArrangmentPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Layout - TableArrangment blocks per project':
          for (const [key, value] of Object.entries(
            val[0].tableArrangmentPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Layout - VerticalArrangment blocks per project':
          for (const [key, value] of Object.entries(
            val[0].verticalArrangmentPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Layout - VerticalScrollArrangment blocks per project':
          for (const [key, value] of Object.entries(
            val[0].verticalScrollArrangmentPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Media - Camcorder blocks per project':
          for (const [key, value] of Object.entries(
            val[0].camcordersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Media - Camera blocks per project':
          for (const [key, value] of Object.entries(val[0].camerasPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Media - ImagePicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].imagepickersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Media - Player blocks per project':
          for (const [key, value] of Object.entries(val[0].playersPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Media - Sound blocks per project':
          for (const [key, value] of Object.entries(val[0].soundsPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Media - SoundRecorder blocks per project':
          for (const [key, value] of Object.entries(
            val[0].soundrecordersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Media - SpeechRecognizer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].speechrecognizersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Media - TextToSpeech blocks per project':
          for (const [key, value] of Object.entries(
            val[0].texttospeechsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Media - VideoPlayer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].videoplayersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Media - YandexTranslate blocks per project':
          for (const [key, value] of Object.entries(
            val[0].yandextranslatorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Drawing and Animation - Ball blocks per project':
          for (const [key, value] of Object.entries(val[0].ballsPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Drawing and Animation - Canvas blocks per project':
          for (const [key, value] of Object.entries(
            val[0].canvasesPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Drawing and Animation - ImageSprite blocks per project':
          for (const [key, value] of Object.entries(
            val[0].imagespritesPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Maps - Circle blocks per project':
          for (const [key, value] of Object.entries(val[0].circlesPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Maps - FeatureCollection blocks per project':
          for (const [key, value] of Object.entries(
            val[0].featurecollectionsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Maps - Map blocks per project':
          for (const [key, value] of Object.entries(val[0].mapsPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Maps - Marker blocks per project':
          for (const [key, value] of Object.entries(val[0].markersPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Maps - Navigation blocks per project':
          for (const [key, value] of Object.entries(
            val[0].navigationsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Maps - Polygon blocks per project':
          for (const [key, value] of Object.entries(
            val[0].polygonsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Maps - Rectangle blocks per project':
          for (const [key, value] of Object.entries(
            val[0].rectanglesPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - AccelerometerSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].accelerometerSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - BarcodeScanner blocks per project':
          for (const [key, value] of Object.entries(
            val[0].barcodeScannersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - Barometer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].barometersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - Clock blocks per project':
          for (const [key, value] of Object.entries(val[0].clocksPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - GyroscopeSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].gyroscopeSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - Hygrometer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].hygrometersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - LightSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].lightSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - LocationSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].locationSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - MagneticFieldSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].magneticFieldSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - NearField blocks per project':
          for (const [key, value] of Object.entries(
            val[0].nearFieldsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - OrientationSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].orientationSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - Pedometer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].pedometersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - ProximitySensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].proximitySensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Sensors - Thermometer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].thermometersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Social - ContactPicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].contactPickersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Social - EmailPicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].emailPickersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Social - PhoneCall blocks per project':
          for (const [key, value] of Object.entries(
            val[0].phoneCallsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Social - PhoneNumberPicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].phoneNumberPickersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Social - Sharing blocks per project':
          for (const [key, value] of Object.entries(
            val[0].sharingsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Social - Texting blocks per project':
          for (const [key, value] of Object.entries(
            val[0].textingsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Social - Twitter blocks per project':
          for (const [key, value] of Object.entries(
            val[0].twittersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Storage - CloudDB blocks per project':
          for (const [key, value] of Object.entries(
            val[0].cloudDbsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Storage - File blocks per project':
          for (const [key, value] of Object.entries(val[0].filesPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Storage - TinyDB blocks per project':
          for (const [key, value] of Object.entries(val[0].tinyDbsPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Storage - TinyWebDB blocks per project':
          for (const [key, value] of Object.entries(
            val[0].tinyWebDbsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Connectivity - ActivityStarter blocks per project':
          for (const [key, value] of Object.entries(
            val[0].activityStartersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Connectivity - BluetoothClient blocks per project':
          for (const [key, value] of Object.entries(
            val[0].bluetoothClientsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Connectivity - BluetoothServer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].bluetoothServersPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Connectivity - Serial blocks per project':
          for (const [key, value] of Object.entries(val[0].serialsPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Connectivity - Web blocks per project':
          for (const [key, value] of Object.entries(val[0].websPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - NxtDrive blocks per project':
          for (const [key, value] of Object.entries(
            val[0].nxtDrivesPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - NxtColorSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].nxtColorSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - NxtLightSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].nxtLightSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - NxtSoundSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].nxtSoundSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - NxtTouchSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].nxtTouchSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - NxtUltrasonicSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].nxtUltrasonicSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - NxtDirectCommands blocks per project':
          for (const [key, value] of Object.entries(
            val[0].nxtDirectCommandsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - Ev3Motors blocks per project':
          for (const [key, value] of Object.entries(
            val[0].ev3MotorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - Ev3ColorSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].ev3ColorSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - Ev3GyroSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].ev3GyroSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - Ev3TouchSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].ev3TouchSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - Ev3UltrasonicSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].ev3UltrasonicSensorsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - Ev3Sound blocks per project':
          for (const [key, value] of Object.entries(
            val[0].ev3SoundsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - Ev3UI blocks per project':
          for (const [key, value] of Object.entries(val[0].ev3UIsPerProject)) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'LEGO MINDSTORMS - Ev3Commands blocks per project':
          for (const [key, value] of Object.entries(
            val[0].ev3CommandsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
        case 'Experimental - FirebaseDB blocks per project':
          for (const [key, value] of Object.entries(
            val[0].firebaseDbsPerProject
          )) {
            this.chartCompareBy.labels.push(key);
            this.chartCompareBy.data.push(value);
          }
          break;
      }
      this.sortData(
        'compareBy',
        this.chartCompareBy.labels,
        this.chartCompareBy.data
      );
    },
    setProjectComparisonExport(val) {
      var result;
      if (this.sumValues(val[0].blocksPerProject) != 0) {
        this.items.push('Blocks per project');
        for (const [key, value] of Object.entries(val[0].blocksPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].blocksPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].componentsPerProject) != 0) {
        this.items.push('Components per project');
        for (const [key, value] of Object.entries(
          val[0].componentsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].componentsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Components = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Components = value;
          }
        }
      }
      if (this.sumValues(val[0].screensPerProject) != 0) {
        this.items.push('Screens per project');
        for (const [key, value] of Object.entries(val[0].screensPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].screensPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Screens = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Screens = value;
          }
        }
      }
      if (this.sumValues(val[0].buttonsPerProject) != 0) {
        this.items.push('User Interface - Button blocks per project');
        for (const [key, value] of Object.entries(val[0].buttonsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].buttonsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Button_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Button_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].checkboxesPerProject) != 0) {
        this.items.push('User Interface - Checkbox blocks per project');
        for (const [key, value] of Object.entries(
          val[0].checkboxesPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].checkboxesPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.CheckBox_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.CheckBox_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].datepickersPerProject) != 0) {
        this.items.push('User Interface - DatePicker blocks per project');
        for (const [key, value] of Object.entries(
          val[0].datepickersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].datepickersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.DatePicker_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.DatePicker_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].imagesPerProject) != 0) {
        this.items.push('User Interface - Image blocks per project');
        for (const [key, value] of Object.entries(val[0].imagesPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].imagesPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Image_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Image_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].labelsPerProject) != 0) {
        this.items.push('User Interface - Label blocks per project');
        for (const [key, value] of Object.entries(val[0].labelsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].labelsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Label_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Label_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].listpickersPerProject) != 0) {
        this.items.push('User Interface - ListPicker blocks per project');
        for (const [key, value] of Object.entries(
          val[0].listpickersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].listpickersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.ListPicker_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.ListPicker_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].listviewsPerProject) != 0) {
        this.items.push('User Interface - ListView blocks per project');
        for (const [key, value] of Object.entries(val[0].listviewsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].listviewsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.ListView_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.ListView_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].notifiersPerProject) != 0) {
        this.items.push('User Interface - Notifier blocks per project');
        for (const [key, value] of Object.entries(val[0].notifiersPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].notifiersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Notifier_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Notifier_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].passwordtextboxesPerProject) != 0) {
        this.items.push('User Interface - PasswordTextBox blocks per project');
        for (const [key, value] of Object.entries(
          val[0].passwordtextboxesPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].passwordtextboxesPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.PasswordTextBox_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.PasswordTextBox_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].slidersPerProject) != 0) {
        this.items.push('User Interface - Slider blocks per project');
        for (const [key, value] of Object.entries(val[0].slidersPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].slidersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Slider_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Slider_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].spinnersPerProject) != 0) {
        this.items.push('User Interface - Spinner blocks per project');
        for (const [key, value] of Object.entries(val[0].spinnersPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].spinnersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Spinner_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Spinner_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].switchesPerProject) != 0) {
        this.items.push('User Interface - Switch blocks per project');
        for (const [key, value] of Object.entries(val[0].switchesPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].switchesPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Switch_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Switch_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].textboxesPerProject) != 0) {
        this.items.push('User Interface - TextBox blocks per project');
        for (const [key, value] of Object.entries(val[0].textboxesPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].textboxesPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.TextBox_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.TextBox_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].timepickersPerProject) != 0) {
        this.items.push('User Interface - TimePicker blocks per project');
        for (const [key, value] of Object.entries(
          val[0].timepickersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].timepickersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.TimePicker_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.TimePicker_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].webviewersPerProject) != 0) {
        this.items.push('User Interface - WebViewer blocks per project');
        for (const [key, value] of Object.entries(
          val[0].webviewersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].webviewersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.WebViewer_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.WebViewer_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].horizontalArrangmentPerProject) != 0) {
        this.items.push('Layout - HorizontalArrangment blocks per project');
        for (const [key, value] of Object.entries(
          val[0].horizontalArrangmentPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].horizontalArrangmentPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.HorizontalArrangment_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.HorizontalArrangment_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].horizontalScrollArrangmentPerProject) != 0) {
        this.items.push(
          'Layout - HorizontalScrollArrangment blocks per project'
        );
        for (const [key, value] of Object.entries(
          val[0].horizontalScrollArrangmentPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].horizontalScrollArrangmentPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.HorizontalScrollArrangment_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.HorizontalScrollArrangment_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].tableArrangmentPerProject) != 0) {
        this.items.push('Layout - TableArrangment blocks per project');
        for (const [key, value] of Object.entries(
          val[0].tableArrangmentPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].tableArrangmentPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.TableArrangment_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.TableArrangment_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].verticalArrangmentPerProject) != 0) {
        this.items.push('Layout - VerticalArrangment blocks per project');
        for (const [key, value] of Object.entries(
          val[0].verticalArrangmentPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].verticalArrangmentPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.VerticalArrangment_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.VerticalArrangment_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].verticalScrollArrangmentPerProject) != 0) {
        this.items.push('Layout - VerticalScrollArrangment blocks per project');
        for (const [key, value] of Object.entries(
          val[0].verticalScrollArrangmentPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].verticalScrollArrangmentPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.VerticalScrollArrangment_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.VerticalScrollArrangment_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].camcordersPerProject) != 0) {
        this.items.push('Media - Camcorder blocks per project');
        for (const [key, value] of Object.entries(
          val[0].camcordersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].camcordersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Camcorder_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Camcorder_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].camerasPerProject) != 0) {
        this.items.push('Media - Camera blocks per project');
        for (const [key, value] of Object.entries(val[0].camerasPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].camerasPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Camera_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Camera_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].imagepickersPerProject) != 0) {
        this.items.push('Media - ImagePicker blocks per project');
        for (const [key, value] of Object.entries(
          val[0].imagepickersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].imagepickersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.ImagePicker_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.ImagePicker_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].playersPerProject) != 0) {
        this.items.push('Media - Player blocks per project');
        for (const [key, value] of Object.entries(val[0].playersPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].playersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Player_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Player_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].soundsPerProject) != 0) {
        this.items.push('Media - Sound blocks per project');
        for (const [key, value] of Object.entries(val[0].soundsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].soundsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Sound_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Sound_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].soundrecordersPerProject) != 0) {
        this.items.push('Media - SoundRecorder blocks per project');
        for (const [key, value] of Object.entries(
          val[0].soundrecordersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].soundrecordersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.SoundRecorder_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.SoundRecorder_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].speechrecognizersPerProject) != 0) {
        this.items.push('Media - SpeechRecognizer blocks per project');
        for (const [key, value] of Object.entries(
          val[0].speechrecognizersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].speechrecognizersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.SpeechRecognizer_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.SpeechRecognizer_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].texttospeechsPerProject) != 0) {
        this.items.push('Media - TextToSpeech blocks per project');
        for (const [key, value] of Object.entries(
          val[0].texttospeechsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].texttospeechsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.TextToSpeech_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.TextToSpeech_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].videoplayersPerProject) != 0) {
        this.items.push('Media - VideoPlayer blocks per project');
        for (const [key, value] of Object.entries(
          val[0].videoplayersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].videoplayersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.VideoPlayer_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.VideoPlayer_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].yandextranslatorsPerProject) != 0) {
        this.items.push('Media - YandexTranslate blocks per project');
        for (const [key, value] of Object.entries(
          val[0].yandextranslatorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].yandextranslatorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.YandexTranslate_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.YandexTranslate_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].ballsPerProject) != 0) {
        this.items.push('Drawing and Animation - Ball blocks per project');
        for (const [key, value] of Object.entries(val[0].ballsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(val[0].ballsPerProject)) {
              const obj = {};
              obj.Project_name = key;
              obj.Ball_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Ball_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].canvasesPerProject) != 0) {
        this.items.push('Drawing and Animation - Canvas blocks per project');
        for (const [key, value] of Object.entries(val[0].canvasesPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].canvasesPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Canvas_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Canvas_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].imagespritesPerProject) != 0) {
        this.items.push(
          'Drawing and Animation - ImageSprite blocks per project'
        );
        for (const [key, value] of Object.entries(
          val[0].imagespritesPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].imagespritesPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.ImageSprite_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.ImageSprite_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].circlesPerProject) != 0) {
        this.items.push('Maps - Circle blocks per project');
        for (const [key, value] of Object.entries(val[0].circlesPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].circlesPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Circle_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Circle_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].featurecollectionsPerProject) != 0) {
        this.items.push('Maps - FeatureCollection blocks per project');
        for (const [key, value] of Object.entries(
          val[0].featurecollectionsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].featurecollectionsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.FeatureCollection_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.FeatureCollection_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].mapsPerProject) != 0) {
        this.items.push('Maps - Map blocks per project');
        for (const [key, value] of Object.entries(val[0].mapsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(val[0].mapsPerProject)) {
              const obj = {};
              obj.Project_name = key;
              obj.Map_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Map_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].markersPerProject) != 0) {
        this.items.push('Maps - Marker blocks per project');
        for (const [key, value] of Object.entries(val[0].markersPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].markersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Marker_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Marker_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].navigationsPerProject) != 0) {
        this.items.push('Maps - Navigation blocks per project');
        for (const [key, value] of Object.entries(
          val[0].navigationsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].navigationsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Navigation_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Navigation_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].polygonsPerProject) != 0) {
        this.items.push('Maps - Polygon blocks per project');
        for (const [key, value] of Object.entries(
          val[0].navigationsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].navigationsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Navigation_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Navigation_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].rectanglesPerProject) != 0) {
        this.items.push('Maps - Rectangle blocks per project');
        for (const [key, value] of Object.entries(
          val[0].rectanglesPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].rectanglesPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Rectangle_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Rectangle_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].accelerometerSensorsPerProject) != 0) {
        this.items.push('Sensors - AccelerometerSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].accelerometerSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].accelerometerSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.AccelerometerSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.AccelerometerSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].barcodeScannersPerProject) != 0) {
        this.items.push('Sensors - BarcodeScanner blocks per project');
        for (const [key, value] of Object.entries(
          val[0].barcodeScannersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].barcodeScannersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.BarcodeScanner_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.BarcodeScanner_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].barometersPerProject) != 0) {
        this.items.push('Sensors - Barometer blocks per project');
        for (const [key, value] of Object.entries(
          val[0].barometersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].barometersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Barometer_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Barometer_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].clocksPerProject) != 0) {
        this.items.push('Sensors - Clock blocks per project');
        for (const [key, value] of Object.entries(val[0].clocksPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].clocksPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Clock_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Clock_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].gyroscopeSensorsPerProject) != 0) {
        this.items.push('Sensors - GyroscopeSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].gyroscopeSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].gyroscopeSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.GyroscopeSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.GyroscopeSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].hygrometersPerProject) != 0) {
        this.items.push('Sensors - Hygrometer blocks per project');
        for (const [key, value] of Object.entries(
          val[0].hygrometersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].hygrometersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Hygrometer_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Hygrometer_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].lightSensorsPerProject) != 0) {
        this.items.push('Sensors - LightSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].lightSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].lightSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.LightSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.LightSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].locationSensorsPerProject) != 0) {
        this.items.push('Sensors - LocationSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].locationSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].locationSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.LocationSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.LocationSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].magneticFieldSensorsPerProject) != 0) {
        this.items.push('Sensors - MagneticFieldSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].magneticFieldSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].magneticFieldSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.MagneticFieldSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.MagneticFieldSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].nearFieldsPerProject) != 0) {
        this.items.push('Sensors - NearField blocks per project');
        for (const [key, value] of Object.entries(
          val[0].nearFieldsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].nearFieldsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.NearField_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.NearField_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].orientationSensorsPerProject) != 0) {
        this.items.push('Sensors - OrientationSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].orientationSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].orientationSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.OrientationSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.OrientationSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].pedometersPerProject) != 0) {
        this.items.push('Sensors - Pedometer blocks per project');
        for (const [key, value] of Object.entries(
          val[0].pedometersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].pedometersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Pedometer_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Pedometer_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].proximitySensorsPerProject) != 0) {
        this.items.push('Sensors - ProximitySensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].proximitySensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].proximitySensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.ProximitySensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.ProximitySensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].thermometersPerProject) != 0) {
        this.items.push('Sensors - Thermometer blocks per project');
        for (const [key, value] of Object.entries(
          val[0].thermometersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].thermometersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Thermometer_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Thermometer_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].contactPickersPerProject) != 0) {
        this.items.push('Social - ContactPicker blocks per project');
        for (const [key, value] of Object.entries(
          val[0].contactPickersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].contactPickersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.ContactPicker_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.ContactPicker_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].emailPickersPerProject) != 0) {
        this.items.push('Social - EmailPicker blocks per project');
        for (const [key, value] of Object.entries(
          val[0].emailPickersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].emailPickersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.EmailPicker_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.EmailPicker_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].phoneCallsPerProject) != 0) {
        this.items.push('Social - PhoneCall blocks per project');
        for (const [key, value] of Object.entries(
          val[0].phoneCallsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].phoneCallsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.PhoneCall_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.PhoneCall_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].phoneNumberPickersPerProject) != 0) {
        this.items.push('Social - PhoneNumberPicker blocks per project');
        for (const [key, value] of Object.entries(
          val[0].phoneNumberPickersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].phoneNumberPickersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.PhoneNumberPicker_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.PhoneNumberPicker_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].sharingsPerProject) != 0) {
        this.items.push('Social - Sharing blocks per project');
        for (const [key, value] of Object.entries(val[0].sharingsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].sharingsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Sharing_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Sharing_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].textingsPerProject) != 0) {
        this.items.push('Social - Texting blocks per project');
        for (const [key, value] of Object.entries(val[0].textingsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].textingsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Texting_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Texting_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].twittersPerProject) != 0) {
        this.items.push('Social - Twitter blocks per project');
        for (const [key, value] of Object.entries(val[0].twittersPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].twittersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Twitter_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Twitter_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].cloudDbsPerProject) != 0) {
        this.items.push('Storage - CloudDB blocks per project');
        for (const [key, value] of Object.entries(val[0].cloudDbsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].cloudDbsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.CloudDB_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.CloudDB_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].filesPerProject) != 0) {
        this.items.push('Storage - File blocks per project');
        for (const [key, value] of Object.entries(val[0].filesPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(val[0].filesPerProject)) {
              const obj = {};
              obj.Project_name = key;
              obj.Files_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Files_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].tinyDbsPerProject) != 0) {
        this.items.push('Storage - TinyDB blocks per project');
        for (const [key, value] of Object.entries(val[0].tinyDbsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].tinyDbsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.TinyDB_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.TinyDB_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].tinyWebDbsPerProject) != 0) {
        this.items.push('Storage - TinyWebDB blocks per project');
        for (const [key, value] of Object.entries(
          val[0].tinyWebDbsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].tinyWebDbsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.TinyWebDB_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.TinyWebDB_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].activityStartersPerProject) != 0) {
        this.items.push('Connectivity - ActivityStarter blocks per project');
        for (const [key, value] of Object.entries(
          val[0].activityStartersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].activityStartersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.ActivityStarter_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.ActivityStarter_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].bluetoothClientsPerProject) != 0) {
        this.items.push('Connectivity - BluetoothClient blocks per project');
        for (const [key, value] of Object.entries(
          val[0].bluetoothClientsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].bluetoothClientsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.BluetoothClient_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.BluetoothClient_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].bluetoothServersPerProject) != 0) {
        this.items.push('Connectivity - BluetoothServer blocks per project');
        for (const [key, value] of Object.entries(
          val[0].bluetoothServersPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].bluetoothServersPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.BluetoothServer_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.BluetoothServer_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].serialsPerProject) != 0) {
        this.items.push('Connectivity - Serial blocks per project');
        for (const [key, value] of Object.entries(val[0].serialsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].serialsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Serial_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Serial_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].websPerProject) != 0) {
        this.items.push('Connectivity - Web blocks per project');
        for (const [key, value] of Object.entries(val[0].websPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(val[0].websPerProject)) {
              const obj = {};
              obj.Project_name = key;
              obj.Web_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Web_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].nxtDrivesPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - NxtDrive blocks per project');
        for (const [key, value] of Object.entries(val[0].nxtDrivesPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].nxtDrivesPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.NxtDrive_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Web_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].nxtColorSensorsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - NxtColorSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].nxtColorSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].nxtColorSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.NxtColorSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.NxtColorSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].nxtLightSensorsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - NxtLightSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].nxtLightSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].nxtLightSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.NxtLightSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.NxtLightSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].nxtSoundSensorsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - NxtSoundSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].nxtSoundSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].nxtSoundSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.NxtSoundSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.NxtSoundSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].nxtTouchSensorsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - NxtTouchSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].nxtTouchSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].nxtTouchSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.NxtTouchSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.NxtTouchSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].nxtUltrasonicSensorsPerProject) != 0) {
        this.items.push(
          'LEGO MINDSTORMS - NxtUltrasonicSensor blocks per project'
        );
        for (const [key, value] of Object.entries(
          val[0].nxtUltrasonicSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].nxtUltrasonicSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.NxtUltrasonicSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.NxtUltrasonicSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].nxtDirectCommandsPerProject) != 0) {
        this.items.push(
          'LEGO MINDSTORMS - NxtDirectCommands blocks per project'
        );
        for (const [key, value] of Object.entries(
          val[0].nxtDirectCommandsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].nxtDirectCommandsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.NxtDirectCommands_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.NxtDirectCommands_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].ev3MotorsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - Ev3Motors blocks per project');
        for (const [key, value] of Object.entries(val[0].ev3MotorsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].ev3MotorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Ev3Motors_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Ev3Motors_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].ev3ColorSensorsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - Ev3ColorSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].ev3ColorSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].ev3ColorSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Ev3ColorSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Ev3ColorSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].ev3GyroSensorsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - Ev3GyroSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].ev3GyroSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].ev3GyroSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Ev3GyroSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Ev3GyroSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].ev3TouchSensorsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - Ev3TouchSensor blocks per project');
        for (const [key, value] of Object.entries(
          val[0].ev3TouchSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].ev3TouchSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Ev3TouchSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Ev3TouchSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].ev3UltrasonicSensorsPerProject) != 0) {
        this.items.push(
          'LEGO MINDSTORMS - Ev3UltrasonicSensor blocks per project'
        );
        for (const [key, value] of Object.entries(
          val[0].ev3UltrasonicSensorsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].ev3UltrasonicSensorsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Ev3UltrasonicSensor_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Ev3UltrasonicSensor_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].ev3SoundsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - Ev3Sound blocks per project');
        for (const [key, value] of Object.entries(val[0].ev3SoundsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].ev3SoundsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Ev3Sound_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Ev3Sound_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].ev3UIsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - Ev3UI blocks per project');
        for (const [key, value] of Object.entries(val[0].ev3UIsPerProject)) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].ev3UIsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Ev3UI_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Ev3UI_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].ev3CommandsPerProject) != 0) {
        this.items.push('LEGO MINDSTORMS - Ev3Commands blocks per project');
        for (const [key, value] of Object.entries(
          val[0].ev3CommandsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].ev3CommandsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.Ev3Commands_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.Ev3Commands_blocks = value;
          }
        }
      }
      if (this.sumValues(val[0].firebaseDbsPerProject) != 0) {
        this.items.push('Experimental - FirebaseDB blocks per project');
        for (const [key, value] of Object.entries(
          val[0].firebaseDbsPerProject
        )) {
          result = this.exportProjectComparison.find(
            (x) => x.Project_name === key
          );
          if (result == null) {
            for (const [key, value] of Object.entries(
              val[0].firebaseDbsPerProject
            )) {
              const obj = {};
              obj.Project_name = key;
              obj.FirebaseDB_blocks = value;
              this.exportProjectComparison.push(obj);
            }
          } else {
            result.FirebaseDB_blocks = value;
          }
        }
      }
      this.compareBy = this.items[0];
    },
    resetData() {
      // resetneme všetky dáta
      this.basicStats = null;
      this.chartDataBuiltInBlocks.labels = [];
      this.chartDataBuiltInBlocks.data = [];
      this.chartDataComponentBlocks.labels = [];
      this.chartDataComponentBlocks.data = [];
      this.chartDataComponentBlocksCategories.labels = [];
      this.chartDataComponentBlocksCategories.data = [];
      this.chartDataUIComponentBlocks.labels = [];
      this.chartDataUIComponentBlocks.data = [];
      this.chartDataDrawAndAnimComponentBlocks.labels = [];
      this.chartDataDrawAndAnimComponentBlocks.data = [];
      this.chartDataStorageAndExpComponentBlocks.labels = [];
      this.chartDataStorageAndExpComponentBlocks.data = [];
      this.chartDataControlBlocksTypes.data = [];
      this.chartDataControlBlocksTypes.labels = [];
      this.chartDataProcedureBlocksTypes.data = [];
      this.chartDataProcedureBlocksTypes.labels = [];
      this.chartDataBlocksPerProject.labels = [];
      this.chartDataBlocksPerProject.data = [];
      this.chartDataComponentsPerProject.labels = [];
      this.chartDataComponentsPerProject.data = [];
      this.chartDataScreensPerProject.labels = [];
      this.chartDataScreensPerProject.data = [];
      this.chartCompareBy.labels = [];
      this.chartCompareBy.data = [];
      this.exportProjectComparison = [];
      this.exportOverallStats = [];
      this.items = [];
    },
    downloadOverallStats() {
      const data = this.exportOverallStats;
      const fileName = 'ai_overall_statistics';
      const exportType = exportFromJSON.types.csv;
      const withBOM = true;
      exportFromJSON({ data, fileName, exportType, withBOM });
    },
    downloadProjectComparison() {
      const data = this.exportProjectComparison;
      const fileName = 'ai_project_comparison';
      const exportType = exportFromJSON.types.csv;
      const withBOM = true;
      exportFromJSON({ data, fileName, exportType, withBOM });
    },
    sumOfArray(data) {
      // vráti súčet prvkov pola
      return (
        data.reduce(function (a, b) {
          return a + b;
        }, 0) != 0
      );
    },
    openSettings() {
      // orvorí kartu s nastaveniami
      this.settingsDialog = true;
      this.changeAnalysed(false);
    },
    startProcess() {
      //resetne a nastaví nové dáta
      this.resetData();
      if (this.getAnalysedData.length != 0) {
        this.setData(this.getAnalysedData);
        this.setProjectComparisonExport(this.getAnalysedData);
        this.renderProjectComparison(this.getAnalysedData);
      }
    },
  },
  watch: {
    // ak sa zmenia analyzované dáta obnoví sa celý proces vykreslenia grafov
    getAnalysedData: function () {
      this.startProcess();
    },
    // ak začne proces analýzy, zavrieme kartu
    getAnalysed: function (val) {
      if (val) {
        if (val == true) {
          this.settingsDialog = false;
        }
      }
    },
    // ak sa zmeni hodnota v selecte zmeníme hodnoty grafu
    compareBy: function (val) {
      if (val) {
        this.renderProjectComparison(this.getAnalysedData);
      }
    },
  },
  mounted() {
    //pri montovaní komponentu spustí celý proces
    this.startProcess();
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
#card {
  padding: 30px;
  margin-bottom: 50px;
}
#heading {
  margin-bottom: 50px;
  margin-left: 10px;
  margin-right: 10px;
  font-size: 26px;
}
.row {
  margin-bottom: 50px;
}
#noData {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 80%;
  flex-direction: column;
}
#icon:hover {
  color: #26a69a;
}
.card_title {
  font-weight: 700;
  font-size: 20px;
}
.selectFiles {
  margin-left: 50px;
  margin-right: 50px;
  padding-bottom: 30px;
}
#divider {
  margin-top: 10px;
  margin-bottom: 20px;
}
.logo {
  display: none;
}
.logo2 {
  display: block;
  cursor: pointer;
}
.v-sheet.v-list:not(.v-sheet--outlined) {
  text-align: left !important;
}
@media only screen and (max-width: 450px) {
  #heading {
    font-size: 20px;
  }
  .card_title {
    font-weight: 700;
    font-size: 14px;
  }
  .logo {
    display: block;
    cursor: pointer;
  }
  .logo2 {
    display: none;
  }
}
</style>
