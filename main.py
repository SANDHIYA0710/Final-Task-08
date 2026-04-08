from models.expense import Expense
from utils.display import display_expenses

exp = Expense()

# ✅ Safe integer input function
def get_int_input(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("❌ Enter a valid number!")

# ✅ Safe float input function
def get_float_input(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("❌ Enter a valid amount!")

data = []  # to store fetched data

while True:
    print("\n📊 Smart Expense Manager")
    print("1️⃣ Add User")
    print("2️⃣ Add Expense")
    print("3️⃣ View Expenses")
    print("4️⃣ Total Expense")
    print("5️⃣ Exit")

    ch = get_int_input("Enter choice: ")

    # 🔹 Add User
    if ch == 1:
        name = input("Enter name: ")
        exp.create_user(name)

    # 🔹 Add Expense
    elif ch == 2:
        uid = get_int_input("User ID: ")
        amt = get_float_input("Amount: ")
        cat = input("Category: ")
        desc = input("Description: ")
        date = input("Date (YYYY-MM-DD): ")

        exp.add_expense(uid, amt, cat, desc, date)

    # 🔹 View Expenses
    elif ch == 3:
        uid = get_int_input("User ID: ")
        data = exp.view_expenses(uid)
        display_expenses(data)

    # 🔹 Total Expense
    elif ch == 4:
        if data:
            print("💰 Total:", exp.total_expense(data))
        else:
            print("⚠️ Please view expenses first!")

    # 🔹 Exit
    elif ch == 5:
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid choice! Please select 1–5.")