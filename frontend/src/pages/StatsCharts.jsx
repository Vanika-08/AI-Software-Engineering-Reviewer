import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

import { Pie } from "react-chartjs-2";

ChartJS.register(
  ArcElement,
  Tooltip,
  Legend
);

function StatsCharts({ stats }) {
  const frontendData = {
  labels: Object.keys(stats.frontend),
  datasets: [
    {
      data: Object.values(stats.frontend),
      backgroundColor: [
        "#0d6efd",
        "#198754",
        "#ffc107",
        "#dc3545",
        "#6f42c1",
        "#20c997",
        "#fd7e14",
        "#6610f2",
      ],
      borderColor: "#ffffff",
      borderWidth: 2,
    },
  ],
};

  const backendData = {
  labels: Object.keys(stats.backend),
  datasets: [
    {
      data: Object.values(stats.backend),
      backgroundColor: [
        "#198754",
        "#0d6efd",
        "#ffc107",
        "#dc3545",
        "#6f42c1",
        "#20c997",
        "#fd7e14",
        "#6610f2",
      ],
      borderColor: "#ffffff",
      borderWidth: 2,
    },
  ],
};

  return (
    <div className="row mt-5">

      <div className="col-md-4 mx-auto">
        <div className="card shadow p-4">

          <h4 className="mb-4">
            Frontend Distribution
          </h4>

          <Pie data={frontendData} />

        </div>
      </div>

      <div className="col-md-4 mx-auto">
        <div className="card shadow p-4">

          <h4 className="mb-4">
            Backend Distribution
          </h4>

          <Pie data={backendData} />

        </div>
      </div>

    </div>
  );
}

export default StatsCharts;