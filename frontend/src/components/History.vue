<template>
  <div class="content" v-if="this.getHistory.length != 0">
    <div>
      <v-card class="mx-auto" color="#F7F7F7">
        <v-subheader inset>Uploaded files history</v-subheader>
        <v-divider></v-divider>
        <v-virtual-scroll
          :items="this.getHistory"
          height="530"
          item-height="70"
        >
          <template v-slot:default="{ item }">
            <v-list-item :key="item.analyse_id">
              <v-list-item-avatar width="40px" height="40px">
                <v-icon
                  :class="'blue'"
                  dark
                  v-text="'mdi-file-eye-outline'"
                ></v-icon>
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title
                  v-text="addPostfix(item.files_count)"
                ></v-list-item-title>
                <v-list-item-subtitle
                  v-text="formatDate(item.date)"
                ></v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-action>
                <v-btn
                  class="white--text"
                  tabindex="2"
                  color="#26A69A"
                  @click="analyze(item.files)"
                >
                  Analyse
                </v-btn>
              </v-list-item-action>
            </v-list-item>

            <v-divider></v-divider>
          </template>
        </v-virtual-scroll>
      </v-card>
    </div>
  </div>
  <div class="noData" v-else>
    <v-icon x-large> mdi-eye-off </v-icon>
    <p>No data to show</p>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Home',
  components: {},
  data() {
    return {};
  },
  methods: {
    ...mapActions({
      getUserHistory: 'users/getUserHistory',
      analyzeFile: 'files/analyzeFile',
      changeAnalysed: 'files/changeAnalysed',
      changeUploadedFiles: 'files/changeUploadedFiles',
    }),
    formatDate(dateStr) {
      // formátovanie dátumu
      var options = {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
      };
      const date = new Date(dateStr);
      return date.toLocaleDateString('en-US', options);
    },
    addPostfix(number) {
      // ak ju počet súborv viac ako 1, aplikujeme množného číslo (Files)
      if (number == 1) {
        return number + ' File';
      } else return number + ' Files';
    },
    analyze(files) {
      var ids = [];
      // ak sú nejaké súbory
      if (files.length != 0) {
        // pridáme do pola id súborov
        for (var i = 0; i < files.length; i++) {
          ids.push(files[i].id);
        }
        // id súborov sú posleané na anlýzu
        this.analyzeFile({ ids: ids });
        // zmeníme stavy
        this.changeUploadedFiles(files);
        this.changeAnalysed(true);
        // používateľ je presmerovaný na Overview
        if (this.$router.currentRoute.path != '/overview') {
          this.$router.push('overview');
        }
      }
    },
  },
  computed: {
    ...mapGetters({
      getUser: 'users/getUser',
      getHistory: 'users/getHistory',
    }),
  },
  mounted() {
    if (this.getUser.id != null) {
      // získame dáta histórie
      this.getUserHistory(this.getUser.id);
    }
  },
};
</script>

<style scoped>
.v-subheader {
  margin-left: 0px;
  font-weight: bold;
  color: rgb(224, 224, 224);
}
.noData {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 30px;
  color: grey;
}
</style>
