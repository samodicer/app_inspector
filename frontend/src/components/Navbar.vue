<template>
  <v-app-bar app color="white" flat height="80px">
    <v-container class="py-0 fill-height">
      <img
        class="logo"
        src="../assets/images/logo.png"
        height="70px"
        @click="refreshByClick()"
      />
      <img
        class="logo2"
        src="../assets/images/logo2.png"
        height="70px"
        @click="refreshByClick()"
      />
      <v-spacer></v-spacer>
      <div id="user" v-if="this.getUser.id != null">
        <v-menu
          bottom
          left
          offset-y
          transition="slide-x-transition"
          :rounded="'lg'"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-avatar
              style="cursor: pointer"
              color="blue"
              size="38"
              v-bind="attrs"
              v-on="on"
            >
              <v-icon dark> mdi-account </v-icon>
            </v-avatar>
          </template>

          <v-list>
            <v-list-item style="cursor: pointer" @click="loadProfilePage()">
              <v-list-item-title>{{ options[0].item }}</v-list-item-title>
            </v-list-item>
            <v-list-item style="cursor: pointer" @click="logout()">
              <v-list-item-title>{{ options[1].item }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
      <v-btn v-if="this.getUser.id == null" text @click="loadSignInPage()">
        Sign in</v-btn
      >
    </v-container>
  </v-app-bar>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Navbar',
  data() {
    return {
      accessToken: localStorage.getItem('accessToken'),
      options: [{ item: 'Profile' }, { item: 'Sign out' }],
    };
  },
  methods: {
    ...mapActions({
      userLogout: 'users/userLogout',
      getCurrentUser: 'users/getCurrentUser',
      refreshAccessToken: 'users/refreshAccessToken',
    }),
    refreshByClick() {
      if (this.$route.name != 'Home') {
        this.$router.push({ name: 'Home' });
      } else {
        this.$router.go();
      }
    },
    loadSignInPage() {
      if (this.$route.name != 'SignIn') {
        this.$router.push('sign-in');
      }
    },
    logout() {
      this.userLogout().then(() => {
        this.$router.go();
      });
    },
    loadProfilePage() {
      if (this.$route.name != 'Profile') {
        this.$router.push('profile');
      }
    },
  },
  computed: {
    ...mapGetters({
      getUser: 'users/getUser',
    }),
  },
  mounted() {
    this.refreshAccessToken().then(() => {
      this.getCurrentUser(localStorage.getItem('accessToken'));
    });
  },
};
</script>

<style scoped>
.logo {
  display: none;
}
.logo2 {
  display: block;
  cursor: pointer;
}
#user {
  display: inline-flex;
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
