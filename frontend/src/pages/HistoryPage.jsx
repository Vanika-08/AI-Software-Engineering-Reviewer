import { useEffect, useState } from "react";
import api from "../services/api";
import ReactMarkdown from "react-markdown";

function HistoryPage() {
  const [reviews, setReviews] = useState([]);
  const [search, setSearch] = useState("");
  const [sortBy, setSortBy] = useState("newest");
  const [selectedReview, setSelectedReview] = useState(null);

  const getBadgeClass = (score) => {
    if (score >= 80) return "bg-success";
    if (score >= 60) return "bg-warning text-dark";
    return "bg-danger";
  };

  const loadReviews = async () => {
  try {
    const response = await api.get("/reviews");
    setReviews(response.data);
  } catch (err) {
    console.error(err);
  }
};

useEffect(() => {
  loadReviews();
}, []);

  const filteredReviews = reviews.filter((review) => {
    const frontend = review.technologies.frontend || "";
    const backend = review.technologies.backend || "";
    const database = review.technologies.database || "";

    return (
      frontend.toLowerCase().includes(search.toLowerCase()) ||
      backend.toLowerCase().includes(search.toLowerCase()) ||
      database.toLowerCase().includes(search.toLowerCase())
    );
  });

  const sortedReviews = [...filteredReviews];

  switch (sortBy) {
    case "highest":
      sortedReviews.sort(
        (a, b) => b.score.overall_score - a.score.overall_score
      );
      break;

    case "lowest":
      sortedReviews.sort(
        (a, b) => a.score.overall_score - b.score.overall_score
      );
      break;

    case "oldest":
      sortedReviews.reverse();
      break;

    default:
      break;
  }

  const deleteReview = async (reviewId) => {

  if (!window.confirm("Delete this review?")) return;

  try {

    await api.delete(`/reviews/${reviewId}`);

    loadReviews();

  } catch (error) {

    console.error(error);

  }

};

  return (
    <div className="container py-5">
      <h2 className="mb-4">Review History</h2>

      <div className="row mb-4">
        <div className="col-md-6">
          <input
            type="text"
            className="form-control"
            placeholder="Search by Technology..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>

        <div className="col-md-3">
          <select
            className="form-select"
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
          >
            <option value="newest">Newest</option>
            <option value="oldest">Oldest</option>
            <option value="highest">Highest Score</option>
            <option value="lowest">Lowest Score</option>
          </select>
        </div>
      </div>

      <table className="table table-bordered table-hover align-middle">
        <thead className="table-dark">
          <tr>
            <th>#</th>
            <th>Date</th>
            <th>Score</th>
            <th>Frontend</th>
            <th>Backend</th>
            <th>Database</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {sortedReviews.length === 0 ? (
            <tr>
              <td colSpan="6" className="text-center py-4">
                No Reviews Found
              </td>
            </tr>
          ) : (
            sortedReviews.map((review, index) => (
              <tr key={index}>
                <td>{index + 1}</td>

                <td>{review.created_at || "-"}</td>

                <td>
                  <span
                    className={`badge ${getBadgeClass(
                      review.score.overall_score
                    )}`}
                  >
                    {review.score.overall_score}/100
                  </span>
                </td>

                <td>{review.technologies.frontend || "-"}</td>

                <td>{review.technologies.backend || "-"}</td>

                <td>{review.technologies.database || "-"}</td>
                <td>
  <button
    className="btn btn-sm btn-primary me-2"
    onClick={() => setSelectedReview(review)}
  >
    View
  </button>

  <button
    className="btn btn-sm btn-danger"
    onClick={() => deleteReview(review.id)}
  >
    Delete
  </button>
</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
      {selectedReview && (
  <div className="card shadow mt-5 p-4">

    <div className="d-flex justify-content-between align-items-center">

      <h3>Review Details</h3>

      <button
        className="btn btn-danger"
        onClick={() => setSelectedReview(null)}
      >
        Close
      </button>

    </div>

    <hr />

    <p>
      <strong>Score:</strong>{" "}
      {selectedReview.score.overall_score}/100
    </p>

    <p>
      <strong>Frontend:</strong>{" "}
      {selectedReview.technologies.frontend || "-"}
    </p>

    <p>
      <strong>Backend:</strong>{" "}
      {selectedReview.technologies.backend || "-"}
    </p>

    <p>
      <strong>Database:</strong>{" "}
      {selectedReview.technologies.database || "-"}
    </p>

    <hr />

    <h5>AI Review</h5>

    {selectedReview.ai_review &&
      Object.entries(selectedReview.ai_review).map(
        ([heading, content]) => (
          <div key={heading} className="mb-3">

            <h6>{heading}</h6>

            <p style={{ whiteSpace: "pre-wrap" }}>
              <ReactMarkdown>{content}</ReactMarkdown>
            </p>

          </div>
        )
      )}

  </div>
)}
    </div>
  );
}

export default HistoryPage;