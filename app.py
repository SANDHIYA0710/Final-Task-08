from flask import Flask, render_template, request, redirect
from models.expense import Expense

app = Flask(__name__)
exp = Expense()

# 🏠 HOME PAGE
@app.route('/')
def home():
    users = exp.get_users()
    return render_template('index.html', users=users)


# ➕ ADD USER
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    if name:
        exp.create_user(name)
    return redirect('/')


# ➕ ADD EXPENSE
@app.route('/add_expense', methods=['POST'])
def add_expense():
    try:
        user_id = int(request.form.get('user_id'))
        amount = float(request.form.get('amount'))
    except:
        return "Invalid input"

    category = request.form.get('category')
    desc = request.form.get('description')
    date = request.form.get('date')

    exp.add_expense(user_id, amount, category, desc, date)
    return redirect('/')


# 📊 DASHBOARD
@app.route('/dashboard/<int:user_id>')
def dashboard(user_id):
    data = exp.view_expenses(user_id)

    # 🔍 FILTER
    category = request.args.get('category')
    date = request.args.get('date')

    if category:
        data = exp.filter_by_category(data, category)
    if date:
        data = exp.filter_by_date(data, date)

    # 📊 ANALYSIS
    summary = exp.category_summary(data)
    monthly = exp.monthly_report(data)

    # 🔥 SAFE HIGHEST EXPENSE (NO ERROR)
    highest = exp.highest_expense(data)
    if highest is None:
        highest = ("No Data", 0, "-", "-", "-")

    # 🧠 OTHER FEATURES
    insight = exp.smart_insight(data)
    alert = exp.budget_alert(data)
    level = exp.spending_level(data)

    # 📤 SEND TO HTML
    return render_template(
        'dashboard.html',
        summary=summary,
        monthly=monthly,
        highest=highest,
        insight=insight,
        alert=alert,
        level=level
    )


# ▶️ RUN APP
if __name__ == "__main__":
    app.run(debug=True)