function TechnologyCard({ technologies }) {
  return (
   <div className="card shadow h-100 p-4">
      <h4>Technology Stack</h4>

      <p>
        <strong>Frontend:</strong>{" "}
        {technologies.frontend || "Not Detected"}
      </p>

      <p>
        <strong>Backend:</strong>{" "}
        {technologies.backend || "Not Detected"}
      </p>

      <p>
        <strong>Database:</strong>{" "}
        {technologies.database || "Not Detected"}
      </p>
    </div>
  );
}

export default TechnologyCard;