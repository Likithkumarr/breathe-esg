import { useEffect, useState } from "react";
import axios from "axios";

function ReviewPage() {

  const [records, setRecords] = useState([]);

  const fetchRecords = async () => {

    const response = await axios.get(
      "http://127.0.0.1:8000/api/review/"
    );

    setRecords(response.data);
  };

  const handleAction = async (id, action) => {

    await axios.post(
      `http://127.0.0.1:8000/api/review/${id}/`,
      {
        action: action
      }
    );

    fetchRecords();
  };

  useEffect(() => {
    fetchRecords();
  }, []);

  return (
  <div>

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
                color: record.approved
                  ? "green"
                  : "red",
                fontWeight: "bold"
              }}
            >
              {record.approved ? "Approved" : "Pending"}
            </td>

            <td>

              <button
                onClick={() =>
                  handleAction(record.id, "approve")
                }
              >
                Approve
              </button>

              {" "}

              <button
                onClick={() =>
                  handleAction(record.id, "reject")
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