<template>
  <v-card id="card">
    <div id="main_content1">
      <h1>Select files to upload</h1>
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

      <v-alert
        :value="alert"
        color="#26A69A"
        border="left"
        transition="scale-transition"
        type="error"
      >
        <p style="color: white">
          <b>{{ alert_text }}</b>
        </p>
        <div class="text-center">
          <v-btn
            class="black--text"
            rounded
            color="white"
            dark
            @click="
              alert = false;
              uploaded = false;
              crashed = false;
            "
          >
            Okay
          </v-btn>
        </div>
      </v-alert>
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
      alert: false,
      alert_text: '',
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
      changeUploaded: 'files/changeUploaded',
      changeUploadedFiles: 'files/changeUploadedFiles',
    }),

    onSelected() {
      this.crashed = false;
      this.alert = false;
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
            this.alert = true;
            this.alert_text =
              'The file type must be aia (MIT App Inventor Project File)';
            this.inputs.files = [];
            this.$refs.fileInputRef = null;
            break;
          }
        }

        /*for (var value of fd.values()) {
          console.log(value);
        }*/
        if (!this.crashed) {
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
            console.log(response);
          });
          this.uploaded = true;
          this.changeUploaded(true);
          this.changeUploadedFiles(this.uploaded_files);
        }
      } else {
        this.crashed = true;
        this.alert = true;
        this.alert_text = 'You have not selected any files.';
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
#main_content1 {
  padding: 20px;
  margin-left: 100px;
  margin-right: 100px;
}
#main_content2 {
  padding: 20px;
}
h1 {
  color: #26a69a;
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
  margin-top: 30px;
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
</style>
