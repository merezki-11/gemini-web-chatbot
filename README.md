# MacSolve AI Tutor — Gemini Web Chatbot

A full-stack AI tutor chatbot powered by Google Gemini 2.5 Flash. Built with a FastAPI backend and a modern React frontend, it teaches Machine Learning and AI concepts clearly using analogies and examples.

**Live Demo:** [macsolve-ai-tutor.vercel.app](https://macsolve-ai-tutor.vercel.app)

---

## Screenshots

### Welcome Screen (Offline — Backend Waking Up)
![Welcome Screen Offline](images/Screenshot_2026-03-28_164058.png)

### Welcome Screen (Online)
![Welcome Screen Online](images/Screenshot_2026-03-28_164128.png)

### Typing Animation
![Typing Animation](images/Screenshot_2026-03-28_164217.png)

### AI Response with Markdown
![AI Response](images/Screenshot_2026-03-28_164247.png)

### Full Detailed Explanation
![Detailed Explanation](images/Screenshot_2026-03-28_164329.png)

---

## Features

- Conversational AI powered by Google Gemini 2.5 Flash
- Markdown rendering for clean, formatted AI responses (bold, code, lists)
- Session persistence via `localStorage` — conversation survives page refresh
- Health check indicator showing backend status (Online/Offline)
- "Clear Conversation" button wired to the backend DELETE endpoint
- Friendly "Tutor is waking up..." message handling Render's free tier cold starts
- Fully responsive — works on mobile and desktop

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React, TypeScript, Tailwind CSS, Vite |
| Backend | FastAPI, Python |
| LLM | Google Gemini 2.5 Flash |
| Frontend Hosting | Vercel |
| Backend Hosting | Render |
| Version Control | Git + GitHub |

---

## Architecture

```
User → React Frontend (Vercel)
           ↓ POST /chat
      FastAPI Backend (Render)
           ↓
      Gemini 2.5 Flash API
           ↓
      Response → Frontend → Rendered Markdown
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check — confirms API is running |
| `POST` | `/chat` | Send a message and receive an AI response |
| `DELETE` | `/session/{session_id}` | Clear conversation history for a session |

### POST /chat — Request Body
```json
{
  "session_id": "unique-uuid-string",
  "message": "What is overfitting?"
}
```

### POST /chat — Response
```json
{
  "reply": "Overfitting happens when your model learns the training data too well..."
}
```

---

## Running Locally

### Backend

```bash
git clone https://github.com/merezki-11/gemini-web-chatbot.git
cd gemini-web-chatbot
pip install -r requirements.txt
```

Create a `.env` file in the root:
```
GEMINI_API_KEY=your_api_key_here
```

Start the server:
```bash
uvicorn main:app --reload
```

API will be available at `http://127.0.0.1:8000`
Interactive docs at `http://127.0.0.1:8000/docs`

### Frontend

The frontend lives in a separate repo: [macsolve-ai-buddy](https://github.com/merezki-11/macsolve-ai-buddy)

---

## Project Structure

```
gemini-web-chatbot/
│
├── main.py              # FastAPI app — all routes and Gemini integration
├── requirements.txt     # Python dependencies
├── .gitignore           # Excluded files
├── images/              # App screenshots
└── README.md            # Project documentation
```

---

## Related Projects

- [gemini-cli-chatbot](https://github.com/merezki-11/gemini-cli-chatbot) — Phase 1: CLI version of this chatbot
- [macsolve-ai-buddy](https://github.com/merezki-11/macsolve-ai-buddy) — Frontend repo (React/TypeScript)

---

## Author

**Macnelson Chibuike**
- GitHub: [@merezki-11](https://github.com/merezki-11)
- LinkedIn: [Macnelson Chibuike](https://www.linkedin.com/in/macnelson-chibuike)

---

## License

This project is open source and available under the [MIT License](LICENSE).