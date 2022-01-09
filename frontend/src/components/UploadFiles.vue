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
      <div v-if="!this.uploaded" class="btn">
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
import { mapActions } from 'vuex';
import axios from 'axios';

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
      uploaded_files: [],
      current_file_id: null,
      selectedFiles: [],
    };
  },
  methods: {
    ...mapActions({
      fetchFiles: 'files/fetchFiles',
      analyzeFile: 'files/analyzeFile',
      changeLoading: 'files/changeLoading',
      changeUploaded: 'files/changeUploaded',
      changeUploadedFiles: 'files/changeUploadedFiles',
    }),

    onSelected() {
      this.crashed = false;
      this.error_snackbar = false;
      //this.inputs.title = this.inputs.files.name;
      if (this.inputs.files.length != 0) {
        const fd = new FormData();
        for (let i = 0; i < this.inputs.files.length; i++) {
          var idxDot = this.inputs.files[i].name.lastIndexOf('.') + 1;
          var extFile = this.inputs.files[i].name
            .substr(idxDot, this.inputs.files[i].name.length)
            .toLowerCase();
          if (extFile == 'aia') {
            fd.append('files', this.inputs.files[i]);
          } else {
            this.crashed = true;
            this.error_snackbar = true;
            this.error_snackbar_text =
              'The file type must be aia (MIT App Inventor Project File).';
            this.inputs.files = [];
            this.$refs.fileInputRef = null;
            break;
          }
        }

        /*for (var value of fd.values()) {
          console.log(value);
        }*/
        if (!this.crashed) {
          this.changeLoading(true);
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/upload-file/',
            data: fd,
            body: fd,
          }).then((response) => {
            //this.inputs.id = response.data.id;
            for (let i = 0; i < response.data.length; i++) {
              var myFile = [];
              myFile['id'] = response.data[i].id;
              myFile['title'] = response.data[i].title;
              myFile['file'] = response.data[i].file;
              this.uploaded_files.push(myFile);
              this.selectedFiles.push(myFile['id']);
            }
            this.changeLoading(false);
            console.log(response);
          });
          this.uploaded = true;
          this.changeUploaded(true);
          this.changeUploadedFiles(this.uploaded_files);
        }
      } else {
        this.crashed = true;
        this.error_snackbar = true;
        this.error_snackbar_text = 'You have not selected any files.';
      }

      if (this.inputs.files) {
        /*var idxDot = this.inputs.file.name.lastIndexOf('.') + 1;
        var extFile = this.inputs.file.name
          .substr(idxDot, this.inputs.file.name.length)
          .toLowerCase();
        if (extFile == 'aia') {
          const fd = new FormData();
          fd.append('title', this.inputs.title);
          fd.append('file', this.inputs.file);
          axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/upload-file/',
            data: fd,
            body: fd,
          }).then((response) => {
            this.inputs.id = response.data.id;
            console.log(response);
          });
          this.uploaded = true;
        } else {
          this.alert = true;
          this.inputs.file = null;
          this.inputs.title = '';
          this.$refs.fileInputRef = null;
          console.log(this.$refs.fileInputRef);
        }*/
      }
    },
    analyze() {
      this.analyzeFile(this.selectedFiles);
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
