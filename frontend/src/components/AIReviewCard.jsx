function AIReviewCard({ review }) {
  return (
    <div
      className="card shadow p-4 mt-4 hide-scrollbar"
      style={{
        maxHeight: "500px",
        overflowY: "auto",
        textAlign: "left",
        whiteSpace: "pre-wrap",
      }}
    >
      <h4 className="mb-4">
        🤖 AI Review
      </h4>

      <div
        style={{
          whiteSpace: "pre-wrap",
          lineHeight: "1.7",
        }}
      >
        {review}
      </div>
    </div>
  );
}

export default AIReviewCard;