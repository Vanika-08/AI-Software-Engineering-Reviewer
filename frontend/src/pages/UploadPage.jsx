import { useState } from "react";
import api from "../services/api";
import ScoreCard from "../components/ScoreCard";
import TechnologyCard from "../components/TechnologyCard";
import StructureCard from "../components/StructureCard";
import SecurityCard from "../components/SecurityCard";
import QualityCard from "../components/QualityCard";
import PerformanceCard from "../components/PerformanceCard";
import ArchitectureCard from "../components/ArchitectureCard";
import AIReviewCard from "../components/AIReviewCard";
import AnalyticsChart from "../components/AnalyticsChart";
import LoadingSpinner from "../components/LoadingSpinner";
import toast from "react-hot-toast";

function UploadPage() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const uploadProject = async () => {
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file);

  try {
    setLoading(true);

    toast.loading("Reviewing Project...", {
      id: "upload",
    });

    const response = await api.post("/upload", formData);

    setResult(response.data);

    toast.success(
      "Review Completed Successfully!",
      {
        id: "upload",
      }
    );

  } catch (error) {

    console.error(error);

    toast.error(
      "Upload Failed",
      {
        id: "upload",
      }
    );

  } finally {

    setLoading(false);

  }
};

  return (
    <div className="container py-5">
      <div className="row g-4">
        <div
          style={{
            maxWidth: "600px",
            margin: "auto",
            textAlign: "center",
          }}
        >
          <h1 style={{ lineHeight: "54px" }}>
            AI Software Engineering Reviewer
          </h1>

          <p>Upload your project ZIP file for AI review.</p>

          <input
            className="form-control"
            type="file"
            accept=".zip"
            onChange={(e) => setFile(e.target.files[0])}
          />

          <br />
          <br />

          <button
            className="btn btn-primary mt-3"
            disabled={!file || loading}
            onClick={uploadProject}
          >
            {loading ? "Reviewing..." : "Upload Project"}
          </button>
          {loading && <LoadingSpinner />}

          {file && (
            <p>
              Selected: <b>{file.name}</b>
            </p>
          )}

          {result && (
            <>
              <hr className="my-5" />

              <h2 className="mb-4">Review Dashboard</h2>

              <div className="row g-4">
                <div className="col-md-6">
                  <ScoreCard score={result.score.overall_score} />
                </div>

                <div className="col-md-6">
                  <TechnologyCard technologies={result.technologies} />
                </div>

                <div className="col-md-6">
                  <StructureCard structure={result.structure} />
                </div>

                <div className="col-md-6">
                  <SecurityCard security={result.security} />
                </div>

                <div className="col-md-6">
                  <QualityCard quality={result.quality} />
                </div>

                <div className="col-md-6">
                  <PerformanceCard performance={result.performance} />
                </div>

                <div className="col-12">
                  <ArchitectureCard architecture={result.architecture} />
                </div>
              </div>

              <div className="mt-4">
                <button
                  className="btn btn-success"
                  onClick={() =>
                    window.open(
                      "http://127.0.0.1:8000/download-report",
                      "_blank",
                    )
                  }
                >
                  Download PDF
                </button>
                <AnalyticsChart result={result} />
                <AIReviewCard review={result.ai_review} />
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default UploadPage;
