<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat height="80px">
      <v-container class="py-0 fill-height">
        <router-link v-bind:to="'/'">
          <img class="logo" src="../assets/images/logo.png" height="70px" />
        </router-link>
        <router-link v-bind:to="'/'">
          <img class="logo2" src="../assets/images/logo2.png" height="70px" />
        </router-link>
        <v-spacer></v-spacer>
        <v-btn v-for="link in links" :key="link" text>
          {{ link }}
        </v-btn>
      </v-container>
    </v-app-bar>

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
                        @click="exportToExcel"
                        v-bind="attrs"
                        v-on="on"
                      >
                        mdi-file-export
                      </v-icon>
                    </template>
                    <span>Export to Excel</span>
                  </v-tooltip>
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
                    <span>Settings</span>
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
                    <h1 id="heading">
                      <v-icon large color="#26a69a">
                        mdi-chart-timeline-variant
                      </v-icon>
                      Overall analysis
                    </h1>

                    <v-row v-if="basicStats != null">
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
                  <v-card id="card">
                    <h1 id="heading">
                      <v-icon large color="#26a69a">
                        mdi-chart-timeline-variant
                      </v-icon>
                      Per project analysis
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
                          <p class="card_title">Blocks per project</p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataBlocksPerProject.data
                              ) != 0
                            "
                          >
                            <BarChart
                              :chartData="this.chartDataBlocksPerProject.data"
                              :chartLabels="
                                this.chartDataBlocksPerProject.labels
                              "
                              class="bar-chart"
                            ></BarChart>
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
                          <p class="card_title">Components per project</p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataComponentsPerProject.data
                              ) != 0
                            "
                          >
                            <BarChart
                              :chartData="
                                this.chartDataComponentsPerProject.data
                              "
                              :chartLabels="
                                this.chartDataComponentsPerProject.labels
                              "
                              class="bar-chart"
                            ></BarChart>
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
                          <p class="card_title">Screens per project</p>
                          <div
                            v-if="
                              this.sumOfArray(
                                this.chartDataScreensPerProject.data
                              ) != 0
                            "
                          >
                            <BarChart
                              :chartData="this.chartDataScreensPerProject.data"
                              :chartLabels="
                                this.chartDataScreensPerProject.labels
                              "
                              class="bar-chart"
                            ></BarChart>
                          </div>
                          <div id="noData" v-else>
                            <v-icon x-large> mdi-eye-off </v-icon>
                            <p>No data to analyse</p>
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
      <v-footer dark padless>
        <v-card flat tile class="teal lighten-1 white--text text-center">
          <v-card-text>
            <v-btn
              v-for="icon in icons"
              :key="icon"
              class="mx-4 white--text"
              icon
            >
              <v-icon size="24px">
                {{ icon }}
              </v-icon>
            </v-btn>
          </v-card-text>

          <v-card-text class="white--text pt-0">
            Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet.
            Mauris cursus commodo interdum. Praesent ut risus eget metus luctus
            accumsan id ultrices nunc. Sed at orci sed massa consectetur
            dignissim a sit amet dui. Duis commodo vitae velit et faucibus.
            Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum
            ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel
            diam elementum tempor vel ut orci. Orci varius natoque penatibus et
            magnis dis parturient montes, nascetur ridiculus mus.
          </v-card-text>

          <v-divider></v-divider>

          <v-card-text class="white--text">
            {{ new Date().getFullYear() }} — <strong>App Inspector</strong>
          </v-card-text>
        </v-card>
      </v-footer>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import DoughnutChart from '../components/DoughnutChart.vue';
import BarChart from '../components/BarChart.vue';
import ExcelExport from 'export-xlsx';
import SelectFiles from '../components/SelectFiles.vue';
import BasicStats from '../components/BasicStats.vue';
import PieChart from '../components/PieChart.vue';
import LineChart from '../components/LineChart.vue';

