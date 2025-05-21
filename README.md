# 🧠 RAG Chatbot LocalWisdom POC

This project is a **Retrieval-Augmented Generation (RAG) Chatbot Proof of Concept** using **GROQ API** for natural language processing and a local **Chroma vector database** for document retrieval. The system consists of a **Flask backend** and a **Streamlit frontend**, containerized with Docker for easy deployment.

---

## 📁 Project Structure

```
.
├── backend                  # Backend (Flask) with Chroma vector store
│   ├── app.py              # Main Flask app
│   ├── .env.example        # .env example
│   ├── chroma_db_poc_v2    # Chroma DB storage folder
│   ├── Dockerfile          # Backend Dockerfile
│   └── requirements.txt    # Backend Python dependencies
├── frontend                 # Frontend (Streamlit)
│   ├── .streamlit          # Streamlit UI config
│   ├── app.py              # Streamlit UI app
│   ├── Dockerfile          # Frontend Dockerfile
│   └── requirements.txt    # Frontend Python dependencies
├── docker-compose.yaml     # Docker Compose file to run full stack
└── README.md               # Project documentation
```

---

## ⚙️ Requirements

### 🧩 Environment Variables

#### 1. **Backend**

Create a `.env` file inside the `backend/` directory with the following content:

```
GROQ_API_KEY=your_groq_api_key_here
```

> Replace `your_groq_api_key_here` with your actual GROQ API key.

#### 2. **Host Machine**

You must set the following environment variable **on your host system** (not in `.env`):

```
TUNNEL_TOKEN=your_cloudflared_tunnel_token
```

> This is used to expose the frontend (or backend) to the internet via a secure Cloudflare tunnel.

---

## 🚀 Running the Project

Make sure Docker and Docker Compose are installed.

### 1. Build and Start the Containers

```bash
docker-compose up --build
```

This will spin up both:

* The **backend API** (Flask)
* The **frontend UI** (Streamlit)

Also the cloudflared tunnel will also up. This cloudflared will up based on the TUNNEL_TOKEN env.

### 2. Access the Chatbot

Once the containers are running, follow the logs for the public Cloudflare tunnel URL and open it in your browser to interact with the chatbot.

---

## 📌 Notes

* The Chroma vector DB is pre-initialized with demo content inside the `chroma_db_poc_v2/` folder.
* The chatbot uses GROQ API to generate responses based on the documents retrieved from the Chroma vector store.
* The model that used via GROQ API is llama-3.3-70b.
* This POC is designed for experimentation and internal use. Ensure your API keys and tokens are kept secure.