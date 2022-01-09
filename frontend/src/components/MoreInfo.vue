<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="700">
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          {{ type }}
        </v-card-title>

        <v-card-text style="margin-top: 20px">
          {{ text }}
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="#26a69a" text @click="dialog = false"> Close </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'MoreInfo',
  components: {},
  data() {
    return {
      dialog: true,
    };
  },
  props: {
    type: String,
    text: String,
  },
  methods: {
    ...mapActions({
      changeMoreInfoDialog: 'files/changeMoreInfoDialog',
    }),
  },
  watch: {
    dialog: function (val) {
      if (val == false) {
        this.changeMoreInfoDialog(false);
      }
    },
  },
  computed: {
    ...mapGetters({
      getMoreInfoDialog: 'files/getMoreInfoDialog',
    }),
  },
};
</script>

<style scoped></style>