export default {
  name: 'Overview',
  components: {
    DoughnutChart,
    BarChart,
    PieChart,
    LineChart,
    SelectFiles,
    BasicStats,
  },
  data() {
    return {
      //analyzedData: Object,
      renderChart: false,
      settingsDialog: false,
      links: ['Sign in'],
      icons: ['mdi-facebook', 'mdi-twitter', 'mdi-linkedin', 'mdi-instagram'],
      basicStats: Object,
      basicStatsExportData: {
        labels: [],
        data: [],
      },
      panel: [0, 1],
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
      SETTINGS_FOR_EXPORT: {
        fileName: 'ai_overview',
        workSheets: [
          {
            sheetName: 'Basic statistics',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Basic statistics',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'Built-in blocks',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Built-in blocks',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'Component blocks',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Component blocks',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'Component blocks types',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Component blocks types',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'User Interface component blocks',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'User Interface component blocks',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'Drawing & Ani. component blocks',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Drawing and Animation component blocks',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'Storage & Exp. component blocks',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Storage and Experimental component blocks',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'Control blocks types',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Control blocks types',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'Procedure blocks types',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Procedure blocks types',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'Blocks per project',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Blocks per project',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'Components per project',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Components per project',
                headerDefinition: [],
              },
            },
          },
          {
            sheetName: 'Screens per project',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Screens per project',
                headerDefinition: [],
              },
            },
          },
        ],
      },
      dataToExport: [
        {
          data: [],
        },
        {
          data: [],
        },
        {
          data: [],
        },
        {
          data: [],
        },
        {
          data: [],
        },
        {
          data: [],
        },
        {
          data: [],
        },
        {
          data: [],
        },
        {
          data: [],
        },
        {
          data: [],
        },
        {
          data: [],
        },
        {
          data: [],
        },
      ],
    };
  },
  computed: {
    ...mapGetters({
      getAnalyzedData: 'files/getAnalyzedData',
      getAnalysed: 'files/getAnalysed',
    }),
  },
  methods: {
    ...mapActions({
      changeAnalysed: 'files/changeAnalysed',
    }),
    setChartData(val) {
      //populate labels and data from server response data
      /*for (const [key, value] of Object.entries(val[0].basicStats)) {
        console.log(key, value);
        this.basicStatsLabels.push(key);
        this.basicStatsData.push(value);
      }*/
      this.basicStats = val[0].basicStats;

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].basicStats)) {
        this.basicStatsExportData.labels.push(key);
        this.basicStatsExportData.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].builtInBlocks)) {
        this.chartDataBuiltInBlocks.labels.push(key);
        this.chartDataBuiltInBlocks.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].componentBlocks)) {
        this.chartDataComponentBlocks.labels.push(key);
        this.chartDataComponentBlocks.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(
        val[0].componentBlocksCategories
      )) {
        this.chartDataComponentBlocksCategories.labels.push(key);
        this.chartDataComponentBlocksCategories.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(
        val[0].userInterfaceComponentBlocks
      )) {
        this.chartDataUIComponentBlocks.labels.push(key);
        this.chartDataUIComponentBlocks.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(
        val[0].drawingAndAnimationComponentBlocks
      )) {
        this.chartDataDrawAndAnimComponentBlocks.labels.push(key);
        this.chartDataDrawAndAnimComponentBlocks.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(
        val[0].storageAndExperimentalComponentBlocks
      )) {
        this.chartDataStorageAndExpComponentBlocks.labels.push(key);
        this.chartDataStorageAndExpComponentBlocks.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].controlBlocksTypes)) {
        this.chartDataControlBlocksTypes.labels.push(key);
        this.chartDataControlBlocksTypes.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].procedureBlocksTypes)) {
        this.chartDataProcedureBlocksTypes.labels.push(key);
        this.chartDataProcedureBlocksTypes.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].blocksPerProject)) {
        this.chartDataBlocksPerProject.labels.push(key);
        this.chartDataBlocksPerProject.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].componentsPerProject)) {
        this.chartDataComponentsPerProject.labels.push(key);
        this.chartDataComponentsPerProject.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].screensPerProject)) {
        this.chartDataScreensPerProject.labels.push(key);
        this.chartDataScreensPerProject.data.push(value);
      }
    },
    sortData(type, labels, data) {
      //create object
      var chartObj = labels.map(function (d, i) {
        return {
          label: d,
          data: data[i] || 0,
        };
      });

      //sort data
      var sortedChartObj = chartObj.sort(function (a, b) {
        return b.data - a.data;
      });

      //populate sorted labels and data arrays
      var sortedLabels = [];
      var sortedData = [];
      sortedChartObj.forEach(function (d) {
        sortedLabels.push(d.label);
        sortedData.push(d.data);
      });

      //set data for each type
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
      }
    },
    setExportData(type, labels, data) {
      //create style object for header cell
      const style = {
        alignment: { horizontal: 'center', vertical: 'middle' },
      };

      //create header object array
      var tableHeaders = labels.map(function (d) {
        return {
          name: d,
          key: d,
          style: style,
          width: 25,
        };
      });

      //create data object array
      var tableData = data.map(function (d, i) {
        return {
          [labels[i]]: d,
        };
      });

      //merge all data objects to single object
      const tableDataMerged = Object.assign({}, ...tableData);

      //set table data for each type
      switch (type) {
        case 'basicStats':
          this.SETTINGS_FOR_EXPORT.workSheets[0].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[0].data = [tableDataMerged];
          break;
        case 'builtInBlocks':
          this.SETTINGS_FOR_EXPORT.workSheets[1].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[1].data = [tableDataMerged];
          break;
        case 'componentBlocks':
          this.SETTINGS_FOR_EXPORT.workSheets[2].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[2].data = [tableDataMerged];
          break;
        case 'componentBlocksCategories':
          this.SETTINGS_FOR_EXPORT.workSheets[3].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[3].data = [tableDataMerged];
          break;
        case 'userInterfaceComponentBlocks':
          this.SETTINGS_FOR_EXPORT.workSheets[4].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[4].data = [tableDataMerged];
          break;
        case 'drawingAndAnimationComponentBlocks':
          this.SETTINGS_FOR_EXPORT.workSheets[5].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[5].data = [tableDataMerged];
          break;
        case 'storageAndExperimentalComponentBlocks':
          this.SETTINGS_FOR_EXPORT.workSheets[6].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[6].data = [tableDataMerged];
          break;
        case 'controlBlocksTypes':
          this.SETTINGS_FOR_EXPORT.workSheets[7].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[7].data = [tableDataMerged];
          break;
        case 'procedureBlocksType':
          this.SETTINGS_FOR_EXPORT.workSheets[8].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[8].data = [tableDataMerged];
          break;
        case 'blocksPerProject':
          this.SETTINGS_FOR_EXPORT.workSheets[9].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[9].data = [tableDataMerged];
          break;
        case 'componentsPerProject':
          this.SETTINGS_FOR_EXPORT.workSheets[10].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[10].data = [tableDataMerged];
          break;
        case 'screensPerProject':
          this.SETTINGS_FOR_EXPORT.workSheets[11].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[11].data = [tableDataMerged];
          break;
      }
    },
    exportToExcel() {
      const excelExport = new ExcelExport();
      excelExport.downloadExcel(this.SETTINGS_FOR_EXPORT, this.dataToExport);
    },
    setData(val) {
      //set chart data and labels
      this.setChartData(val);

      //sort all data and labels
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

      //set all data to excel export
      this.setExportData(
        'basicStats',
        this.basicStatsExportData.labels,
        this.basicStatsExportData.data
      );

      this.setExportData(
        'builtInBlocks',
        this.chartDataBuiltInBlocks.labels,
        this.chartDataBuiltInBlocks.data
      );
      this.setExportData(
        'componentBlocks',
        this.chartDataComponentBlocks.labels,
        this.chartDataComponentBlocks.data
      );
      this.setExportData(
        'componentBlocksCategories',
        this.chartDataComponentBlocksCategories.labels,
        this.chartDataComponentBlocksCategories.data
      );
      this.setExportData(
        'userInterfaceComponentBlocks',
        this.chartDataUIComponentBlocks.labels,
        this.chartDataUIComponentBlocks.data
      );
      this.setExportData(
        'drawingAndAnimationComponentBlocks',
        this.chartDataDrawAndAnimComponentBlocks.labels,
        this.chartDataDrawAndAnimComponentBlocks.data
      );
      this.setExportData(
        'storageAndExperimentalComponentBlocks',
        this.chartDataStorageAndExpComponentBlocks.labels,
        this.chartDataStorageAndExpComponentBlocks.data
      );
      this.setExportData(
        'controlBlocksTypes',
        this.chartDataControlBlocksTypes.labels,
        this.chartDataControlBlocksTypes.data
      );
      this.setExportData(
        'procedureBlocksType',
        this.chartDataProcedureBlocksTypes.labels,
        this.chartDataProcedureBlocksTypes.data
      );
      this.setExportData(
        'blocksPerProject',
        this.chartDataBlocksPerProject.labels,
        this.chartDataBlocksPerProject.data
      );
      this.setExportData(
        'componentsPerProject',
        this.chartDataComponentsPerProject.labels,
        this.chartDataComponentsPerProject.data
      );
      this.setExportData(
        'screensPerProject',
        this.chartDataScreensPerProject.labels,
        this.chartDataScreensPerProject.data
      );
      //render charts
      this.renderChart = true;
    },
    resetData() {
      this.basicStats = null;
      this.basicStatsExportData.labels = [];
      this.basicStatsExportData.data = [];
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

      this.SETTINGS_FOR_EXPORT.workSheets[0].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[1].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[2].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[3].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[4].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[5].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[6].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[7].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[8].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[9].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[10].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[11].tableSettings.data.headerDefinition = [];
      this.dataToExport[0].data = [];
      this.dataToExport[1].data = [];
      this.dataToExport[2].data = [];
      this.dataToExport[3].data = [];
      this.dataToExport[4].data = [];
      this.dataToExport[5].data = [];
      this.dataToExport[6].data = [];
      this.dataToExport[7].data = [];
      this.dataToExport[8].data = [];
      this.dataToExport[9].data = [];
      this.dataToExport[10].data = [];
      this.dataToExport[11].data = [];
    },
    sumOfArray(data) {
      return (
        data.reduce(function (a, b) {
          return a + b;
        }, 0) != 0
      );
    },
    openSettings() {
      this.settingsDialog = true;
      this.changeAnalysed(false);
    },
  },
  watch: {
    getAnalyzedData: function (val) {
      if (val) {
        this.resetData();
        this.setData(val);
      }
    },
    getAnalysed: function (val) {
      if (val) {
        if (val == true) {
          this.settingsDialog = false;
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
#card {
  padding: 30px;
  margin-bottom: 50px;
}
#heading {
  margin-top: 50px;
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
  margin-top: 20px;
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
