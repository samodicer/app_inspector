<template>
  <v-card class="mx-auto" id="card" color="#F7F7F7">
    <v-toolbar color="#26a69a" dark>
      <v-toolbar-title>Uploaded files</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-checkbox
        v-if="getUploadedFiles.length != 0"
        hide-details
        color="#FFFFFF"
        v-model="headerCheck"
        @click="setChecked()"
      ></v-checkbox>
    </v-toolbar>
    <div id="loader" v-if="getLoading">
      <v-progress-circular indeterminate color="#26a69a"></v-progress-circular>
    </div>
    <div v-else-if="getUploadedFiles.length != 0">
      <v-card class="mx-auto" id="innerCard" color="#F7F7F7">
        <v-virtual-scroll
          :items="getUploadedFiles"
          height="300"
          item-height="50"
        >
          <template v-slot:default="{ item }">
            <v-list-item :key="item.id">
              <v-list-item-avatar width="30px" height="30px">
                <v-icon class="grey lighten-1" dark> mdi-file </v-icon>
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title v-text="item.title"></v-list-item-title>
              </v-list-item-content>

              <v-list-item-action class="field">
                <v-checkbox
                  v-model="selectedFiles"
                  color="#26a69a"
                  :value="item.id"
                ></v-checkbox>
              </v-list-item-action>
            </v-list-item>

            <v-divider></v-divider>
          </template>
        </v-virtual-scroll>
        <div class="btn">
          <v-btn color="#26A69A" dark @click="analyze()"> Analyse files </v-btn>
        </div>
      </v-card>
    </div>
    <div class="noData" v-else>
      <v-icon x-large> mdi-eye-off </v-icon>
      <p>No uploaded files</p>
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
      user_id: null,
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
      // ak sú vybrané nejaké súbory analyzujeme ich, ak nie zobrazíme snackbar
      if (this.selectedFiles.length != 0) {
        // id súborov pošleme na analýzu
        this.analyzeFile({
          ids: this.selectedFiles,
        });
        // zmeníme stav
        this.changeAnalysed(true);
        // presmerovanie na Overview
        if (this.$router.currentRoute.path != '/overview') {
          this.$router.push('overview');
        }
      } else {
        this.error_snackbar = true;
      }
    },
    setSelected(val) {
      // každý vybraný súbor pridáme do pola
      val.forEach((file) => this.selectedFiles.push(file.id));
    },
    setChecked() {
      // v hlavičke vyberieme všetky súbory alebo zrušíme výber
      if (this.headerCheck == true) {
        this.setSelected(this.getUploadedFiles);
      } else {
        this.selectedFiles = [];
      }
    },
  },
  watch: {
    getUploadedFiles: function (val) {
      // ak sa nahrajú súbory nastavíme ich ako vybrané
      if (val) {
        this.setSelected(val);
      }
    },
  },
  computed: {
    ...mapGetters({
      getUploadedFiles: 'files/getUploadedFiles',
      getLoading: 'files/getLoading',
      getUser: 'users/getUser',
    }),
  },
};
</script>

<style scoped>
.btn {
  text-align: center;
  padding: 10px;
}
#card {
  margin-top: 30px;
  margin-bottom: 0px !important;
  border-radius: 15px;
  padding: 0px !important;
}
#innerCard {
  margin-bottom: 0px !important;
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
  border-bottom-right-radius: 15px;
  border-bottom-left-radius: 15px;
  padding: 0px !important;
}
.field {
  margin-right: 8px;
}
#loader {
  padding: 30px;
}
.noData {
  color: grey;
  padding: 30px;
}
</style>
