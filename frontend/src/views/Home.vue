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
          <!-- <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list color="transparent">
                <v-list-item v-for="n in 5" :key="n" link>
                  <v-list-item-content>
                    <v-list-item-title> List Item {{ n }} </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>

                <v-divider class="my-2"></v-divider>

                <v-list-item link color="grey lighten-4">
                  <v-list-item-content>
                    <v-list-item-title> Refresh </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>-->

          <v-col>
            <v-sheet id="sheet" min-height="70vh" rounded="lg">
              <UploadFiles></UploadFiles>
              <!--<p>uploaded files on server:</p>
              <div v-for="doc in allFiles" :key="doc.id" class="files">
                  <b>{{doc}}</b>
              </div>-->
              <div v-if="this.getUploaded">
                <SelectFiles></SelectFiles>
              </div>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import UploadFiles from '../components/UploadFiles.vue';
import SelectFiles from '../components/SelectFiles.vue';

export default {
  name: 'Home',
  components: {
    UploadFiles,
    SelectFiles,
  },
  data() {
    return {
      links: ['Dashboard', 'Messages', 'Profile', 'Updates'],
    };
  },
  methods: {
    ...mapActions({
      fetchFiles: 'files/fetchFiles',
    }),
  },
  computed: {
    ...mapGetters({
      allFiles: 'files/allFiles',
      getUploaded: 'files/getUploaded',
    }),
  },
  mounted() {
    this.fetchFiles();
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
</style>
