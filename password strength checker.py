from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)


def check_password_strength(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\];']", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")

    result = check_password_strength(password)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)