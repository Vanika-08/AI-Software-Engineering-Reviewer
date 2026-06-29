function NamingCard({ naming }) {
  return (
    <div
      className="card shadow p-4 h-100 hide-scrollbar"
      style={{
        maxHeight: "450px",
        overflowY: "auto",
      }}
    >
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h4>Naming Convention</h4>

        <span className="badge bg-secondary">
          {naming.length}
        </span>
      </div>

      {naming.length === 0 ? (
        <p className="text-success">
          ✅ Naming Convention Looks Good
        </p>
      ) : (
        naming.map((item, index) => (
          <div
            key={index}
            className="border rounded p-3 mb-3"
          >
            <span className="badge bg-info text-dark">
              {item.issue}
            </span>

            <br />

            <strong>{item.name}</strong>

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

export default NamingCard;