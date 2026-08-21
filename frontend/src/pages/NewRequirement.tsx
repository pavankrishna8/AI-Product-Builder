import { useState } from "react";
import axios from "axios";

export default function NewRequirement() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [result, setResult] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8000/requirements", {
        title,
        description,
      });
      setResult(res.data.message);
    } catch {
      setResult("Something went wrong submitting the requirement.");
    }
  };

  return (
    <div>
      <h1>New Requirement</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title: </label>
          <input value={title} onChange={(e) => setTitle(e.target.value)} />
        </div>
        <div>
          <label>Description: </label>
          <textarea value={description} onChange={(e) => setDescription(e.target.value)} />
        </div>
        <button type="submit">Submit</button>
      </form>
      {result && <p>{result}</p>}
    </div>
  );
}