function SecurityCard({ security }) {
    const badgeColor = {
  LOW: "bg-success",
  MEDIUM: "bg-warning text-dark",
  HIGH: "bg-danger",
  CRITICAL: "bg-dark",
};
  return (
    <div
  className="card shadow p-4 h-100 hide-scrollbar"
  style={{
    maxHeight: "400px",
    overflowY: "auto",
  }}
>
      <h4>Security Findings</h4>

      {security.length === 0 ? (
        <p className="text-success">
          No Security Issues 🎉
        </p>
      ) : (
        security.map((issue, index) => (
          <div key={index} className="mb-2">
            <span className={`badge ${badgeColor[issue.severity]}`}>
  {issue.severity}
</span>

            <div>{issue.issue}</div>

            <small title={issue.file}>
  {issue.file.split("/").slice(-2).join("/")}
</small>
          </div>
        ))
      )}
    </div>
  );
}

export default SecurityCard;