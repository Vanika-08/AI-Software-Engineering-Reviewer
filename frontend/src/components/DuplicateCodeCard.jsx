function DuplicateCodeCard({ duplicateCode }) {

  return (
    <div
      className="card shadow p-4 h-100 hide-scrollbar"
      style={{
        maxHeight: "450px",
        overflowY: "auto",
      }}
    >
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h4>Duplicate Code</h4>

        <span className="badge bg-secondary">
          {duplicateCode.length}
        </span>
      </div>

      {duplicateCode.length === 0 ? (
        <p className="text-success">
          ✅ No Duplicate Code Found
        </p>
      ) : (
        duplicateCode.map((item, index) => (
          <div
            key={index}
            className="border rounded p-3 mb-3"
          >
            <span className="badge bg-danger">
              {item.similarity}% Similar
            </span>

            <p className="mt-2 mb-1">
              <strong>File 1</strong>
            </p>

            <small>
              {item.file1.split("/").slice(-2).join("/")}
            </small>

            <p className="mt-2 mb-1">
              <strong>File 2</strong>
            </p>

            <small>
              {item.file2.split("/").slice(-2).join("/")}
            </small>
          </div>
        ))
      )}
    </div>
  );
}

export default DuplicateCodeCard;