# placeMate

A full stack application integrated using AI models to generate placement questions for interview preparation. 

---

## 🐍 Backend Setup (FastAPI + SQLAlchemy)

### 1 Navigate to the backend directory
```bash
cd backend
```

### 2 Create the Enviroment File

```bash
python -m venv .venv
```

### 3 Activate the venv

```bash
source .venv/bin/activate
```

AND

```bash
.venv\Scripts\activate
```

### 4 Install Dependencies

```bash
pip install -r requirements.txt
```

### 5 Initialize the DB (if not , you can change db name from the `models` file

### 6 Start the FastAPI Server

```bash
uvicorn src.app:app --reload
```

## Frontend Setup (Vite)

Make sure you have Node.js in your system

## 1 Change to that directory for frontend

```bash
cd frontend
```

## 2 Install node dependencies

```bash
npm install
```

## 3 Start the server

```bash
npm run dev
```


# Make sure that you add all API keys and secrets in the `.env` file.

## Reference 

### Backend:

```bash
uvicorn src.app:app --reload – Start dev server
python src/database/models.py – Initialize DB tables
```


### Frontend:

```bash
npm run dev – Start frontend dev server
npm run build – Build production assets
npm run preview – Preview production build
```




