import React, { useState } from 'react';

function CropForm() {
  const [form, setForm] = useState({
    N: '',
    P: '',
    K: '',
    pH: '',
    temperature: '',
    humidity: '',
    rainfall: ''
  });
  const [result, setResult] = useState(null);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      });
      const data = await res.json();
      setResult(data.recommended_crop);
    } catch (error) {
      console.error('Error fetching prediction:', error);
      setResult('Error fetching prediction');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {Object.keys(form).map(key => (
        <input
          key={key}
          type="number"
          name={key}
          placeholder={key}
          value={form[key]}
          onChange={handleChange}
          step="any"
          required
        />
      ))}
      <button type="submit">Get Recommendation</button>
      {result && <p><strong>Recommended Crop:</strong> {result}</p>}
    </form>
  );
}

export default CropForm;
