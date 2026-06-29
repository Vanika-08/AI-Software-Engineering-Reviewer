function ArchitectureCard({ architecture }) {
  return (
    <div className="card shadow p-4 h-100">

      <h4 className="mb-3">
        Project Architecture
      </h4>

      {Object.entries(architecture).map(([key, value]) => (
        <div
          key={key}
          className="d-flex justify-content-between border-bottom py-2"
        >
          <span>
            {key.replace("_", " ").toUpperCase()}
          </span>

          <span>
            {value ? "✅" : "❌"}
          </span>
        </div>
      ))}

    </div>
  );
}

export default ArchitectureCard;