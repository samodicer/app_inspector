<template>
  <v-container>
    <v-row id="content">
      <v-sheet id="sheet" rounded="lg" color="#F7F7F7" elevation="2">
        <v-row id="row">
          <v-col>
            <v-sheet id="sheet" rounded="lg" color="#FFFFFF" elevation="2">
              <h1 id="heading">
                <v-icon large color="#26a69a"> mdi-speedometer</v-icon>
                Fast
              </h1>
              <p id="text">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry.
              </p>
              <h1 id="heading">
                <v-icon large color="#26a69a"> mdi-check-circle-outline</v-icon>
                Free
              </h1>
              <p id="text">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry.
              </p>
              <h1 id="heading">
                <v-icon large color="#26a69a"> mdi-school</v-icon>
                Instructive
              </h1>
              <p id="text">
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry.
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
              <h1 id="heading" style="text-align: center">
                Analyse your MIT App Inventor <br />
                projects via App Inspector
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
        <h1 id="heading" style="margin-top: 30px; text-align: center">
          What is App Inspector?
        </h1>
        <br />
        <p style="text-align: left">
          Contrary to popular belief, Lorem Ipsum is not simply random text. It
          has roots in a piece of classical Latin literature from 45 BC, making
          it over 2000 years old. Richard McClintock, a Latin professor at
          Hampden-Sydney College in Virginia, looked up one of the more obscure
          Latin words, consectetur, from a Lorem Ipsum passage, and going
          through the cites of the word in classical literature, discovered the
          undoubtable source. Lorem Ipsum comes from sections 1.10.32 and
          1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and
          Evil) by Cicero, written in 45 BC. This book is a treatise on the
          theory of ethics, very popular during the Renaissance. The first line
          of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in
          section 1.10.32. The standard chunk of Lorem Ipsum used since the
          1500s is reproduced below for those interested. Sections 1.10.32 and
          1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also
          reproduced in their exact original form, accompanied by English
          versions from the 1914 translation by H. Rackham.
        </p>
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
      width: 3,
      radius: 10,
      padding: 14,
      lineCap: 'round',
      gradient: ['#1c857b', '#32d1c2', '#24f2cc'],
      value: Array.from({ length: 17 }, () => Math.floor(Math.random() * 20)),
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
  text-align: left;
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
  #row {
    flex-direction: column;
  }
}
</style>
