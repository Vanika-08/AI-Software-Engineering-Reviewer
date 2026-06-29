import { useEffect, useState } from "react";
import api from "../services/api";
import StatsCharts from "./StatsCharts";

function StatsPage() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    const loadStats = async () => {
      try {
        const response = await api.get("/stats");
        setStats(response.data);
      } catch (err) {
        console.error(err);
      }
    };

    loadStats();
  }, []);

  if (!stats) {
    return (
      <div className="container py-5 text-center">
        <h3>Loading Analytics...</h3>
      </div>
    );
  }

  return (
    <>
    <div className="container py-5">

      <h2 className="mb-5">
        📊 Project Analytics
      </h2>

      <div className="row g-4">

        <div className="col-md-3">
          <div className="card shadow text-center p-4 h-100">
            <h6>Total Reviews</h6>
            <h2 className="text-primary">
              {stats.total_reviews}
            </h2>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card shadow text-center p-4 h-100">
            <h6>Average Score</h6>
            <h2 className="text-success">
              {stats.average_score}
            </h2>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card shadow text-center p-4 h-100">
            <h6>Best Score</h6>
            <h2 className="text-success">
              {stats.best_score}
            </h2>
          </div>
        </div>

        <div className="col-md-3">
          <div className="card shadow text-center p-4 h-100">
            <h6>Lowest Score</h6>
            <h2 className="text-danger">
              {stats.worst_score}
            </h2>
          </div>
        </div>

      </div>

      <div className="row mt-5 g-4">

        <div className="col-md-4">
          <div className="card shadow p-4 h-100">

            <h4 className="mb-3">
              ⚛️ Frontend
            </h4>

            {Object.entries(stats.frontend).map(([tech, count]) => (
              <span
                key={tech}
                className="badge bg-primary me-2 mb-2 fs-6"
              >
                {tech} ({count})
              </span>
            ))}

          </div>
        </div>

        <div className="col-md-4">
          <div className="card shadow p-4 h-100">

            <h4 className="mb-3">
              🚀 Backend
            </h4>

            {Object.entries(stats.backend).map(([tech, count]) => (
              <span
                key={tech}
                className="badge bg-success me-2 mb-2 fs-6"
              >
                {tech} ({count})
              </span>
            ))}

          </div>
        </div>

        <div className="col-md-4">
          <div className="card shadow p-4 h-100">

            <h4 className="mb-3">
              🗄 Database
            </h4>

            {Object.entries(stats.database).map(([tech, count]) => (
              <span
                key={tech}
                className="badge bg-dark me-2 mb-2 fs-6"
              >
                {tech} ({count})
              </span>
            ))}

          </div>
        </div>

      </div>

    </div>
    <StatsCharts stats={stats} />
    </>
  );
}

export default StatsPage;