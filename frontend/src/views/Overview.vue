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
                    <h1 id="heading">
                      <v-icon large color="#26a69a"> mdi-compare </v-icon>
                      Project comparison
                    </h1>

                    <!--<v-row>
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
                    </v-row>-->
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
                            v-model="criterion"
                          ></v-select>
                          <p class="card_title">{{ criterion }}</p>
                          <div
                            v-if="
                              this.sumOfArray(this.chartDataCriteria.data) != 0
                            "
                          >
                            <BarChart
                              :chartData="this.chartDataCriteria.data"
                              :chartLabels="this.chartDataCriteria.labels"
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
import ExcelExport from 'export-xlsx';
import SelectFiles from '../components/SelectFiles.vue';
import BasicStats from '../components/BasicStats.vue';
import PieChart from '../components/PieChart.vue';
import LineChart from '../components/LineChart.vue';
import Footer from '../components/Footer.vue';

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
      items: [
        'Blocks per project',
        'Components per project',
        'Screens per project',
        'User Interface - Button blocks per project',
        'User Interface - Checkbox blocks per project',
        'User Interface - DatePicker blocks per project',
        'User Interface - Image blocks per project',
        'User Interface - Label blocks per project',
        'User Interface - ListPicker blocks per project',
        'User Interface - ListView blocks per project',
        'User Interface - Notifier blocks per project',
        'User Interface - PasswordTextBox blocks per project',
        'User Interface - Slider blocks per project',
        'User Interface - Spinner blocks per project',
        'User Interface - Switch blocks per project',
        'User Interface - TextBox blocks per project',
        'User Interface - TimePicker blocks per project',
        'User Interface - WebViewer blocks per project',
        'Layout - HorizontalArrangment blocks per project',
        'Layout - HorizontalScrollArrangment blocks per project',
        'Layout - TableArrangment blocks per project',
        'Layout - VerticalArrangment blocks per project',
        'Layout - VerticalScrollArrangment blocks per project',
        'Media - Camcorder blocks per project',
        'Media - Camera blocks per project',
        'Media - ImagePicker blocks per project',
        'Media - Player blocks per project',
        'Media - Sound blocks per project',
        'Media - SoundRecorder blocks per project',
        'Media - SpeechRecognizer blocks per project',
        'Media - TextToSpeech blocks per project',
        'Media - VideoPlayer blocks per project',
        'Media - YandexTranslate blocks per project',
        'Drawing and Animation - Ball blocks per project',
        'Drawing and Animation - Canvas blocks per project',
        'Drawing and Animation - ImageSprite blocks per project',
        'Maps - Circle blocks per project',
        'Maps - FeatureCollection blocks per project',
        'Maps - Map blocks per project',
        'Maps - Marker blocks per project',
        'Maps - Navigation blocks per project',
        'Maps - Polygon blocks per project',
        'Maps - Rectangle blocks per project',
        'Sensors - AccelerometerSensor blocks per project',
        'Sensors - BarcodeScanner blocks per project',
        'Sensors - Barometer blocks per project',
        'Sensors - Clock blocks per project',
        'Sensors - GyroscopeSensor blocks per project',
        'Sensors - Hygrometer blocks per project',
        'Sensors - LightSensor blocks per project',
        'Sensors - LocationSensor blocks per project',
        'Sensors - MagneticFieldSensor blocks per project',
        'Sensors - NearField blocks per project',
        'Sensors - OrientationSensor blocks per project',
        'Sensors - Pedometer blocks per project',
        'Sensors - ProximitySensor blocks per project',
        'Sensors - Thermometer blocks per project',
      ],
      criterion: 'Blocks per project',
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
      chartDataCriteria: {
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
        this.basicStatsExportData.labels.push(key);
        this.basicStatsExportData.data.push(value);
        if (key == 'Number of projects') {
          this.numberOfProjects = value;
        }
      }

      for (const [key, value] of Object.entries(val[0].builtInBlocks)) {
        this.chartDataBuiltInBlocks.labels.push(key);
        this.chartDataBuiltInBlocks.data.push(value);
      }

      for (const [key, value] of Object.entries(val[0].componentBlocks)) {
        this.chartDataComponentBlocks.labels.push(key);
        this.chartDataComponentBlocks.data.push(value);
      }

      for (const [key, value] of Object.entries(
        val[0].componentBlocksCategories
      )) {
        this.chartDataComponentBlocksCategories.labels.push(key);
        this.chartDataComponentBlocksCategories.data.push(value);
      }

      for (const [key, value] of Object.entries(
        val[0].userInterfaceComponentBlocks
      )) {
        this.chartDataUIComponentBlocks.labels.push(key);
        this.chartDataUIComponentBlocks.data.push(value);
      }

      for (const [key, value] of Object.entries(
        val[0].drawingAndAnimationComponentBlocks
      )) {
        this.chartDataDrawAndAnimComponentBlocks.labels.push(key);
        this.chartDataDrawAndAnimComponentBlocks.data.push(value);
      }

      for (const [key, value] of Object.entries(
        val[0].storageAndExperimentalComponentBlocks
      )) {
        this.chartDataStorageAndExpComponentBlocks.labels.push(key);
        this.chartDataStorageAndExpComponentBlocks.data.push(value);
      }

      for (const [key, value] of Object.entries(val[0].controlBlocksTypes)) {
        this.chartDataControlBlocksTypes.labels.push(key);
        this.chartDataControlBlocksTypes.data.push(value);
      }

      for (const [key, value] of Object.entries(val[0].procedureBlocksTypes)) {
        this.chartDataProcedureBlocksTypes.labels.push(key);
        this.chartDataProcedureBlocksTypes.data.push(value);
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

      switch (this.criterion) {
        case 'Blocks per project':
          for (const [key, value] of Object.entries(val[0].blocksPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Components per project':
          for (const [key, value] of Object.entries(
            val[0].componentsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Screens per project':
          for (const [key, value] of Object.entries(val[0].screensPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - Button blocks per project':
          for (const [key, value] of Object.entries(val[0].buttonsPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - Checkbox blocks per project':
          for (const [key, value] of Object.entries(
            val[0].checkboxesPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - DatePicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].datepickersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - Image blocks per project':
          for (const [key, value] of Object.entries(val[0].imagesPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - Label blocks per project':
          for (const [key, value] of Object.entries(val[0].labelsPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - ListPicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].listpickersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - ListView blocks per project':
          for (const [key, value] of Object.entries(
            val[0].listviewsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - Notifier blocks per project':
          for (const [key, value] of Object.entries(
            val[0].notifiersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - PasswordTextBox blocks per project':
          for (const [key, value] of Object.entries(
            val[0].passwordtextboxesPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - Slider blocks per project':
          for (const [key, value] of Object.entries(val[0].slidersPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - Spinner blocks per project':
          for (const [key, value] of Object.entries(
            val[0].spinnersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - Switch blocks per project':
          for (const [key, value] of Object.entries(
            val[0].switchesPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - TextBox blocks per project':
          for (const [key, value] of Object.entries(
            val[0].textboxesPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - TimePicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].timepickersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'User Interface - WebViewer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].webviewersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Layout - HorizontalArrangment blocks per project':
          for (const [key, value] of Object.entries(
            val[0].horizontalArrangmentPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Layout - HorizontalScrollArrangment blocks per project':
          for (const [key, value] of Object.entries(
            val[0].horizontalScrollArrangmentPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Layout - TableArrangment blocks per project':
          for (const [key, value] of Object.entries(
            val[0].tableArrangmentPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Layout - VerticalArrangment blocks per project':
          for (const [key, value] of Object.entries(
            val[0].verticalArrangmentPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Layout - VerticalScrollArrangment blocks per project':
          for (const [key, value] of Object.entries(
            val[0].verticalScrollArrangmentPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Media - Camcorder blocks per project':
          for (const [key, value] of Object.entries(
            val[0].camcordersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Media - Camera blocks per project':
          for (const [key, value] of Object.entries(val[0].camerasPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Media - ImagePicker blocks per project':
          for (const [key, value] of Object.entries(
            val[0].imagepickersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Media - Player blocks per project':
          for (const [key, value] of Object.entries(val[0].playersPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Media - Sound blocks per project':
          for (const [key, value] of Object.entries(val[0].soundsPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Media - SoundRecorder blocks per project':
          for (const [key, value] of Object.entries(
            val[0].soundrecordersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Media - SpeechRecognizer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].speechrecognizersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Media - TextToSpeech blocks per project':
          for (const [key, value] of Object.entries(
            val[0].texttospeechsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Media - VideoPlayer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].videoplayersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Media - YandexTranslate blocks per project':
          for (const [key, value] of Object.entries(
            val[0].yandextranslatorsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Drawing and Animation - Ball blocks per project':
          for (const [key, value] of Object.entries(val[0].ballsPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Drawing and Animation - Canvas blocks per project':
          for (const [key, value] of Object.entries(
            val[0].canvasesPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Drawing and Animation - ImageSprite blocks per project':
          for (const [key, value] of Object.entries(
            val[0].imagespritesPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Maps - Circle blocks per project':
          for (const [key, value] of Object.entries(val[0].circlesPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Maps - FeatureCollection blocks per project':
          for (const [key, value] of Object.entries(
            val[0].featurecollectionsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Maps - Map blocks per project':
          for (const [key, value] of Object.entries(val[0].mapsPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Maps - Marker blocks per project':
          for (const [key, value] of Object.entries(val[0].markersPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Maps - Navigation blocks per project':
          for (const [key, value] of Object.entries(
            val[0].navigationsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Maps - Polygon blocks per project':
          for (const [key, value] of Object.entries(
            val[0].polygonsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Maps - Rectangle blocks per project':
          for (const [key, value] of Object.entries(
            val[0].rectanglesPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - AccelerometerSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].accelerometerSensorsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - BarcodeScanner blocks per project':
          for (const [key, value] of Object.entries(
            val[0].barcodeScannersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - Barometer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].barometersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - Clock blocks per project':
          for (const [key, value] of Object.entries(val[0].clocksPerProject)) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - GyroscopeSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].gyroscopeSensorsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - Hygrometer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].hygrometersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - LightSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].lightSensorsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - LocationSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].locationSensorsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - MagneticFieldSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].magneticFieldSensorsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - NearField blocks per project':
          for (const [key, value] of Object.entries(
            val[0].nearFieldsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - OrientationSensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].orientationSensorsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - Pedometer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].pedometersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - ProximitySensor blocks per project':
          for (const [key, value] of Object.entries(
            val[0].proximitySensorsPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
        case 'Sensors - Thermometer blocks per project':
          for (const [key, value] of Object.entries(
            val[0].thermometersPerProject
          )) {
            this.chartDataCriteria.labels.push(key);
            this.chartDataCriteria.data.push(value);
          }
          break;
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
        case 'criteria':
          this.chartDataCriteria.labels = sortedLabels;
          this.chartDataCriteria.data = sortedData;
          break;
      }
    },
    setExportData(type, labels, data) {
      // vytvoríme štýlovací objekt pre hlavičku
      const style = {
        alignment: { horizontal: 'center', vertical: 'middle' },
      };

      // vytvoríme objekt pre hlavičku
      var tableHeaders = labels.map(function (d) {
        return {
          name: d,
          key: d,
          style: style,
          width: 25,
        };
      });

      //  vytvoríme objekt pre dáta
      var tableData = data.map(function (d, i) {
        return {
          [labels[i]]: d,
        };
      });

      // spojíme všetky dátové objekty do jedného
      const tableDataMerged = Object.assign({}, ...tableData);

      // pre každý typ nastavíme dáta pre tabuľku
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
      // stiahneme Excel súbor s analyzovaními dátami
      const excelExport = new ExcelExport();
      excelExport.downloadExcel(this.SETTINGS_FOR_EXPORT, this.dataToExport);
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

      this.sortData(
        'criteria',
        this.chartDataCriteria.labels,
        this.chartDataCriteria.data
      );

      // nastavíme dáta na export do Excelu
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
      // vykreslíme grafy
      this.renderChart = true;
    },
    resetData() {
      // resetneme všetky dáta
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
      this.chartDataCriteria.labels = [];
      this.chartDataCriteria.data = [];
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
      }
    },
  },
  watch: {
    // ak sa zmenia analyzované dáta obnoví sa celý proces vykreslenia grafov
    getAnalysedData: function (val) {
      if (val) {
        this.resetData();
        this.setData(val);
      }
    },
    // ak začne proces analýzy, zavrieme kartu
    getAnalysed: function (val) {
      if (val) {
        if (val == true) {
          this.settingsDialog = false;
        }
      }
    },
    criterion: function (val) {
      if (val) {
        this.startProcess();
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
