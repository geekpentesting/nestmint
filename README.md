# 💸 NestMint

**NestMint** is a clean, beginner-friendly financial planning tool that helps families plan for:

- 🎓 Children’s education
- 🏖️ Passive income during retirement

Designed with safe investment assumptions like SIPs and post office schemes, NestMint focuses on **realistic planning** and **ease of use**.

---

## 🚀 Features

- Set your **current and retirement age**
- Specify **monthly passive income** needed after retirement
- Plan for **multiple children’s education**
- Optional **5% education cost inflation**
- Assumes **7% annual return** from safe investment options
- Outputs:
  - Per-child SIP breakdown
  - Retirement corpus & SIP
  - Total required SIP monthly
- Download education plan as Excel
- **Powered by FastAPI + Streamlit**

---

## 📁 Project Structure

```
nestmint/
├── api/
│   └── main.py           # FastAPI backend logic
├── streamlit_app.py      # Streamlit frontend interface
├── requirements.txt      # Python package requirements
└── README.md             # Project documentation
```

---

## 💻 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start FastAPI Backend

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

### 3. Launch Streamlit Frontend (port 9001)

```bash
streamlit run streamlit_app.py --server.port 9001
```

---

## 🔗 Access App

Go to: [http://localhost:9001](http://localhost:9001)

---

## 📊 Outputs

- Per-child SIP plan (based on age, goal, inflation)
- Monthly SIP for retirement
- Total monthly SIP required

---

## 🛡️ Assumptions

- Education goal is at age 18
- Retirement income lasts until age 55
- Investment return: **7% annually**
- Optional 5% inflation on education goals

---

## 👥 Ideal For

- Working professionals with kids
- Early retirement planners
- Anyone wanting a real, understandable financial plan

---
