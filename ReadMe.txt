# ** Simple Secure Bank Management System**

A Django-based web application for managing bank accounts, transactions, and users. This project provides functionalities for deposits, withdrawals, money transfers, and transaction history tracking, offering a simple and secure banking solution.

---

## **Table of Contents**
- [Introduction](#introduction)
- [Purpose](#Purpose)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)


---

## **File Structure **
simpleSecureBank
+---bankVenv
ª   +---Scripts
ª   ª   ª  activate (The file to activate the virtual environment)
+---base
ª   +---migrations (Database models created by Django)
ª   ª   ª   0001_initial.py
ª   ª   ª   0002_account_transactions_alter_customers_custid.py
ª   ª   ª   0003_rename_customers_customer_and_more.py
ª   ª   ª   0004_account_amount_transaction_trans_amount.py
ª   ª   ª   0005_alter_customer_custid.py
ª   ª   ª   0006_alter_customer_name.py
ª   ª   ª   0007_alter_customer_password.py
ª   ª   ª   0008_delete_transaction_account_name.py
ª   ª   ª   0009_remove_customer_created_remove_customer_custid.py
ª   ª   ª   0010_remove_customer_name_remove_customer_password.py
ª   ª   ª   0011_customer_name_customer_password.py
ª   ª   ª   0012_customer_created_customer_custid.py
ª   ª   ª   0013_transaction.py
ª   ª   ª   0014_alter_transaction_custid.py
ª   ª   ª   __init__.py
ª   ª   ª

ª   ª   admin.py
ª   ª   apps.py
ª   ª   forms.py
ª   ª   models.py
ª   ª   tests.py
ª   ª   urls.py (Links for all site)
ª   ª   views.py (main functions call)
ª   ª   __init__.py
+---patelbank
ª   ª   asgi.py
ª   ª   settings.py (Setting up the secure base)
ª   ª   test
ª   ª   urls.py
ª   ª   wsgi.py
ª   ª   __init__.py
+---templates (All HTML CSS and JS code to view the site)
ª   ª   default.html
ª   ª   home.html
ª   ª   login.html
ª   ª   signout.html
ª   ª   signup.html
ª   ª   zelle.html

ª   .gitattributes
ª   .gitignore
ª   bandit-report.html (the result of the bandit report conducted)
ª   bandit-report.txt
ª   db.sqlite3
ª   manage.py (the main file to run)
ª   ReadMe.txt
ª   Test.txt.txt
ª   tree.txt

---

## **Introduction**

The **Bank Management System** is a web-based application built using Django that simplifies banking operations. It is ideal for small-scale banking solutions or as a learning project for those interested in web development and database management using Python Django Framework. 

### **Purpose**
- Facilitate basic banking operations like deposits, withdrawals, and transfers.
- Provide transaction history for users.
- Secure user authentication and account management.

---

## **Technologies Used**
- **Backend**: Python, Django
- **Frontend**: Javascript, HTML, CSS, JavaScript
- **Database**: SQLite (default)
- **Authentication**: Django Authentication System

---

## **Features**
- User authentication and session management.
- View account balance.
- Deposit and withdraw funds.
- Transfer money to other registered users.
- View transaction history.
- Simple and responsive user interface.

---

## **Installation**

### **Prerequisites**
Ensure you have the following installed on your system:
- Python 3.8+
- Django 4.0+
- A database system like SQLite (default) or PostgreSQL

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bank-management-system.git
   cd bank-management-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the server:
   ```bash
   python manage.py runserver 8080
   ```

7. Access the application at `http://127.0.0.1:8080/`.

---

## **Usage**

1. **Admin Access**:
   - Log in as a superuser at `http://127.0.0.1:8080/value-admin/`.
   - Manage users, accounts, and transactions.

2. **User Operations**:
   - Sign up to create a new user.
   - Log in to view the dashboard.
   - Perform deposits, withdrawals, and transfers.
   - View transaction history.

3. **Transfer Money**:
   - Go to the transfer page.
   - Enter the recipient's name and the amount to transfer.
   - Confirm the transaction.

---

Security Improvements
- Created a better function to use stronger passwords for login (pre-used validators didnt work as they only work on DJANGO forms and this was HTML CSS forms).
- Changed the path for admin to value-admin for secure access
- Handled code to make it more clear from UI point of view.
- Made the webpage more secure from man in the middle attacks, XSS attacks, and http redirection.

---

Testing Process

Used bandit tool to understand what can be done better with security point of view. Tried using SonarQube but the installation process didnt happen correctly.

---

Contribution and References
-
