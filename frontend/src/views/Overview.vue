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
                      :chartData="this.chartDataBuiltInBlocks.data"
                      :chartLabels="this.chartDataBuiltInBlocks.labels"
                      class="doughnut-chart"
                    ></DoughnutChart>
                  </v-sheet>
                </v-col>
                <v-col>
                  <v-sheet id="sheet" rounded="lg" color="#F7F7F7">
                    <p class="card_title">Component blocks</p>
                    <DoughnutChart
                      :chartData="this.chartDataComponentBlocks.data"
                      :chartLabels="this.chartDataComponentBlocks.labels"
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
                      :chartData="this.chartDataComponentBlocksCategories.data"
                      :chartLabels="
                        this.chartDataComponentBlocksCategories.labels
                      "
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
                      :chartData="this.chartDataUIComponentBlocks.data"
                      :chartLabels="this.chartDataUIComponentBlocks.labels"
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
                          <v-toolbar-title>Settings</v-toolbar-title>
                          <v-spacer></v-spacer>
                          <v-toolbar-items>
                            <v-btn dark text @click="settingsDialog = false">
                              <v-icon>mdi-close</v-icon>
                            </v-btn>
                          </v-toolbar-items>
                        </v-toolbar>
                        <SelectFiles></SelectFiles>
                      </v-card>
                    </v-dialog>
                  </div>
                </v-col>
              </v-row>
            </v-sheet>
            <v-sheet v-else style="padding: 50px">
              <v-icon style="margin-right: 10px" x-large> mdi-eye-off</v-icon>
              <p>No data to analyse</p>
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
import SelectFiles from '../components/SelectFiles.vue';

export default {
  name: 'Overview',
  components: {
    DoughnutChart,
    BarChart,
    SelectFiles,
  },
  data() {
    return {
      //analyzedData: Object,
      renderChart: false,
      settingsDialog: false,
      links: ['Dashboard', 'Messages', 'Profile', 'Updates'],
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
        this.chartDataBuiltInBlocks.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(val[0].componentBlocks)) {
        console.log(key, value);
        this.chartDataComponentBlocks.labels.push(key);
        this.chartDataComponentBlocks.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(
        val[0].componentBlocksCategories
      )) {
        console.log(key, value);
        this.chartDataComponentBlocksCategories.labels.push(key);
        this.chartDataComponentBlocksCategories.data.push(value);
      }

      //populate labels and data from server response data
      for (const [key, value] of Object.entries(
        val[0].userInterfaceComponentBlocks
      )) {
        console.log(key, value);
        this.chartDataUIComponentBlocks.labels.push(key);
        this.chartDataUIComponentBlocks.data.push(value);
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

      //set all data to excel export
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

      //render charts
      this.renderChart = true;
    },
    resetData() {
      this.chartDataBuiltInBlocks.labels = [];
      this.chartDataBuiltInBlocks.data = [];
      this.chartDataComponentBlocks.labels = [];
      this.chartDataComponentBlocks.data = [];
      this.chartDataComponentBlocksCategories.labels = [];
      this.chartDataComponentBlocksCategories.data = [];
      this.chartDataUIComponentBlocks.labels = [];
      this.chartDataUIComponentBlocks.data = [];

      this.SETTINGS_FOR_EXPORT.workSheets[0].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[1].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[2].tableSettings.data.headerDefinition = [];
      this.SETTINGS_FOR_EXPORT.workSheets[3].tableSettings.data.headerDefinition = [];
      this.dataToExport[0].data = [];
      this.dataToExport[1].data = [];
      this.dataToExport[2].data = [];
      this.dataToExport[3].data = [];
    },
  },
  watch: {
    getAnalyzedData: function (val) {
      if (val) {
        this.resetData();
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
