<template>
  <div class="content" v-if="this.getUser.id != null">
    <v-row align="center" justify="center">
      <v-col>
        <v-avatar id="avatar" color="blue">
          <v-icon id="icon" dark> mdi-account </v-icon>
        </v-avatar>
        <h1 id="heading">{{ this.getUser.username }}</h1>
        <v-divider id="divider"></v-divider>
        <h2 id="text">
          {{ this.getUser.first_name + ' ' + this.getUser.last_name }}
        </h2>
      </v-col>
    </v-row>
  </div>
  <div class="noData" v-else>
    <v-icon x-large> mdi-eye-off </v-icon>
    <p>No data to show</p>
  </div>
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
  width: 200px;
  margin-top: 5px;
  margin-bottom: 10px;
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
.noData {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 30px;
  color: grey;
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
    margin-top: 10px;
    margin-bottom: 10px;
  }
  .content {
    padding-top: 100px;
  }
}
</style>
