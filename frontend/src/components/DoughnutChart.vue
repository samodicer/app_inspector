<script>
import { Doughnut } from 'vue-chartjs';

export default {
  extends: Doughnut,
  name: 'DoughnutChart',
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
  computed: {
    myChartData: function () {
      return this.chartData;
    },
    myChartLabels: function () {
      return this.chartLables;
    },
  },
  mounted() {
    this.renderMyChart();
  },
  methods: {
    shuffle(array) {
      let currentIndex = array.length,
        randomIndex;

      // While there remain elements to shuffle...
      while (currentIndex != 0) {
        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
          array[randomIndex],
          array[currentIndex],
        ];
      }

      return array;
    },
    renderMyChart() {
      this.renderChart(
        {
          labels: this.$attrs['chartLabels'],
          datasets: [
            {
              backgroundColor: this.shuffle(this.backgroundColor),
              data: this.myChartData,
            },
          ],
        },
        {
          maintainAspectRatio: false,
          responsive: true,
          legend: {
            position: 'bottom',
            align: 'middle',
          },
        }
      );
    },
  },
  watch: {
    chartData: function () {
      this.renderMyChart();
    },
    myChartLabels: function () {
      this.renderMyChart();
    },
  },
};
</script>
