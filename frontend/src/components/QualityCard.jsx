function QualityCard({ quality }) {
  return (
    <div
      className="card shadow p-4 h-100 hide-scrollbar"
      style={{
        maxHeight: "450px",
        overflowY: "auto",
      }}
    >
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h4>Code Quality</h4>

        <span className="badge bg-secondary">{quality.length}</span>
      </div>

      {quality.length === 0 ? (
        <p className="text-success mt-3">✅ No Code Quality Issues</p>
      ) : (
        quality.map((issue, index) => (
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

export default QualityCard;
