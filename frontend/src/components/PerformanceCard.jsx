function PerformanceCard({ performance }) {
  return (
    <div
      className="card shadow p-4 h-100 hide-scrollbar"
      style={{
        maxHeight: "450px",
        overflowY: "auto",
      }}
    >
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h4>Performance</h4>

        <span className="badge bg-secondary">
          {performance.length}
        </span>
      </div>

      {performance.length === 0 ? (
        <p className="text-success">
          ✅ No Performance Issues
        </p>
      ) : (
        performance.map((issue, index) => (
          <div
            key={index}
            className="border rounded p-2 mb-3"
          >
            <span className="badge bg-warning text-dark mb-2">
              {issue.issue}
            </span>

            <br />

            <small className="text-muted">
              {issue.file.split("/").slice(-2).join("/")}
            </small>
          </div>
        ))
      )}
    </div>
  );
}

export default PerformanceCard;