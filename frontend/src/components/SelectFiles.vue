<template>
  <v-card class="mx-auto" id="card" color="#F7F7F7">
    <v-toolbar color="#26a69a" dark>
      <v-toolbar-title>Uploaded files</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-checkbox
        hide-details
        color="#FFFFFF"
        v-model="headerCheck"
        @click="setChecked()"
      ></v-checkbox>
    </v-toolbar>
    <div id="loader" v-if="getLoading">
      <v-progress-circular indeterminate color="#26a69a"></v-progress-circular>
    </div>
    <v-list subheader color="#F7F7F7">
      <v-list-item v-for="file in getUploadedFiles" :key="file.id">
        <v-list-item-avatar width="30px" height="30px">
          <v-icon class="grey lighten-1" dark> mdi-file </v-icon>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-text="file.title"></v-list-item-title>
        </v-list-item-content>

        <v-list-item-action class="field">
          <v-checkbox
            v-model="selectedFiles"
            color="#26a69a"
            :value="file.id"
          ></v-checkbox>
        </v-list-item-action>
      </v-list-item>
    </v-list>
    <div class="btn">
      <v-btn color="#26A69A" dark @click="analyze()"> Analyse files </v-btn>
    </div>
    <v-snackbar v-if="error_snackbar" v-model="error_snackbar" timeout="3000">
      {{ error_snackbar_text }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="#26a69a"
          text
          v-bind="attrs"
          @click="error_snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-card>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'SelectFiles',
  components: {},
  data() {
    return {
      selectedFiles: [],
      headerCheck: true,
      error_snackbar: false,
      error_snackbar_text: 'You have not selected any files.',
    };
  },
  methods: {
    ...mapActions({
      analyzeFile: 'files/analyzeFile',
      changeAnalysed: 'files/changeAnalysed',
    }),
    analyze() {
      if (this.selectedFiles.length != 0) {
        this.analyzeFile(this.selectedFiles);
        this.changeAnalysed(true);
        console.log('route: ' + this.$router.currentRoute.path);
        if (this.$router.currentRoute.path != '/overview') {
          this.$router.push('overview');
        }
      } else {
        this.error_snackbar = true;
      }
    },
    setSelected(val) {
      val.forEach((file) => this.selectedFiles.push(file.id));
    },
    setChecked() {
      if (this.headerCheck == true) {
        this.setSelected(this.getUploadedFiles);
      } else {
        this.selectedFiles = [];
      }
    },
  },
  watch: {
    getUploadedFiles: function (val) {
      if (val) {
        this.setSelected(val);
      }
    },
  },
  computed: {
    ...mapGetters({
      getUploadedFiles: 'files/getUploadedFiles',
      getLoading: 'files/getLoading',
    }),
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
.field {
  margin-right: 8px;
}
#loader {
  margin-top: 10px;
}
</style>
