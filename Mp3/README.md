![1000015108](https://github.com/user-attachments/assets/d3bf42a2-3740-46ab-8280-8bc1617b1a7b)
<div align="center">
  <h1>💄 Cosmetics Online Store</h1>
  <p>An elegant and simple e-commerce web application for beauty & cosmetic products</p>
  <img src="https://img.shields.io/badge/Backend-Django-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-HTML/CSS-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Development-yellow?style=for-the-badge" />
</div>

---

## 🚀 Overview

The **Cosmetics Online Store** is a full-stack web application built with **Python/Django** on the backend and a pre-designed **HTML/CSS** template for the frontend. It provides essential features for a modern online shopping experience — including authentication, shopping cart, order placement, product management, and more.

This project was developed for educational purposes to strengthen backend development skills while implementing practical e-commerce features.

---

## ✨ Features

### 🧑‍💼 User-Side

- 🔐 User authentication (Sign up, Login, Logout)
- 🏠 Home page with real product prices and discounts
- 🔎 Fast product search bar
- 🛍️ Place and view orders
- 🛒 View personalized shopping cart (after login)
- ⚡ Fast and user-friendly interface

### 🛠 Admin Panel

- 📦 Add, edit, or delete products
- 📑 View all placed orders by users
- 🔧 Full control over store content via Django Admin

---

## 🧰 Tech Stack

| Layer         | Technology           |
|---------------|----------------------|
| Frontend      | Pre-built HTML/CSS Template |
| Backend       | Python, Django       |
| Database      | SQLite (easily upgradable) |
| Admin Panel   | Django Admin Interface |

---

## 🧪 Setup & Installation

```bash
# Clone the repository
git clone https://github.com/your-username/cosmetics-store.git
cd cosmetics-store

# Create a virtual environment
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
