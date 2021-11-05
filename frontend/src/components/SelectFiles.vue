<template>
  <v-card class="mx-auto">
    <v-toolbar color="#26a69a" dark>
      <v-toolbar-title>Uploaded files</v-toolbar-title>
    </v-toolbar>

    <v-list subheader>
      <v-list-item v-for="file in getUploadedFiles" :key="file.id">
        <v-list-item-avatar width="30px" height="30px">
          <v-icon class="grey lighten-1" dark> mdi-file </v-icon>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-text="file.title"></v-list-item-title>

          <!--<v-list-item-subtitle
                        v-text="file.file"
                      ></v-list-item-subtitle>-->
        </v-list-item-content>

        <v-list-item-action>
          <v-checkbox
            v-model="selectedFiles"
            color="#26a69a"
            :value="file.id"
          ></v-checkbox>
        </v-list-item-action>
      </v-list-item>
    </v-list>
    <div class="btn" v-if="this.selectedFiles.length != 0">
      <router-link v-bind:to="'/overview'">
        <v-btn color="#26A69A" dark @click="analyze()"> Analyse files </v-btn>
      </router-link>
    </div>

    <v-snackbar v-model="snackbar">
      {{ snackbar_text }}

      <template v-slot:action="{ attrs }">
        <v-btn color="#26a69a" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-card>
  <!--  <v-card id="card" v-for="data in getAnalyzedData" :key="data.id">
    <div id="main_content2">
      <h1>Analysed data</h1>
      <v-row id="row">
        <v-col v-for="n in 6" :key="n" cols="4">
          <v-card id="card" height="100%" elevation="3" outlined>
            <div class="stat" v-if="n == 1">
              <p class="headline">Blocks</p>
              <p class="num_data">{{ data.number_of_blocks }}</p>
            </div>
            <div class="stat" v-if="n == 2">
              <p class="headline">Getters</p>
              <p class="num_data">{{ data.gets }}</p>
            </div>
            <div class="stat" v-if="n == 3">
              <p class="headline">Setters</p>
              <p class="num_data">{{ data.sets }}</p>
            </div>
            <div class="stat" v-if="n == 4">
              <p class="headline">Components</p>
              <div v-for="i in data.components" :key="i">
                <p class="text_data">{{ i }}</p>
              </div>
            </div>
            <div class="stat" v-if="n == 5">
              <p class="headline">Methods</p>
              <div v-for="i in data.methods" :key="i">
                <p class="text_data">{{ i }}</p>
              </div>
            </div>
            <div class="stat" v-if="n == 6">
              <p class="headline">Parameters</p>
              <div v-for="i in data.parameters" :key="i">
                <p class="text_data">{{ i }}</p>
              </div>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </v-card> -->
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'SelectFiles',
  components: {},
  data() {
    return {
      selectedFiles: [],
      snackbar: true,
      snackbar_text: 'Files has been successfully uploaded',
    };
  },
  methods: {
    ...mapActions({
      analyzeFile: 'files/analyzeFile',
    }),
    analyze() {
      if (this.selectedFiles.length != 0) {
        this.analyzeFile(this.selectedFiles);
      }
    },
    setSelected() {
      console.log('HER3E');
      for (let i = 0; i < this.getUploadedFiles; i++) {
        this.selectedFiles.push(this.files[i].id);
        console.log('HERE');
      }
    },
  },
  computed: {
    ...mapGetters({
      getUploadedFiles: 'files/getUploadedFiles',
    }),
  },
  mounted() {
    this.setSelected;
  },
};
</script>

<style scoped>
#main_content1 {
  padding: 20px;
  margin-left: 100px;
  margin-right: 100px;
}
#main_content2 {
  padding: 20px;
}
h1 {
  color: #26a69a;
  text-align: center;
}
.file_input {
  margin: auto;
}
.btn {
  text-align: center;
  padding: 10px;
}
#card {
  margin-top: 30px;
  margin-bottom: 30px;
  border-radius: 15px;
}
.stat {
  text-align: center;
}
.stat .headline {
  padding: 20px;
  color: #26a69a;
  text-align: center;
}
.stat .num_data {
  font-weight: bold;
  font-size: 70px;
  text-align: center;
}
.stat .text_data {
  font-weight: bold;
  font-size: 30px;
  text-align: center;
}
</style>
