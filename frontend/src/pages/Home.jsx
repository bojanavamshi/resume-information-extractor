import { useState } from "react";
import { useNavigate } from "react-router-dom";
import UploadResume from "../components/UploadResume";
import Loading from "../components/Loading";
import ErrorMessage from "../components/ErrorMessage";
import { extractResume } from "../services/api";

function Home() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleUpload = async (file) => {
    if (!file) {
      setError("Please select a PDF or DOCX resume to continue.");
      return;
    }

    setIsLoading(true);
    setError("");

    try {
      // Call the backend API
      const response = await extractResume(file);

      // Print response in browser console (F12 -> Console)
      console.log("API Response:", response);

      // Navigate to Result page with extracted data
      navigate("/result", {
        state: {
          resumeData: response.data,
        },
      });
    } catch (err) {
      console.error("API Error:", err);

      setError(
        err.response?.data?.detail ||
          "We could not analyze your resume right now. Please try again."
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <section className="hero-section">
      <div className="hero-card glass-card">
        <div className="hero-copy">
          <p className="eyebrow">AI-powered resume intelligence</p>

          <h1>Extract key details from any resume in seconds.</h1>

          <p className="hero-text">
            Upload a PDF or DOCX file and instantly retrieve structured data
            for contact details, skills, experience, education, and more.
          </p>

          <ul className="feature-list">
            <li>Secure, fast upload workflow</li>
            <li>Professional result cards for every section</li>
            <li>Mobile-friendly experience</li>
          </ul>
        </div>

        <div className="hero-panel">
          <UploadResume
            onUpload={handleUpload}
            isLoading={isLoading}
            onError={setError}
          />

          {isLoading && <Loading />}

          {error && (
            <ErrorMessage
              message={error}
              onRetry={() => setError("")}
            />
          )}
        </div>
      </div>
    </section>
  );
}

export default Home;