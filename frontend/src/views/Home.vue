<template>
  <v-app id="inspire">
    <Navbar></Navbar>
    <v-main class="grey lighten-3">
      <v-container id="content">
        <v-row>
          <v-col>
            <v-sheet id="sheet" rounded="lg">
              <UploadFiles></UploadFiles>
              <SelectFiles></SelectFiles>
              <v-divider id="divider"></v-divider>
              <AboutUs></AboutUs>
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
import UploadFiles from '../components/UploadFiles.vue';
import SelectFiles from '../components/SelectFiles.vue';
import AboutUs from '../components/AboutUs.vue';
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';

export default {
  name: 'Home',
  components: {
    UploadFiles,
    SelectFiles,
    AboutUs,
    Navbar,
    Footer,
  },
  data() {
    return {};
  },
  methods: {
    ...mapActions({
      resetStates: 'files/resetStates',
    }),
  },
  computed: {
    ...mapGetters({
      getUploaded: 'files/getUploaded',
    }),
  },
  mounted() {
    this.resetStates();
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
#divider {
  margin-top: 30px;
  margin-bottom: 30px;
}
</style>
