import { useState } from "react";
import axios from "axios";

function UploadPage() {

  const [file, setFile] = useState(null);
  const [sourceType, setSourceType] = useState("sap");

  const handleUpload = async () => {

    const formData = new FormData();

    formData.append("file", file);
    formData.append("source_type", sourceType);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/api/upload/",
        formData
      );

      alert(response.data.message);

    } catch (error) {

      console.error(error);
      alert("Upload failed");
    }
  };

  return (
    <div>

      <h2>Upload CSV</h2>

      <select
        value={sourceType}
        onChange={(e) => setSourceType(e.target.value)}
      >
        <option value="sap">SAP</option>
        <option value="utility">Utility</option>
        <option value="travel">Travel</option>
      </select>

      <br /><br />

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload}>
        Upload
      </button>

    </div>
  );
}

export default UploadPage;