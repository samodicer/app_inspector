<!--<template>
    <div>
        <div>
            <label for="file">Choose aia file to upload</label><br>
            <input type="file" id="file" name="file" ref="fileInputRef" @change="onSelected"><br><br>
            <div v-if="this.uploaded" class="message"><b>Nahral si "{{this.inputs.title}}"</b></div>
            <div v-if="this.uploaded" class="btn">
                <button @click="analyze()"> analyzovat </button>
            </div>
        </div>
        <br><br>
        <p>uploaded files on server:</p>
        <div v-for="doc in allFiles" :key="doc.id" class="files">
            <b>{{doc}}</b>
        </div>
        <div v-for="data in getAnalyzedData" :key="data.id" class="analyzed_data">
            Number of blocks:{{data.number_of_blocks}}<br>
            Getters:{{data.gets}}<br>
            Setters:{{data.sets}}<br>
            Components:{{data.components}}<br>
            Methods:{{data.methods}}<br> 
        </div>
    </div>
</template>-->
<template>
  <v-app id="inspire">
    <v-app-bar app color="white" flat>
      <v-container class="py-0 fill-height">
        <v-avatar tile class="mr-10" color="#26A69A" size="50">
          <span class="white--text headline">AI</span>
        </v-avatar>
        <v-btn v-for="link in links" :key="link" text>
          {{ link }}
        </v-btn>

        <v-spacer></v-spacer>

        <v-responsive max-width="260">
          <v-text-field
            dense
            flat
            hide-details
            rounded
            solo-inverted
          ></v-text-field>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list color="transparent">
                <v-list-item v-for="n in 5" :key="n" link>
                  <v-list-item-content>
                    <v-list-item-title> List Item {{ n }} </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>

                <v-divider class="my-2"></v-divider>

                <v-list-item link color="grey lighten-4">
                  <v-list-item-content>
                    <v-list-item-title> Refresh </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet id="sheet" min-height="70vh" rounded="lg">
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
                    <v-btn color="#26A69A" dark @click="onSelected()">
                      Upload files
                    </v-btn>
                  </div>
                  <h2 v-if="this.uploaded">
                    Files has been successfully uploaded
                  </h2>
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
              <!--<p>uploaded files on server:</p>
              <div v-for="doc in allFiles" :key="doc.id" class="files">
                  <b>{{doc}}</b>
              </div>-->

              <v-card
                max-width="600"
                class="mx-auto"
                v-if="uploaded_files.length != 0"
              >
                <v-toolbar color="#26a69a" dark>
                  <v-toolbar-title>Uploaded files</v-toolbar-title>
                </v-toolbar>

                <v-list subheader two-line>
                  <v-list-item v-for="file in uploaded_files" :key="file.id">
                    <v-list-item-avatar>
                      <v-icon class="grey lighten-1" dark> mdi-file </v-icon>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title
                        v-text="file.title"
                      ></v-list-item-title>

                      <!--<v-list-item-subtitle
                        v-text="file.file"
                      ></v-list-item-subtitle>-->
                    </v-list-item-content>

                    <v-list-item-action>
                      <v-checkbox
                        v-model="selectedFiles"
                        color="#26a69a"
                        :value="file.id"
                      ></v-checkbox>
                    </v-list-item-action>
                  </v-list-item>
                </v-list>
                <div v-if="this.uploaded" class="btn">
                  <v-btn color="#26A69A" dark @click="analyze()">
                    Analyse files
                  </v-btn>
                </div>
              </v-card>
              <v-card id="card" v-for="data in getAnalyzedData" :key="data.id">
                <div id="main_content2">
                  <h1>Analysed data</h1>
                  <v-row id="row">
                    <v-col v-for="n in 6" :key="n" cols="4">
                      <v-card id="card" height="100%" elevation="3" outlined>
                        <div class="stat" v-if="n == 1">
                          <p class="headline">Blocks</p>
                          <p class="num_data">{{ data.number_of_blocks }}</p>
                        </div>
                        <div class="stat" v-if="n == 2">
                          <p class="headline">Getters</p>
                          <p class="num_data">{{ data.gets }}</p>
                        </div>
                        <div class="stat" v-if="n == 3">
                          <p class="headline">Setters</p>
                          <p class="num_data">{{ data.sets }}</p>
                        </div>
                        <div class="stat" v-if="n == 4">
                          <p class="headline">Components</p>
                          <div v-for="i in data.components" :key="i">
                            <p class="text_data">{{ i }}</p>
                          </div>
                        </div>
                        <div class="stat" v-if="n == 5">
                          <p class="headline">Methods</p>
                          <div v-for="i in data.methods" :key="i">
                            <p class="text_data">{{ i }}</p>
                          </div>
                        </div>
                        <div class="stat" v-if="n == 6">
                          <p class="headline">Parameters</p>
                          <div v-for="i in data.parameters" :key="i">
                            <p class="text_data">{{ i }}</p>
                          </div>
                        </div>
                      </v-card>
                    </v-col>
                  </v-row>
                </div>
              </v-card>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import axios from 'axios';

export default {
  name: 'Home',
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
      links: ['Dashboard', 'Messages', 'Profile', 'Updates'],
      selectedFiles: [],
    };
  },
  methods: {
    ...mapActions({
      fetchFiles: 'documents/fetchFiles',
      analyzeFile: 'documents/analyzeFile',
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
  computed: {
    ...mapGetters({
      allFiles: 'documents/allFiles',
      getAnalyzedData: 'documents/getAnalyzedData',
    }),
  },
  mounted() {
    this.fetchFiles();
  },
};
</script>

<style scoped>
#inspire {
  text-align: center;
}
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
#sheet {
  padding: 30px;
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
.row {
  margin-bottom: 50px;
}
</style>
