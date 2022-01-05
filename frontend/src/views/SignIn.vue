<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat height="80px">
      <v-container class="py-0 fill-height">
        <router-link v-bind:to="'/'">
          <img class="logo" src="../assets/images/logo.png" height="70px" />
        </router-link>
        <router-link v-bind:to="'/'">
          <img class="logo2" src="../assets/images/logo2.png" height="70px" />
        </router-link>
        <v-spacer></v-spacer>
        <v-btn v-for="link in links" :key="link" text>
          {{ link }}
        </v-btn>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container id="content">
        <v-sheet id="sheet" rounded="lg">
          <v-card id="card" color="#F7F7F7">
            <div class="form">
              <h1 id="heading">Sign-in</h1>
              <v-text-field
                v-model="user.email"
                label="Email"
                placeholder="Email"
                :rules="[rules.required, rules.email]"
                outlined
                dense
                color="#26A69A"
              ></v-text-field>
              <v-text-field
                v-model="user.password"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[rules.required, rules.min]"
                :type="show ? 'text' : 'password'"
                label="Password"
                hint="At least 8 characters"
                outlined
                dense
                @click:append="show = !show"
                color="#26A69A"
              ></v-text-field>
              <div class="btn">
                <v-btn color="#26A69A" dark> Sign-in </v-btn>
              </div>
            </div>
            <v-divider id="divider"></v-divider>
            <p>New to App Insepctor?</p>
            <router-link v-bind:to="'/create-account'">
              <p>Create new account</p>
            </router-link>
          </v-card>
        </v-sheet>
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

export default {
  name: 'Home',
  components: {},
  data() {
    return {
      user: {
        email: '',
        password: '',
      },
      show: false,
      rules: {
        required: (value) => !!value || 'This field is required',
        min: (value) => {
          return value.length >= 8 || 'At least 8 characters';
        },
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || 'Invalid Email';
        },
      },
      links: ['Sign in'],
      icons: ['mdi-facebook', 'mdi-twitter', 'mdi-linkedin', 'mdi-instagram'],
    };
  },
  methods: {
    ...mapActions({
      fetchFiles: 'files/fetchFiles',
      resetStates: 'files/resetStates',
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
  display: flex;
  align-items: center;
  justify-content: center;
}
#card {
  padding: 30px;
  width: 500px;
  border-radius: 15px;
}
.form {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.btn {
  padding: 10px;
}
.logo {
  cursor: pointer;
}
#heading {
  padding: 10px;
}
#divider {
  margin-top: 20px;
  margin-bottom: 20px;
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
