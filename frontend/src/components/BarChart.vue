<script>
import { Bar } from 'vue-chartjs';

export default {
  extends: Bar,
  name: 'BarChart',
  props: ['chartData', 'chartLables'],
  mounted() {
    this.renderMyChart();
  },
  methods: {
    renderMyChart() {
      this.renderChart(
        {
          labels: this.$attrs['chartLabels'],
          datasets: [
            {
              backgroundColor: [
                '#FBA92A',
                '#F54141',
                '#FFF80B',
                '#4BF148',
                '#EA2FCD',
                '#8934C8',
                '#1A90E7',
                '#0AD68F',
                '#04B9C8',
                '#9D9D9D',
                '#E670B8',
                '#764903',
                '#C296E1',
                '#000000',
                '#F15757',
              ],
              data: this.chartData,
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
      this.renderMyChart();
    },
  },
};
</script>
