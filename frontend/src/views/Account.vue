<template>
  <v-app id="inspire">
    <Navbar></Navbar>
    <v-main class="grey lighten-3">
      <v-container id="content">
        <v-sheet id="sheet" rounded="lg">
          <v-card id="card" color="#F7F7F7">
            <v-tabs
              v-model="tabs"
              background-color="#26a69a"
              centered
              dark
              icons-and-text
            >
              <v-tabs-slider></v-tabs-slider>

              <v-tab href="#tab-1">
                Profile
                <v-icon>mdi-account-box</v-icon>
              </v-tab>

              <v-tab href="#tab-2">
                History
                <v-icon>mdi-folder-clock</v-icon>
              </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tabs">
              <v-tab-item :value="'tab-1'">
                <Profile></Profile>
              </v-tab-item>
              <v-tab-item :value="'tab-2'">
                <History></History>
              </v-tab-item>
            </v-tabs-items>
          </v-card>
        </v-sheet>
      </v-container>
      <Footer></Footer>
    </v-main>
  </v-app>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';
import Profile from '../components/Profile.vue';
import History from '../components/History.vue';

export default {
  name: 'Account',
  components: {
    Navbar,
    Footer,
    Profile,
    History,
  },
  data() {
    return {
      tabs: null,
    };
  },
  methods: {
    ...mapActions({}),
  },
  computed: {
    ...mapGetters({}),
  },
  mounted() {},
};
</script>

<style scoped>
#inspire {
  text-align: center;
}
#sheet {
  padding: 30px;
  min-height: 720px;
  display: flex;
  justify-content: center;
}
#card {
  width: 100%;
  border-radius: 15px;
}
#content {
  margin-bottom: 50px;
}
.theme--light.v-tabs-items {
  background-color: #f7f7f7 !important;
}
</style>
