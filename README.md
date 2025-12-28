![CI](https://github.com/LucasNguyen2k/api-test-automation-lucasng/actions/workflows/python-ci.yml/badge.svg)

# API Test Automation (Python + PyTest)

This project demonstrates a clean, scalable Python API test automation framework using **PyTest** and **GitHub Actions CI**.

It is designed to reflect real-world testing practices, including:
- Clean project structure (`src` layout)
- Positive and negative API tests
- Parametrized test cases
- Continuous Integration (CI)

---

## 🔧 Tech Stack

- Python 3
- PyTest
- Requests
- GitHub Actions (CI)

---

## 📁 Project Structure

api-test-automation/
├── src/
│ ├── init.py
│ └── client.py
├── tests/
│ └── test_posts.py
├── .github/
│ └── workflows/
│ └── python-ci.yml
├── pytest.ini
└── README.md


---

## 🌐 API Under Test

This project uses the public test API:
https://jsonplaceholder.typicode.com

Example endpoint:
GET /posts/{id}

---

## ▶️ How to Run Tests Locally

### 1️⃣ Install dependencies
```bash
pip install pytest requests
```

### 2️⃣ Run tests
```bash
py -m pytest
```

