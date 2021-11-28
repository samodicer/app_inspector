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
                    <p class="card_title">Built-in blocks</p>
                    <DoughnutChart
                      :chartData="this.chartDataBuiltInBlocks"
                      :chartOptions="this.chartOptionsBuiltInBlocks"
                      class="doughnut-chart"
                    ></DoughnutChart>
                  </v-sheet>
                </v-col>
                <v-col>
                  <v-sheet id="sheet" rounded="lg" color="#F7F7F7">
                    <p class="card_title">Component blocks</p>
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
                    <p class="card_title">Categories of component blocks</p>
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
                    <p class="card_title">User Interface component blocks</p>
                    <BarChart
                      :chartData="this.chartDataUIComponentBlocks"
                      :chartOptions="this.chartOptionsUIComponentBlocks"
                      class="doughnut-chart"
                    ></BarChart>
                  </v-sheet>
                </v-col>
              </v-row>
              <v-row>
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
                        @click="settingsDialog = true"
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
                          <v-btn icon dark @click="settingsDialog = false">
                            <v-icon>mdi-close</v-icon>
                          </v-btn>
                          <v-toolbar-title>Settings</v-toolbar-title>
                          <v-spacer></v-spacer>
                          <v-toolbar-items>
                            <v-btn dark text @click="settingsDialog = false">
                              Save
                            </v-btn>
                          </v-toolbar-items>
                        </v-toolbar>
                        <v-list three-line subheader>
                          <v-subheader>User Controls</v-subheader>
                          <v-list-item>
                            <v-list-item-content>
                              <v-list-item-title
                                >Content filtering</v-list-item-title
                              >
                              <v-list-item-subtitle
                                >Set the content filtering level to restrict
                                apps that can be
                                downloaded</v-list-item-subtitle
                              >
                            </v-list-item-content>
                          </v-list-item>
                          <v-list-item>
                            <v-list-item-content>
                              <v-list-item-title>Password</v-list-item-title>
                              <v-list-item-subtitle
                                >Require password for purchase or use password
                                to restrict purchase</v-list-item-subtitle
                              >
                            </v-list-item-content>
                          </v-list-item>
                        </v-list>
                        <v-divider></v-divider>
                        <v-list three-line subheader>
                          <v-subheader>General</v-subheader>
                          <v-list-item>
                            <v-list-item-action>
                              <v-checkbox v-model="notifications"></v-checkbox>
                            </v-list-item-action>
                            <v-list-item-content>
                              <v-list-item-title
                                >Notifications</v-list-item-title
                              >
                              <v-list-item-subtitle
                                >Notify me about updates to apps or games that I
                                downloaded</v-list-item-subtitle
                              >
                            </v-list-item-content>
                          </v-list-item>
                          <v-list-item>
                            <v-list-item-action>
                              <v-checkbox v-model="sound"></v-checkbox>
                            </v-list-item-action>
                            <v-list-item-content>
                              <v-list-item-title>Sound</v-list-item-title>
                              <v-list-item-subtitle
                                >Auto-update apps at any time. Data charges may
                                apply</v-list-item-subtitle
                              >
                            </v-list-item-content>
                          </v-list-item>
                          <v-list-item>
                            <v-list-item-action>
                              <v-checkbox v-model="widgets"></v-checkbox>
                            </v-list-item-action>
                            <v-list-item-content>
                              <v-list-item-title
                                >Auto-add widgets</v-list-item-title
                              >
                              <v-list-item-subtitle
                                >Automatically add home screen
                                widgets</v-list-item-subtitle
                              >
                            </v-list-item-content>
                          </v-list-item>
                        </v-list>
                      </v-card>
                    </v-dialog>
                  </div>
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
import ExcelExport from 'export-xlsx';

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
      settingsDialog: false,
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

      SETTINGS_FOR_EXPORT: {
        fileName: 'app_inspector_project_overview',
        workSheets: [
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
            sheetName: 'Categories of component blocks',
            startingRowNumber: 2,
            gapBetweenTwoTables: 2,
            tableSettings: {
              data: {
                importable: true,
                tableTitle: 'Categories of component blocks',
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
      ],
    };
  },
  computed: {
    ...mapGetters({
      getAnalyzedData: 'files/getAnalyzedData',
    }),
  },
  methods: {
    setChartData(val) {
      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].builtInBlocks)) {
        console.log(key, value);
        this.chartDataBuiltInBlocks.labels.push(key);
        this.chartDataBuiltInBlocks.datasets[0].data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].componentBlocks)) {
        console.log(key, value);
        this.chartDataComponentBlocks.labels.push(key);
        this.chartDataComponentBlocks.datasets[0].data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(
        val[0].componentBlocksCategories
      )) {
        console.log(key, value);
        this.chartDataComponentBlocksCategories.labels.push(key);
        this.chartDataComponentBlocksCategories.datasets[0].data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(
        val[0].userInterfaceComponentBlocks
      )) {
        console.log(key, value);
        this.chartDataUIComponentBlocks.labels.push(key);
        this.chartDataUIComponentBlocks.datasets[0].data.push(value);
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
          this.chartDataBuiltInBlocks.datasets[0].data = sortedData;
          break;
        case 'componentBlocks':
          this.chartDataComponentBlocks.labels = sortedLabels;
          this.chartDataComponentBlocks.datasets[0].data = sortedData;
          break;
        case 'componentBlocksCategories':
          this.chartDataComponentBlocksCategories.labels = sortedLabels;
          this.chartDataComponentBlocksCategories.datasets[0].data = sortedData;
          break;
        case 'userInterfaceComponentBlocks':
          this.chartDataUIComponentBlocks.labels = sortedLabels;
          this.chartDataUIComponentBlocks.datasets[0].data = sortedData;
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
        case 'builtInBlocks':
          this.SETTINGS_FOR_EXPORT.workSheets[0].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[0].data = [tableDataMerged];
          break;
        case 'componentBlocks':
          this.SETTINGS_FOR_EXPORT.workSheets[1].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[1].data = [tableDataMerged];
          break;
        case 'componentBlocksCategories':
          this.SETTINGS_FOR_EXPORT.workSheets[2].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[2].data = [tableDataMerged];
          break;
        case 'userInterfaceComponentBlocks':
          this.SETTINGS_FOR_EXPORT.workSheets[3].tableSettings.data.headerDefinition = tableHeaders;
          this.dataToExport[3].data = [tableDataMerged];
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
        this.chartDataBuiltInBlocks.datasets[0].data
      );
      this.sortData(
        'componentBlocks',
        this.chartDataComponentBlocks.labels,
        this.chartDataComponentBlocks.datasets[0].data
      );
      this.sortData(
        'componentBlocksCategories',
        this.chartDataComponentBlocksCategories.labels,
        this.chartDataComponentBlocksCategories.datasets[0].data
      );
      this.sortData(
        'userInterfaceComponentBlocks',
        this.chartDataUIComponentBlocks.labels,
        this.chartDataUIComponentBlocks.datasets[0].data
      );

      //set all data to excel export
      this.setExportData(
        'builtInBlocks',
        this.chartDataBuiltInBlocks.labels,
        this.chartDataBuiltInBlocks.datasets[0].data
      );
      this.setExportData(
        'componentBlocks',
        this.chartDataComponentBlocks.labels,
        this.chartDataComponentBlocks.datasets[0].data
      );
      this.setExportData(
        'componentBlocksCategories',
        this.chartDataComponentBlocksCategories.labels,
        this.chartDataComponentBlocksCategories.datasets[0].data
      );
      this.setExportData(
        'userInterfaceComponentBlocks',
        this.chartDataUIComponentBlocks.labels,
        this.chartDataUIComponentBlocks.datasets[0].data
      );

      //render chart
      this.renderChart = true;
    },
  },
  watch: {
    getAnalyzedData: function (val) {
      if (val) {
        this.setData(val);
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
#icon:hover {
  color: #26a69a;
}
.card_title {
  font-weight: 700;
  font-size: 20px;
}
</style>
