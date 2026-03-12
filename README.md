# 📚 Library Management System

A structured, menu-driven Library Management System built using Python.
This project demonstrates real-world project architecture using Object-Oriented Programming, JSON persistence, logging, virtual environments, and unit testing.

---

## 🚀 Features

* Add a book
* Remove a book
* Issue a book
* Return a book
* View all books
* Persistent storage using JSON
* Logging of system activities
* Unit testing using pytest
* Menu-driven CLI interface

---

## 🏗 Project Structure

```
library_system/
│
├── venv/                  # Virtual Environment (ignored in Git)
├── library/               # Core package
│   ├── __init__.py
│   ├── book.py
│   ├── user.py
│   ├── library.py
│   ├── storage.py
│   └── logger_config.py
│
├── data/
│   └── books.json
│
├── tests/
│   └── test_library.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧠 Concepts Covered

* Object-Oriented Programming (OOP)
* Classes and Objects
* Encapsulation
* Static methods
* File handling
* JSON serialization and deserialization
* Logging module
* Python package structure
* Virtual environments
* Unit testing with pytest
* CLI application design
* Separation of concerns

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone <your-repository-url>
cd library_system
```

---

### 2️⃣ Create and Activate Virtual Environment

#### Windows

```
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
venv\Scripts\activate
```

#### Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```
python main.py
```

You will see a menu-driven interface where you can manage books interactively.

---

### 5️⃣ Run Unit Tests

```
python -m pytest
```

---

## 🗂 Data Storage

All book data is stored in:

```
data/books.json
```

Data is automatically loaded at startup and saved after every operation.

---

## 📝 Logging

System activities are recorded in:

```
library.log
```

Logged operations include:

* Adding a book
* Removing a book
* Issuing a book
* Returning a book

---

## 🧪 Testing

Unit tests are written using pytest and located in the `tests/` folder.

The test suite validates core library operations such as:

* Adding books
* Issuing books
* Business logic functionality

---

## 🎓 Learning Outcomes

This project helps students understand:

* How real Python projects are structured
* How packages and imports work
* How to manage dependencies with virtual environments
* How to persist data using JSON
* How logging works in production systems
* How to write and execute unit tests
* How to design a modular and maintainable application

---

## 🔮 Future Improvements

* User authentication system
* Due date tracking and fine calculation
* Database integration (MySQL/PostgreSQL)
* REST API using Flask
* Role-based access (Admin/User)
* Docker containerization
* CI/CD integration

---

## 📌 Ideal For

* Python beginners
* Academic mini projects
* Resume projects
* Understanding backend fundamentals
* Learning clean architecture practices

---

## 📜 License

This project is open-source and intended for educational purposes.
