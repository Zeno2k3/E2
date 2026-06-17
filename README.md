# Chatbot Tuyển sinh Tiểu học (E2)

Đồ án tốt nghiệp (KLTN): chatbot hỏi-đáp tuyển sinh tiểu học dùng RAG, trả lời dựa trên tài liệu tuyển sinh thật (chống bịa). Có quản lý tài liệu cho admin và xác thực phân quyền.

## Kiến trúc

```
Next.js (chat / admin / auth)  ──JWT──>  FastAPI
                                            ├─ Auth (JWT + bcrypt)
                                            ├─ Documents (upload/quản lý)
                                            └─ RAG (LlamaIndex)
                                                 ├─ OpenAI LLM + embeddings
                                                 └─ FAISS vector store (disk)
                                          PostgreSQL (users, conversations, messages, documents)
```

- **Frontend**: Next.js 16 (App Router) + TypeScript + Tailwind v4 — `frontend/`
- **Backend**: FastAPI + LlamaIndex + PostgreSQL — `backend/`
- **DB local**: PostgreSQL qua `docker-compose.yml`

## Bắt đầu nhanh

```powershell
# 1. PostgreSQL
docker compose up -d db

# 2. Backend  (xem backend/README.md)
cd backend; python -m venv .venv; .venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env   # sửa OPENAI_API_KEY, JWT_SECRET
uvicorn app.main:app --reload --port 8000

# 3. Frontend
cd ../frontend; npm install; npm run dev
```

- Frontend: http://localhost:3000
- Backend API docs: http://localhost:8000/docs

## Lộ trình (milestones)
- **M0** Scaffolding + infra ✓
- **M1** DB models + Auth (JWT, phân quyền)
- **M2** Upload & quản lý tài liệu (admin)
- **M3** RAG ingestion bằng LlamaIndex (FAISS)
- **M4** Chat hỏi-đáp end-to-end (citations + lịch sử)
- **M5** Admin polish + roles
- **M6** Hardening + tests + docs

Chi tiết kế hoạch: xem tài liệu kế hoạch nội bộ.
