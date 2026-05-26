import { useEffect, useState } from "react";
import axios from "axios";

function ReviewPage() {

  const [records, setRecords] = useState([]);

  const API_BASE =
    "https://breathe-esg-87pg.onrender.com";

  const fetchRecords = async () => {

    try {

      const response = await axios.get(
        `${API_BASE}/api/review/`
      );

      setRecords(response.data);

    } catch (error) {

      console.error("Error fetching records:", error);
    }
  };

  const handleAction = async (id, action) => {

    try {

      await axios.post(
        `${API_BASE}/api/review/${id}/`,
        {
          action: action
        }
      );

      fetchRecords();

    } catch (error) {

      console.error("Error updating record:", error);
    }
  };

  useEffect(() => {
    fetchRecords();
  }, []);

  return (
    <div style={{ padding: "20px" }}>

      <h2>Review Dashboard</h2>

      <table
        border="1"
        cellPadding="10"
        style={{
          borderCollapse: "collapse",
          width: "100%",
          marginTop: "20px"
        }}
      >

        <thead
          style={{
            backgroundColor: "#222",
            color: "white"
          }}
        >
          <tr>
            <th>ID</th>
            <th>Activity</th>
            <th>Value</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>

          {records.map((record) => (

            <tr
              key={record.id}
              style={{
                backgroundColor:
                  record.activity_value < 0
                    ? "#ffcccc"
                    : "white"
              }}
            >

              <td>{record.id}</td>

              <td>{record.activity_type}</td>

              <td>{record.activity_value}</td>

              <td
                style={{
                  color:
                    record.approved
                      ? "green"
                      : "orange",
                  fontWeight: "bold"
                }}
              >
                {record.approved
                  ? "Approved"
                  : "Pending"}
              </td>

              <td>

                <button
                  style={{
                    marginRight: "10px",
                    backgroundColor: "green",
                    color: "white",
                    border: "none",
                    padding: "8px 12px",
                    cursor: "pointer"
                  }}
                  onClick={() =>
                    handleAction(
                      record.id,
                      "approve"
                    )
                  }
                >
                  Approve
                </button>

                <button
                  style={{
                    backgroundColor: "red",
                    color: "white",
                    border: "none",
                    padding: "8px 12px",
                    cursor: "pointer"
                  }}
                  onClick={() =>
                    handleAction(
                      record.id,
                      "reject"
                    )
                  }
                >
                  Reject
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default ReviewPage;