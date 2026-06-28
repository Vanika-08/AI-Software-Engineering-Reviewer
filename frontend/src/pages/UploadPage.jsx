import { useState } from "react";
import api from "../services/api";

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

      const response = await api.post("/upload", formData);

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Upload Failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "600px",
        margin: "auto",
        textAlign: "center",
      }}
    >
      <h1 style={{ lineHeight: "54px" }}>AI Software Engineering Reviewer</h1>

      <p>Upload your project ZIP file for AI review.</p>

      <input
        type="file"
        accept=".zip"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button disabled={!file || loading} onClick={uploadProject}>
        {loading ? "Reviewing..." : "Upload Project"}
      </button>

      {file && (
        <p>
          Selected: <b>{file.name}</b>
        </p>
      )}

      {result && (
        <div style={{ marginTop: "30px" }}>
          <h2>Review Completed</h2>

          <p>
            <strong>Score:</strong> {result.score.overall_score}/100
          </p>

          <p>
            <strong>Frontend:</strong> {result.technologies.frontend}
          </p>

          <button
            onClick={() =>
              window.open("http://127.0.0.1:8000/download-report", "_blank")
            }
          >
            Download PDF
          </button>
        </div>
      )}
    </div>
  );
}

export default UploadPage;
