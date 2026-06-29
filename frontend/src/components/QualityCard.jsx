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

  <span className="badge bg-secondary">
    {quality.length}
  </span>
</div>

      {quality.length === 0 ? (
        <p className="text-success mt-3">
          ✅ No Code Quality Issues
        </p>
      ) : (
        quality.map((issue, index) => (
          <div
            key={index}
            className="border rounded p-2 mb-3"
          >
            <span className="badge bg-primary mb-2">
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

export default QualityCard;