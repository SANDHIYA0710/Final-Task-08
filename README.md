# Final-Task-08

 # Smart Expense Manager (Real-Time Project)

## Project Overview

Smart Expense Manager is a full-stack web application developed using Python, MySQL, and Flask.
The system allows users to track daily expenses, categorize spending, and analyze financial behavior through a dynamic dashboard.

The application not only performs CRUD operations but also provides analytical insights such as monthly reports, spending patterns, and budget monitoring.

---

## Key Features

### User Management

* Create and manage users
* View user list dynamically

### Expense Tracking

* Add daily expenses with amount, category, description, and date
* Store and retrieve expense data from MySQL database

### Data Analysis

* View expenses using SQL JOIN operations
* Filter expenses by category and date
* Calculate total expenses using functional programming techniques (`map`, `reduce`)
* Category-wise spending summary using dictionary comprehension
* Monthly expense aggregation

### Advanced Analytics

* Identify highest expense using `reduce`
* Generate smart insights based on spending patterns
* Classify spending level (Low, Moderate, High)
* Budget monitoring and alert system

### Dashboard

* Interactive dashboard built using Flask templates
* Visualization using Chart.js (doughnut chart)
* Displays:

  * Total expense
  * Highest expense
  * Category distribution
  * Monthly report
  * Smart insights
  * Spending level
  * Budget status

### Error Handling

* Handles empty dataset scenarios
* Prevents runtime errors during analysis
* Input validation for numeric fields

---

## Technologies Used

* Python
* Flask
* MySQL
* HTML, CSS
* Chart.js

---

## Concepts Implemented

### Object-Oriented Programming

* Encapsulation using private variables
* Inheritance (Expense class extends User class)
* Method overriding
* Modular design

### Functional Programming

* `map()` for transformation
* `filter()` for filtering data
* `reduce()` for aggregation
* List comprehension
* Dictionary comprehension

### Database Concepts

* Relational database design
* Foreign key constraints
* SQL JOIN operations

---

## Project Structure

```id="projtree"
expense_manager/
│
├── main.py
├── app.py
├── db_config.py
│
├── models/
│   ├── user.py
│   ├── expense.py
│
├── templates/
│   ├── index.html
│   ├── view.html
│   ├── dashboard.html
│
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```id="clonecmd"
git clone <your-repository-url>
cd expense_manager
```

### 2. Install Dependencies

```id="installcmd"
pip install flask
pip install mysql-connector-python
```

### 3. Database Setup

```id="dbsetup"
CREATE DATABASE expense_db;
USE expense_db;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

CREATE TABLE expenses (
    exp_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    amount FLOAT,
    category VARCHAR(50),
    description VARCHAR(100),
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

### 4. Configure Database

Update credentials in `db_config.py`:

```id="dbconfig"
password = "your_password"
```

---

## How to Run

```id="runapp"
python app.py
```

Open in browser:

```id="url"
http://127.0.0.1:5000
```

---

## Application Flow

1. Create a user
2. Add expense records
3. Navigate to dashboard
4. Apply filters (optional)
5. Analyze results through charts and insights

---

## Sample Output

* Displays categorized expense distribution
* Shows highest spending category
* Provides monthly spending breakdown
* Generates automated insights

---

## Future Enhancements

* User authentication system
* Export reports (PDF/Excel)
* Budget planning module
* Data visualization enhancements (line charts, bar charts)
* Deployment to cloud platforms

---

## Conclusion

This project demonstrates a practical implementation of backend development, database management, and data analysis using Python.
It integrates programming concepts with real-world financial tracking and provides meaningful insights through a structured dashboard.

---

