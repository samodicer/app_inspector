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
              <h1 id="heading">Create account</h1>
              <v-text-field
                tabindex="1"
                v-model="user.username"
                label="Username"
                placeholder="Username"
                :rules="[
                  rules.required,
                  rules.username_min,
                  rules.username_max,
                ]"
                outlined
                dense
                color="#26A69A"
              ></v-text-field>
              <v-text-field
                tabindex="1"
                v-model="user.first_name"
                label="First name"
                placeholder="First name"
                :rules="[rules.required, rules.names_max]"
                outlined
                dense
                color="#26A69A"
              ></v-text-field>
              <v-text-field
                tabindex="1"
                v-model="user.last_name"
                label="Last name"
                placeholder="Last name"
                :rules="[rules.required, rules.names_max]"
                outlined
                dense
                color="#26A69A"
              ></v-text-field>
              <!--<v-text-field
                v-model="user.email"
                label="Email"
                placeholder="Email"
                :rules="[rules.required, rules.email]"
                outlined
                dense
                color="#26A69A"
              ></v-text-field>-->
              <v-text-field
                tabindex="1"
                v-model="user.password"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[
                  rules.required,
                  rules.password_min,
                  rules.password_max,
                ]"
                :type="show1 ? 'text' : 'password'"
                label="Password"
                hint="At least 8 characters"
                outlined
                dense
                @click:append="show1 = !show1"
                color="#26A69A"
              ></v-text-field>
              <v-text-field
                tabindex="1"
                v-model="user.confirm_password"
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[
                  rules.required,
                  rules.password_min,
                  rules.password_max,
                ]"
                :type="show2 ? 'text' : 'password'"
                label="Confirm password"
                hint="At least 8 characters"
                outlined
                dense
                @click:append="show2 = !show2"
                color="#26A69A"
              ></v-text-field>
              <div v-if="getRegisterErrorMessages.username">
                <v-alert
                  v-for="error in getRegisterErrorMessages.username"
                  :key="error"
                  dense
                  outlined
                  type="error"
                >
                  Username: {{ error }}
                </v-alert>
              </div>
              <div v-if="getRegisterErrorMessages.first_name">
                <v-alert
                  v-for="error in getRegisterErrorMessages.first_name"
                  :key="error"
                  dense
                  outlined
                  type="error"
                >
                  First name: {{ error }}
                </v-alert>
              </div>
              <div v-if="getRegisterErrorMessages.last_name">
                <v-alert
                  v-for="error in getRegisterErrorMessages.last_name"
                  :key="error"
                  dense
                  outlined
                  type="error"
                >
                  Last name: {{ error }}
                </v-alert>
              </div>
              <div v-if="getRegisterErrorMessages.password">
                <v-alert
                  v-for="error in getRegisterErrorMessages.password"
                  :key="error"
                  dense
                  outlined
                  type="error"
                >
                  Password: {{ error }}
                </v-alert>
              </div>
              <div class="btn">
                <v-btn tabindex="2" color="#26A69A" @click="createAcc()">
                  Create account
                </v-btn>
              </div>
            </div>
            <v-divider id="divider"></v-divider>
            <p>Already have an account?</p>
            <router-link v-bind:to="'/sign-in'">
              <p>Sign-in</p>
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
        username: '',
        password: '',
        confirm_password: '',
        first_name: '',
        last_name: '',
      },
      show1: false,
      show2: false,
      rules: {
        required: (value) => !!value || 'This field is required',
        username_min: (value) => {
          return value.length >= 2 || 'At least 2 characters';
        },
        username_max: (value) => {
          return value.length <= 30 || 'No more than 30 characters';
        },
        names_max: (value) => {
          return value.length <= 64 || 'No more than 64 characters';
        },
        password_min: (value) => {
          return value.length >= 8 || 'At least 8 characters';
        },
        password_max: (value) => {
          return value.length <= 256 || 'No more than 256 characters';
        },
        /*email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || 'Invalid Email';
        },*/
      },
      links: ['Sign in'],
      icons: ['mdi-facebook', 'mdi-twitter', 'mdi-linkedin', 'mdi-instagram'],
    };
  },
  methods: {
    ...mapActions({
      fetchFiles: 'files/fetchFiles',
      resetStates: 'files/resetStates',
      createAccount: 'users/userCreateAccount',
    }),
    createAcc() {
      this.createAccount(this.user).then(() => {
        this.$router.push({ name: 'SignIn' });
      });
    },
  },
  computed: {
    ...mapGetters({
      allFiles: 'files/allFiles',
      getUploaded: 'files/getUploaded',
      getRegisterErrorMessages: 'users/getRegisterErrorMessages',
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
