<script>
import { Doughnut } from 'vue-chartjs';

export default {
  extends: Doughnut,
  name: 'DoughnutChart',
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
              data: this.myChartData,
            },
          ],
        },
        {
          maintainAspectRatio: false,
          responsive: true,
          legend: {
            position: 'right',
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
