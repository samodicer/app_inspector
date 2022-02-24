<template>
  <v-card color="#F7F7F7">
    <div class="content">
      <v-list subheader two-line color="#F7F7F7">
        <v-subheader inset>File upload history</v-subheader>
        <v-divider></v-divider>
        <div v-for="file in files" :key="file.title">
          <v-list-item>
            <v-list-item-avatar>
              <v-icon :class="file.color" dark v-text="file.icon"></v-icon>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title v-text="file.title"></v-list-item-title>

              <v-list-item-subtitle
                v-text="file.subtitle"
              ></v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <v-btn class="white--text" tabindex="2" color="#26A69A">
                Show
              </v-btn>
            </v-list-item-action>
          </v-list-item>
          <v-divider></v-divider>
        </div>
      </v-list>
    </div>
  </v-card>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Home',
  components: {},
  data() {
    return {
      files: [
        {
          color: 'blue',
          icon: 'mdi-clipboard-text',
          subtitle: 'Jan 20, 2014',
          title: 'Vacation itinerary',
        },
        {
          color: 'blue',
          icon: 'mdi-clipboard-text',
          subtitle: 'Feb 10, 2014',
          title: 'Kitchen remodel',
        },
      ],
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
.content {
  padding-top: 20px;
}
.v-subheader {
  margin-left: 0px;
  font-weight: bold;
}
</style>
