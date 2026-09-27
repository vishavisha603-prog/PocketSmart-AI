from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Get values from the form
    income = float(request.form.get("income", 0))
    food = float(request.form.get("food", 0))
    travel = float(request.form.get("travel", 0))
    shopping = float(request.form.get("shopping", 0))
    other = float(request.form.get("other", 0))

    # Calculate total expenses
    total_expense = food + travel + shopping + other

    # Calculate remaining balance
    balance = income - total_expense

    # Calculate savings percentage
    if income > 0:
        savings_percentage = (balance / income) * 100
    else:
        savings_percentage = 0

    # Generate recommendation
    if balance < 0:
        recommendation = (
            "Your expenses are higher than your income. "
            "Try reducing unnecessary expenses."
        )

    elif savings_percentage < 20:
        recommendation = (
            "Your savings are below 20%. "
            "Try to reduce shopping and other unnecessary expenses."
        )

    elif savings_percentage < 40:
        recommendation = (
            "Your budget is manageable. "
            "Try to save a little more for future needs."
        )

    else:
        recommendation = (
            "Good budgeting! You are maintaining a healthy savings level."
        )

    return render_template(
        "index.html",
        income=income,
        total_expense=total_expense,
        balance=balance,
        savings_percentage=round(savings_percentage, 2),
        recommendation=recommendation
    )


if __name__ == "__main__":
    app.run(debug=True)