<script>
import { Line } from 'vue-chartjs';

export default {
  extends: Line,
  name: 'LineChart',
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
    this.renderMyChart();
  },
  methods: {
    shuffle(array) {
      // náhodné poradie farieb
      let currentIndex = array.length,
        randomIndex;

      // výber náhodného indexu
      while (currentIndex != 0) {
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
              fill: false,
              tension: 0,
              borderWidth: 5,
              pointBorderWidth: 2,
              pointRadius: 5,
              borderColor: '#9D9D9D',
            },
          ],
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
      // ak sa zmení chartData, vykreslíme graf
      this.renderMyChart();
    },
  },
};
</script>
