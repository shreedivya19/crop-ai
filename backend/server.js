const express = require('express');
const cors = require('cors');
const axios = require('axios');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

app.post('/predict', async (req, res) => {
  try {
    const mlResponse = await axios.post('http://localhost:5001/predict', req.body);
    res.json(mlResponse.data);
  } catch (error) {
    console.error('Error calling ML API:', error.message);
    res.status(500).json({ error: 'ML Prediction Service Unavailable' });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Backend server running on port ${PORT}`);
});
