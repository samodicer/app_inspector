<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat height="80px">
      <v-container class="py-0 fill-height">
        <img
          class="logo"
          src="../assets/images/logo.png"
          height="70px"
          @click="refreshByClick"
        />
        <img
          class="logo2"
          src="../assets/images/logo2.png"
          height="70px"
          @click="refreshByClick"
        />
        <v-spacer></v-spacer>
        <p
          style="margin-bottom: 0px"
          v-if="this.getUser.username"
          class="font-weight-black"
        >
          {{ this.getUser.username }}
        </p>
        <v-btn v-if="accessToken" text @click="logout()"> Sign-out</v-btn>
        <v-btn v-if="!accessToken" text @click="loadSignInPage()">
          Sign-in</v-btn
        >
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container id="content">
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
            <v-sheet id="sheet" rounded="lg">
              <UploadFiles></UploadFiles>
              <!--<p>uploaded files on server:</p>
              <div v-for="doc in allFiles" :key="doc.id" class="files">
                  <b>{{doc}}</b>
              </div>-->
              <div v-if="this.getUploaded">
                <SelectFiles></SelectFiles>
              </div>
              <v-divider id="divider"></v-divider>
              <AboutUs></AboutUs>
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
import UploadFiles from '../components/UploadFiles.vue';
import SelectFiles from '../components/SelectFiles.vue';
import AboutUs from '../components/AboutUs.vue';

export default {
  name: 'Home',
  components: {
    UploadFiles,
    SelectFiles,
    AboutUs,
  },
  data() {
    return {
      accessToken: localStorage.getItem('accessToken'),
      icons: ['mdi-facebook', 'mdi-twitter', 'mdi-linkedin', 'mdi-instagram'],
    };
  },
  methods: {
    ...mapActions({
      fetchFiles: 'files/fetchFiles',
      resetStates: 'files/resetStates',
      userLogout: 'users/userLogout',
      getCurrentUser: 'users/getCurrentUser',
    }),
    refreshByClick() {
      this.$router.go();
    },
    loadSignInPage() {
      this.$router.push('sign-in');
    },
    logout() {
      this.userLogout();
      location.reload();
    },
  },
  computed: {
    ...mapGetters({
      allFiles: 'files/allFiles',
      getUploaded: 'files/getUploaded',
      getUploadedFiles: 'files/getUploadedFiles',
      getUser: 'users/getUser',
    }),
  },
  mounted() {
    this.fetchFiles();
    this.resetStates();
    this.getCurrentUser(this.accessToken);
  },
};
</script>

<style scoped>
#inspire {
  text-align: center;
}
#sheet {
  padding: 30px;
  min-height: 720px;
}
#content {
  margin-bottom: 50px;
}
.logo {
  display: none;
}
.logo2 {
  display: block;
  cursor: pointer;
}
#divider {
  margin-top: 30px;
  margin-bottom: 30px;
}
@media only screen and (max-width: 450px) {
  .logo {
    display: block;
    cursor: pointer;
  }
  .logo2 {
    display: none;
  }
}
</style>
