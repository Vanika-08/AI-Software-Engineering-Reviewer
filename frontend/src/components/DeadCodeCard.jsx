function DeadCodeCard({ deadCode }) {
  return (
    <div
      className="card shadow p-4 h-100 hide-scrollbar"
      style={{
        maxHeight: "450px",
        overflowY: "auto",
      }}
    >
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h4>Dead Code</h4>

        <span className="badge bg-secondary">
          {deadCode.length}
        </span>
      </div>

      {deadCode.length === 0 ? (
        <p className="text-success">
          ✅ No Dead Code Found
        </p>
      ) : (
        deadCode.map((item, index) => (
          <div
            key={index}
            className="border rounded p-3 mb-3"
          >
            <span className="badge bg-warning text-dark">
              {item.issue}
            </span>

            <br />

            <small className="text-muted">
              {item.file.split("/").slice(-2).join("/")}
            </small>
          </div>
        ))
      )}
    </div>
  );
}

export default DeadCodeCard;