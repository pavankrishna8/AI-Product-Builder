import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import NewRequirement from "./pages/NewRequirement";

function App() {
  return (
    <BrowserRouter>
      <nav style={{ display: "flex", gap: "1rem", padding: "1rem" }}>
        <Link to="/">Dashboard</Link>
        <Link to="/new">New Requirement</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/new" element={<NewRequirement />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;