<template>
  <v-card class="mx-auto" id="card">
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

    <v-list subheader>
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
    <div class="btn" v-if="this.selectedFiles.length != 0">
      <router-link v-bind:to="'/overview'">
        <v-btn color="#26A69A" dark @click="analyze()"> Analyse files </v-btn>
      </router-link>
    </div>
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
    setSelected(val) {
      val.forEach((file) => this.selectedFiles.push(file.id));
    },
    setChecked() {
      console.log('som tu a val:' + this.headerCheck);
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
</style>
