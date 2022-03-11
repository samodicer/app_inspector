<template>
  <v-container>
    <v-row id="content">
      <v-sheet id="sheet" rounded="lg" color="#F7F7F7" elevation="2">
        <v-row id="row">
          <v-col>
            <v-sheet id="sheet" rounded="lg" color="#FFFFFF" elevation="2">
              <h1 id="heading" style="justify-content: start">
                <v-icon id="icon" large color="#26a69a"> mdi-school</v-icon>
                Educational
              </h1>
              <p id="text">
                By using App Inspector, you can gain new insights into your AIA
                projects and improve them.
              </p>
              <h1 id="heading" style="justify-content: start">
                <v-icon id="icon" large color="#26a69a">
                  mdi-speedometer</v-icon
                >
                Fast
              </h1>
              <p id="text">
                Analysing AIA projects with App Inspector is quick and easy.
              </p>
              <h1 id="heading" style="justify-content: start">
                <v-icon id="icon" large color="#26a69a">
                  mdi-check-circle-outline</v-icon
                >
                Free
              </h1>
              <p id="text">
                With App Inspector, you can analyse your AIA projects for free.
              </p>
            </v-sheet>
          </v-col>
          <v-col>
            <v-sheet
              id="sheet"
              rounded="lg"
              color="#FFFFFF"
              elevation="2"
              style="height: 100%"
            >
              <h1 id="heading">
                Analyse your MIT App Inventor projects <br />via App Inspector
              </h1>
              <v-sparkline
                :height="50"
                :value="value"
                :gradient="gradient"
                :smooth="radius || false"
                :padding="padding"
                :line-width="width"
                :stroke-linecap="lineCap"
                :gradient-direction="gradientDirection"
                :fill="fill"
                :type="type"
                :auto-line-width="autoLineWidth"
                auto-draw
              ></v-sparkline>
            </v-sheet>
          </v-col>
        </v-row>
        <v-card id="card">
          <v-row id="row">
            <v-col id="col">
              <h1 id="heading2">What is</h1>
              <h1 id="heading3">App Inspector?</h1>
            </v-col>
            <v-divider id="devider" class="mx-4" vertical></v-divider>
            <v-col id="col">
              <p id="aboutText">
                App Inspector is an online tool that allows you to analyse and
                compare multiple MIT App Inventor projects. The results can be
                used for statistical analysis or educational purposes.
              </p>
            </v-col>
          </v-row>
        </v-card>
      </v-sheet>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: 'SelectFiles',
  components: {},
  data() {
    return {
      width: 6,
      radius: 10,
      padding: 14,
      lineCap: 'round',
      gradient: ['#1c857b', '#32d1c2', '#24f2cc'],
      value: Array.from({ length: 17 }, () => Math.floor(Math.random() * 22)),
      gradientDirection: 'top',
      fill: false,
      type: 'trend',
      autoLineWidth: false,
    };
  },
  methods: {},
  watch: {},
  computed: {},
};
</script>

<style scoped>
#heading {
  display: flex;
  justify-content: center;
  align-items: center;
}
#heading2 {
  text-align: center;
  font-size: 50px;
}
#heading3 {
  text-align: center;
  font-size: 25px;
}
#aboutText {
  display: flex;
  align-items: center;
  text-align: left;
  font-size: 25px;
}
#devider {
  margin-left: 30px;
  margin-right: 30px;
}
#col {
  padding: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-left: 10px;
}
#row {
  margin: 10px;
}
#card {
  display: flex;
  margin-top: 30px;
  border-radius: 15px;
  margin: 20px;
}
#icon {
  margin-right: 5px;
}
#text {
  text-align: left;
}
#sheet {
  width: 100%;
  padding: 30px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
#content {
  display: flex;
  justify-content: center;
  align-items: center;
}
@media only screen and (max-width: 800px) {
  #heading {
    font-size: 20px;
  }
  #heading2 {
    font-size: 20px;
  }
  #heading3 {
    font-size: 20px;
  }
  #row {
    flex-direction: column;
  }
  #aboutText {
    padding: 0x;
    font-size: 16px;
    text-align: center;
  }
  #col {
    padding: 20px;
    min-width: 180px;
  }
  #card {
    flex-direction: column;
  }
  #devider {
    display: none;
  }
  #row {
    flex-direction: column;
  }
}
</style>
