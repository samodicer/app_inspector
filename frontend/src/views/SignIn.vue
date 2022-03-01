<template>
  <v-app id="inspire">
    <Navbar></Navbar>
    <v-main class="grey lighten-3">
      <v-container id="content">
        <v-sheet id="sheet" rounded="lg">
          <v-card id="card" color="#F7F7F7">
            <div class="form">
              <h1 id="heading">Sign in</h1>
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
                v-model="user.username"
                label="Username"
                placeholder="Username"
                :rules="[rules.required]"
                outlined
                dense
                color="#26A69A"
              ></v-text-field>
              <v-text-field
                tabindex="1"
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
              <div v-if="getLoginErrorMessages.username">
                <v-alert
                  v-for="error in getLoginErrorMessages.username"
                  :key="error"
                  dense
                  outlined
                  type="error"
                >
                  Username: {{ error }}
                </v-alert>
              </div>
              <div v-if="getLoginErrorMessages.password">
                <v-alert
                  v-for="error in getLoginErrorMessages.password"
                  :key="error"
                  dense
                  outlined
                  type="error"
                >
                  Password: {{ error }}
                </v-alert>
              </div>
              <v-alert
                v-if="this.getLoginErrorMessages.detail"
                dense
                outlined
                type="error"
              >
                {{ this.getLoginErrorMessages.detail }}
              </v-alert>
              <div class="btn">
                <v-btn
                  class="white--text"
                  tabindex="2"
                  color="#26A69A"
                  @click="login()"
                >
                  Sign in
                </v-btn>
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
      <Footer></Footer>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';

export default {
  name: 'SignIn',
  components: {
    Navbar,
    Footer,
  },
  data() {
    return {
      user: {
        username: '',
        password: '',
      },
      incorrectAuth: false,
      show: false,
      rules: {
        required: (value) => !!value || 'This field is required',
        min: (value) => {
          return value.length >= 8 || 'At least 8 characters';
        },
        /*email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || 'Invalid Email';
        },*/
      },
    };
  },
  methods: {
    ...mapActions({
      userLogin: 'users/userLogin',
      refreshMessages: 'users/refreshMessages',
    }),
    login() {
      this.userLogin(this.user)
        .then(() => {
          this.$router.push({ name: 'Home' });
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
    },
  },
  computed: {
    ...mapGetters({
      getUploaded: 'files/getUploaded',
      getLoginErrorMessages: 'users/getLoginErrorMessages',
    }),
  },
  mounted() {
    this.refreshMessages();
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
@media only screen and (max-width: 500px) {
  #heading {
    font-size: 20px;
  }
}
</style>
