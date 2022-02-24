<template>
  <v-card color="#F7F7F7">
    <div class="content">
      <v-row align="center" justify="center">
        <v-col>
          <v-avatar id="avatar" color="blue" v-bind="attrs" v-on="on">
            <v-icon id="icon" dark> mdi-account </v-icon>
          </v-avatar>

          <h1 id="heading">{{ this.getUser.username }}</h1>
          <h2 id="text">
            {{ this.getUser.first_name + ' ' + this.getUser.last_name }}
          </h2>
          <v-divider id="divider"></v-divider>
          <router-link v-bind:to="'/sign-in'">
            <p style="margin-top: 20px">Edit profile</p>
          </router-link>
        </v-col>
      </v-row>
    </div>
  </v-card>
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
    ...mapActions({}),
  },
  computed: {
    ...mapGetters({
      getUser: 'users/getUser',
    }),
  },
  mounted() {},
};
</script>

<style scoped>
.content {
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 60px;
}
#heading {
  margin-top: 10px;
}
#divider {
  margin: auto;
  width: 300px;
}
#avatar {
  width: 180px !important;
  height: 180px !important;
}
#text {
  margin-bottom: 20px;
}
#icon {
  font-size: 140px;
}
@media only screen and (max-width: 500px) {
  #heading {
    font-size: 20px;
  }
  #text {
    font-size: 16px;
  }
  #avatar {
    width: 120px !important;
    height: 120px !important;
  }
  #icon {
    font-size: 90px;
  }
  #divider {
    width: 150px;
  }
  .content {
    padding-top: 100px;
  }
}
</style>
