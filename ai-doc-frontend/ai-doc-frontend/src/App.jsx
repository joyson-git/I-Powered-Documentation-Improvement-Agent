import { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeUrl = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8005/analyze/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });
      const data = await response.json();
      if (data.error) {
        setResult({ error: data.error });
      } else {
        setResult(data.analysis);
      }
    } catch (error) {
      setResult({ error: "Error connecting to backend." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1>AI-Powered Documentation Review</h1>
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter documentation URL"
        style={{
          width: "300px",
          marginRight: "1rem",
          padding: "0.5rem",
          fontSize: "1rem",
        }}
      />
      <button onClick={analyzeUrl} disabled={loading} style={{ padding: "0.5rem 1rem" }}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      <div style={{ marginTop: "2rem", whiteSpace: "pre-wrap" }}>
  <strong>Result:</strong>

  {result ? (
    typeof result === "string" ? (
      // If result is just a string message
      <p style={{ marginTop: "1rem" }}>{result}</p>
    ) : result.error ? (
      // If result has an error field
      <p style={{ color: "red", marginTop: "1rem" }}>Error: {result.error}</p>
    ) : (
      // Otherwise, result is an object - display it point-wise
      <div style={{ marginTop: "1rem" }}>
        {Object.entries(result).map(([key, value], index) => (
          <p key={index} style={{ marginBottom: "1.5rem" }}>
            <strong>{index + 1}. {key.charAt(0).toUpperCase() + key.slice(1)}:</strong> {String(value)}
          </p>
        ))}
      </div>
    )
  ) : (
    <p style={{ marginTop: "1rem" }}>No result yet.</p>
  )}
</div>
    </div>
  );
}

export default App;
