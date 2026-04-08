from models.user import User
from functools import reduce

class Expense(User):

    def add_expense(self, user_id, amount, category, desc, date):
        query = "INSERT INTO expenses (user_id, amount, category, description, date) VALUES (%s,%s,%s,%s,%s)"
        self._User__cursor.execute(query, (user_id, amount, category, desc, date))
        self._User__conn.commit()

    def view_expenses(self, user_id):
        query = '''
        SELECT u.name, e.amount, e.category, e.description, e.date
        FROM users u
        JOIN expenses e ON u.user_id = e.user_id
        WHERE u.user_id = %s
        '''
        self._User__cursor.execute(query, (user_id,))
        return self._User__cursor.fetchall()
    
    def total_expense(self, data):
        if not data:
            return 0
        amounts = list(map(lambda x: x[1], data))
        return reduce(lambda a, b: a + b, amounts, 0)

    # 🔍 FILTER
    def filter_by_category(self, data, category):
        return [d for d in data if d[2].lower() == category.lower()]

    def filter_by_date(self, data, date):
        return list(filter(lambda d: str(d[4]) == date, data))

    # 📊 CATEGORY SUMMARY
    def category_summary(self, data):
        return {
            cat: sum(d[1] for d in data if d[2] == cat)
            for cat in set(d[2] for d in data)
        }

    # 📅 MONTHLY REPORT
    def monthly_report(self, data):
        report = {}
        for d in data:
            month = str(d[4])[:7]
            report[month] = report.get(month, 0) + d[1]
        return report

    # 🔥 HIGHEST EXPENSE
    def highest_expense(self, data):
        if not data:
            return None
        return reduce(lambda x, y: x if x[1] > y[1] else y, data)

    # 🧠 SMART INSIGHT
    def smart_insight(self, data):
        if not data:
            return "No data to analyze"
        summary = self.category_summary(data)
        max_cat = max(summary, key=summary.get)
        total = sum(summary.values())
        percent = (summary[max_cat] / total) * 100
        if percent > 50:
            return f"Critical: You are spending too much on {max_cat}"
        elif percent > 30:
            return f"Moderate: Spending high on {max_cat}"
        else:
            return f"Good: Spending is balanced"
    
    # 💰 BUDGET ALERT
    def budget_alert(self, data, limit=3000):
        total = self.total_expense(data)
        return "Budget Exceeded!" if total > limit else "Within Budget"

    # 🚀 NEW FEATURE (ADD HERE)
    def spending_level(self, data):
        total = self.total_expense(data)

        if total > 5000:
            return "High Spending"
        elif total > 2000:
            return "Moderate Spending"
        else:
            return "Low Spending"