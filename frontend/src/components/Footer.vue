<template>
  <v-footer dark padless>
    <v-card
      flat
      tile
      class="teal lighten-1 white--text text-center"
      style="width: 100%"
    >
      <v-card-text>
        <v-btn
          v-for="link in links"
          :key="link.name"
          class="mx-4 white--text"
          icon
        >
          <v-icon
            size="24px"
            @click="loadPage(link.name)"
            :disabled="getUser.id != null"
          >
            {{ link.icon }}
          </v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="white--text pt-0">
        <p><b>CONTACT:</b> app.inspector.contact@gmail.com</p>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong>App Inspector</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  name: 'Footer',
  data() {
    return {
      links: [
        { icon: 'mdi-login-variant', name: 'SignIn' },
        { icon: 'mdi-account-plus-outline', name: 'CreateAccount' },
      ],
    };
  },
  computed: {
    ...mapGetters({
      getUser: 'users/getUser',
    }),
  },
  methods: {
    loadPage(name) {
      // ak sa odchytí udalosť kliknutia, nastane presmerovanie na stránku
      if (name == 'SignIn') {
        //ak sme na prihlasovacej stránke, presmerovanie nenastane
        if (this.$route.name != 'SignIn') {
          this.$router.push({ name: 'SignIn' });
        }
      } else {
        //ak sme na stránke registrácie, presmerovanie nenastane
        if (this.$route.name != 'CreateAccount') {
          this.$router.push({ name: 'CreateAccount' });
        }
      }
    },
  },
};
</script>

<style scoped></style>
