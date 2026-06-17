# Admissions Chatbot — Backend (FastAPI + LlamaIndex)

RAG chatbot tuyển sinh tiểu học. Backend cung cấp API xác thực, quản lý tài liệu, và hỏi-đáp RAG.

## Stack
- FastAPI + Uvicorn
- PostgreSQL (SQLAlchemy 2.0 + Alembic)
- LlamaIndex (OpenAI LLM + embeddings, FAISS vector store)
- JWT auth (python-jose + passlib/bcrypt)

## Yêu cầu
- Python 3.11+
- Docker (chạy PostgreSQL local)
- OpenAI API key

## Cài đặt & chạy (Windows PowerShell)

```powershell
# 1. Bật PostgreSQL (từ thư mục gốc repo)
docker compose up -d db

# 2. Tạo venv + cài deps
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 3. Cấu hình môi trường
Copy-Item .env.example .env   # rồi sửa OPENAI_API_KEY, JWT_SECRET

# 4. Chạy migration (sau khi có models — M1)
alembic upgrade head

# 5. Tạo admin đầu tiên (M1)
python -m app.scripts.seed_admin

# 6. Chạy server
uvicorn app.main:app --reload --port 8000
```

- API docs (Swagger): http://localhost:8000/docs
- Health check: http://localhost:8000/health

## Cấu trúc

```
app/
├── main.py          # FastAPI app, CORS, đăng ký router, load index lúc startup
├── core/            # config, security (JWT/hash), deps (auth)
├── db/              # SQLAlchemy engine/session, Base
├── models/          # ORM: user, conversation, message, document
├── schemas/         # Pydantic request/response
├── routers/         # auth, chat, documents, admin
├── services/        # business logic
├── rag/             # luồng RAG bằng LlamaIndex (settings, vector_store, index, ingest, retriever, prompts)
└── scripts/         # seed_admin, rebuild_index
```

## Ghi chú
- Mọi call OpenAI đi qua backend — không lộ key ra frontend.
- FAISS index + LlamaIndex docstore lưu ở `data/faiss`; file gốc ở `data/uploads` (nguồn rebuild).
