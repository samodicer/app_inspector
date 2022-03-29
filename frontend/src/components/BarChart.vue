<script>
import { Bar } from 'vue-chartjs';

export default {
  extends: Bar,
  name: 'BarChart',
  data() {
    return {
      backgroundColor: [
        '#F78585',
        '#F8AD72',
        '#F8EB78',
        '#CBF878',
        '#8FF878',
        '#78F8A8',
        '#78F8D5',
        '#78ECF8',
        '#78C2F8',
        '#7888F8',
        '#A278F8',
        '#D378F8',
        '#F878DF',
        '#D9D9D9',
        '#AA927D',
      ],
    };
  },
  props: ['chartData', 'chartLables'],
  mounted() {
    this.checkColors();
    this.renderMyChart();
  },
  methods: {
    checkColors() {
      // ak je viac stĺpcov ako farieb, použije sa rovnaká farba
      // ak nie, použijú sa definované farby
      if (this.chartData.length > this.backgroundColor.length) {
        this.backgroundColor = [];
        for (var i = 0; i < this.chartData.length; i++) {
          this.backgroundColor.push('#26a69a');
        }
      } else {
        this.backgroundColor = [];
        this.backgroundColor = [
          '#F78585',
          '#F8AD72',
          '#F8EB78',
          '#CBF878',
          '#8FF878',
          '#78F8A8',
          '#78F8D5',
          '#78ECF8',
          '#78C2F8',
          '#7888F8',
          '#A278F8',
          '#D378F8',
          '#F878DF',
          '#D9D9D9',
          '#AA927D',
        ];
      }
    },
    shuffle(array) {
      // náhodné poradie farieb
      let currentIndex = array.length,
        randomIndex;

      while (currentIndex != 0) {
        // výber náhodného indexu
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // zámena indexov
        [array[currentIndex], array[randomIndex]] = [
          array[randomIndex],
          array[currentIndex],
        ];
      }
      return array;
    },
    renderMyChart() {
      // vykreslíme graf za pomoci poslaných dát (chartLables, chartData)
      this.renderChart(
        {
          labels: this.$attrs['chartLabels'],
          datasets: [
            {
              backgroundColor: this.shuffle(this.backgroundColor),
              data: this.chartData,
            },
          ],
          annotation: {
            annotations: [
              {
                type: 'line',
                mode: 'horizontal',
                scaleID: 'y-axis-0',
                value: '10',
                borderColor: '#AA927D',
                borderWidth: 2,
              },
            ],
            drawTime: 'afterDraw', // (default)
          },
        },
        {
          maintainAspectRatio: false,
          responsive: true,
          legend: {
            display: false,
          },
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                  precision: 0,
                },
              },
            ],
          },
        }
      );
    },
  },
  watch: {
    chartData: function () {
      // ak sa zmení chartData, nastavíme farby a vykreslíme graf
      this.checkColors();
      this.renderMyChart();
    },
  },
};
</script>
