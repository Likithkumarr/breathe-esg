import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import UploadPage from "./pages/UploadPage";
import ReviewPage from "./pages/ReviewPage";

function App() {
  return (
    <BrowserRouter>

      <div style={{ padding: "20px" }}>
        <h1>Breathe ESG Dashboard</h1>

        <nav style={{ marginBottom: "20px" }}>
          <Link to="/">Upload</Link> |{" "}
          <Link to="/review">Review</Link>
        </nav>

        <Routes>
          <Route path="/" element={<UploadPage />} />
          <Route path="/review" element={<ReviewPage />} />
        </Routes>
      </div>

    </BrowserRouter>
  );
}

export default App;