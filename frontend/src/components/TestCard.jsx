function TestCard({ tests }) {
  return (
    <div
      className="card shadow p-4 h-100 hide-scrollbar"
      style={{
        maxHeight: "450px",
        overflowY: "auto",
      }}
    >
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h4>Testing</h4>

        <span className="badge bg-secondary">
          {tests.length}
        </span>
      </div>

      {tests.map((item, index) => (
        <div
          key={index}
          className="border rounded p-3 mb-3"
        >
          <span
            className={`badge ${
              item.framework === "None"
                ? "bg-danger"
                : "bg-success"
            }`}
          >
            {item.framework}
          </span>

          <br />

          <small className="text-muted">
            {item.issue}
          </small>
        </div>
      ))}
    </div>
  );
}

export default TestCard;