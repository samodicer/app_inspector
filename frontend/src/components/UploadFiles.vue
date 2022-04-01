<template>
  <v-card id="card" color="#F7F7F7">
    <div id="main_content">
      <h1 id="heading">Select files to upload</h1>
      <div class="file_input">
        <v-file-input
          id="fi"
          class="d-flex pa-2"
          v-model="inputs.files"
          multiple="multiple"
          ref="fileInputRef"
          color="black"
          counter
          show-size
          truncate-length="40"
        ></v-file-input>
      </div>

      <div v-if="!this.getUploaded" class="btn">
        <v-btn color="#26A69A" dark @click="onSelected()"> Upload files </v-btn>
      </div>

      <v-snackbar v-if="error_snackbar" v-model="error_snackbar" timeout="3000">
        {{ error_snackbar_text }}

        <template v-slot:action="{ attrs }">
          <v-btn
            color="#26a69a"
            text
            v-bind="attrs"
            @click="error_snackbar = false"
          >
            Close
          </v-btn>
        </template>
      </v-snackbar>

      <v-snackbar v-if="uploaded" v-model="success_snackbar" timeout="5000">
        {{ success_snackbar_text }}

        <template v-slot:action="{ attrs }">
          <v-btn
            color="#26a69a"
            text
            v-bind="attrs"
            @click="success_snackbar = false"
          >
            Close
          </v-btn>
        </template>
      </v-snackbar>
    </div>
  </v-card>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
//import axios from 'axios';

export default {
  name: 'UploadFiles',
  components: {},
  data() {
    return {
      success_snackbar: true,
      success_snackbar_text: 'Files has been successfully uploaded.',
      error_snackbar: false,
      error_snackbar_text: '',
      uploaded: false,
      crashed: false,
      inputs: {
        files: [],
      },
    };
  },
  computed: {
    ...mapGetters({
      getUser: 'users/getUser',
      getUploaded: 'files/getUploaded',
    }),
  },
  methods: {
    ...mapActions({
      analyzeFile: 'files/analyzeFile',
      uploadFiles: 'files/uploadFiles',
      changeLoading: 'files/changeLoading',
      changeUploaded: 'files/changeUploaded',
    }),

    onSelected() {
      this.crashed = false;
      this.error_snackbar = false;
      // ak používateľ zvolil nejaké súbory
      if (this.inputs.files.length != 0) {
        const fd = new FormData();
        // ak je požívateľ prihlásený vložíme id, ak nie vložíme -1
        if (this.getUser.id != null) {
          fd.append('user_id', this.getUser.id);
        } else {
          fd.append('user_id', -1);
        }
        // prebehneme po súboroch
        for (let i = 0; i < this.inputs.files.length; i++) {
          // zoberieme koncovku súboru
          var idxDot = this.inputs.files[i].name.lastIndexOf('.') + 1;
          var extFile = this.inputs.files[i].name
            .substr(idxDot, this.inputs.files[i].name.length)
            .toLowerCase();

          if (extFile == 'aia') {
            // ak je koncovka aia, tak pridáme súbor do pola
            fd.append('files', this.inputs.files[i]);
          } else {
            // ak nie, zobrazíme chybu
            this.crashed = true;
            this.error_snackbar = true;
            this.error_snackbar_text =
              'The file type must be AIA (App Inventor Application).';
            this.inputs.files = [];
            this.$refs.fileInputRef = null;
            break;
          }
        }

        if (!this.crashed) {
          // zmeníme stavy a nahráme súbory
          this.changeLoading(true);
          this.uploadFiles(fd).then(() => {
            this.changeLoading(false);
          });
          this.uploaded = true;
          this.changeUploaded(true);
        }
      } else {
        this.crashed = true;
        this.error_snackbar = true;
        this.error_snackbar_text = 'You have not selected any files.';
      }
    },
  },
};
</script>

<style scoped>
#main_content {
  padding: 20px;
  margin-left: 100px;
  margin-right: 100px;
}
#heading {
  color: #000000;
  text-align: center;
}
.file_input {
  margin: auto;
}
.btn {
  text-align: center;
  padding: 10px;
}
#card {
  margin-bottom: 30px;
  border-radius: 15px;
}
.stat {
  text-align: center;
}
.stat .headline {
  padding: 20px;
  color: #26a69a;
  text-align: center;
}
.stat .num_data {
  font-weight: bold;
  font-size: 70px;
  text-align: center;
}
.stat .text_data {
  font-weight: bold;
  font-size: 30px;
  text-align: center;
}
@media only screen and (max-width: 800px) {
  #heading {
    font-size: 20px;
  }
  #main_content {
    padding: 20px;
    margin-left: 0px;
    margin-right: 0px;
  }
}
</style>
