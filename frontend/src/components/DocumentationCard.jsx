function documentationCard({ documentation }) {
  return (
    <div
      className="card shadow p-4 h-100 hide-scrollbar"
      style={{
        maxHeight: "450px",
        overflowY: "auto",
      }}
    >
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h4>Documentation</h4>

        <span className="badge bg-secondary">{documentation.length}</span>
      </div>

      {documentation.length === 0 ? (
        <p className="text-success mt-3">✅ No Code documentation Issues</p>
      ) : (
        documentation.map((issue, index) => (
          <div key={index} className="border rounded p-2 mb-3">
            <span className="badge bg-primary">{issue.issue}</span>

            <div className="small text-muted mt-2">
              {issue.count} occurrence{issue.count > 1 ? "s" : ""}
            </div>

            <div className="small mt-2 text-break">
              {issue.file.split("/").slice(-2).join("/")}
            </div>
          </div>
        ))
      )}
    </div>
  );
}

export default documentationCard;
