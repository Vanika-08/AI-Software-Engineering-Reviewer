import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

function AnalyticsChart({ result }) {
  const data = [
    {
      name: "Security",
      value: result.security.length,
    },
    {
      name: "Quality",
      value: result.quality.length,
    },
    {
      name: "Performance",
      value: result.performance.length,
    },
  ];

  const COLORS = [
    "#ef4444",
    "#3b82f6",
    "#f59e0b",
  ];

  return (
    <div className="card shadow p-4 mt-4">
      <h4 className="mb-3">
        Issue Distribution
      </h4>

      <ResponsiveContainer width="100%" height={320}>
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            outerRadius={110}
            label
          >
            {data.map((entry, index) => (
              <Cell
                key={index}
                fill={COLORS[index]}
              />
            ))}
          </Pie>

          <Tooltip />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

export default AnalyticsChart;