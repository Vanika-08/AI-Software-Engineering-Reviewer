function ComplexityCard({ complexity }) {
  return (
    <div
      className="card shadow p-4 h-100 hide-scrollbar"
      style={{
        maxHeight: "450px",
        overflowY: "auto",
      }}
    >
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h4>Code Complexity</h4>

        <span className="badge bg-secondary">
          {complexity.length}
        </span>
      </div>

      {complexity.length === 0 ? (
        <p className="text-success mt-3">
          ✅ No Complexity Issues
        </p>
      ) : (
        complexity.map((issue, index) => (
          <div
            key={index}
            className="border rounded p-3 mb-3"
          >
            <span className="badge bg-danger mb-2">
              {issue.issue}
            </span>

            <br />

            <small className="text-muted d-block mb-2">
              {issue.file.split("/").slice(-2).join("/")}
            </small>

            <small>
              IF: {issue.if_count} | Loops: {issue.loop_count} | Returns: {issue.return_count}
            </small>
          </div>
        ))
      )}
    </div>
  );
}

export default ComplexityCard;