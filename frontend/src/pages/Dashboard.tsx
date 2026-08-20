import { useEffect, useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [status, setStatus] = useState("checking...");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/health")
      .then((res) => setStatus(res.data.status))
      .catch(() => setStatus("backend unreachable"));
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Backend status: {status}</p>
      <p>Your submitted requirements will appear here.</p>
    </div>
  );
}