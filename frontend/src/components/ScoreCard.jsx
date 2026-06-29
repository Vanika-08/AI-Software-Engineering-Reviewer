function ScoreCard({ score }) {

  const getColor = () => {
    if (score >= 80) return "text-success";
    if (score >= 60) return "text-warning";
    return "text-danger";
  };

  const getBarColor = () => {
    if (score >= 80) return "bg-success";
    if (score >= 60) return "bg-warning";
    return "bg-danger";
  };

  const getStatus = () => {
    if (score >= 80) return "Excellent";
    if (score >= 60) return "Good";
    if (score >= 40) return "Needs Improvement";
    return "Poor";
  };

  return (
    <div className="card shadow h-100 p-4">

      <h4>Overall Score</h4>

      <p className="mt-2">
        {getStatus()}
      </p>

      <h1 className={getColor()}>
        {score}/100
      </h1>

      <div className="progress mt-3" style={{ height: "22px" }}>
        <div
          className={`progress-bar ${getBarColor()}`}
          role="progressbar"
          style={{ width: `${score}%` }}
        >
          {score}%
        </div>
      </div>

    </div>
  );
}

export default ScoreCard;