const express = require("express");
const axios = require("axios");
const cors = require("cors");
const path = require("path");

const app = express();

app.use(cors());
app.use(express.json());

const FRONTEND_PATH = path.join(__dirname, "chat");

app.use(express.static(FRONTEND_PATH));

app.get("/", (req, res) => {
    res.sendFile(path.join(FRONTEND_PATH, "index.html"));
});

app.post("/chat", async (req, res) => {
    try {
        const response = await axios.post("http://localhost:8000/chat", {
            query: req.body.message
        });

        res.json(response.data);

  } catch (err) {

    console.log("FULL ERROR:");
    console.log(err.response?.data || err.message);

    res.status(500).json({
        error: err.response?.data || err.message
    });
}
});

app.listen(3000, () => {
    console.log("===== Node server running on PORT 3000 ====");
});