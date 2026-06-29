function AIReviewCard({ review }) {

  if (!review) return null;

  return (
    <div
      className="card shadow p-4 mt-4 hide-scrollbar"
      style={{
        maxHeight: "500px",
        overflowY: "auto",
        textAlign: "left",
      }}
    >
      <h4 className="mb-4">
        🤖 AI Review
      </h4>

      {Object.entries(review).map(([heading, content]) => (
        <div key={heading} className="mb-4">

          <h5 className="fw-bold">
            {heading}
          </h5>

          <p
            style={{
              whiteSpace: "pre-wrap",
              lineHeight: "1.7",
            }}
          >
            {content}
          </p>

          <hr />

        </div>
      ))}

    </div>
  );
}

export default AIReviewCard;