# 🍋 Little Lemon Restaurant - Backend API

A **Django REST Framework (DRF)** backend API for the **Little Lemon Restaurant** project. This API enables customers to browse menu items as well as book a table at the restaurant. Managers can add, adjust or delete menu items, as well as browse all restaurant bookings. More features will be added to the API consecutively.

---

## 🚀 Features

- **Customer Features**:
  - Browse menu items
  - Reserve a table

- **Manager Features**:
  - Manage menu items
  - Browse customer bookings

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Django 4.x**
- **Django REST Framework**
- **Pipenv** to create a virtual environment
- **MySQL**

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/little-lemon-api.git
cd littlelemon
```

### 2. Install dependencies
```bash
pipenv shell
pipenv install
```

### 3. Apply migrations & create superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run the server
```bash
python manage.py runserver
```

## 🔑 API Endpoints (Not the full list, TBD)

| Endpoint                  | Method | Description                     |
|---------------------------|--------|---------------------------------|
| `/restaurant/menu-items/`       | GET    | List menu items               |
| `/restaurant/menu-items/`       | POST   | Add item             |
| `/restaurant/menu-items/{id}/`      | PUT  | Adjust item         |
| `/restaurant/menu-items/{id}/`      | DELETE  | Delete item          |
| `/restaurant/booking`      | GET  | Get all bookings          |
| `/restaurant/booking`      | POST  | Add a new booking       |

---

## 📄 License
This project is licensed under the MIT License.

---
