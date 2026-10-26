from flask import Flask, abort
app = Flask(__name__)

@app.route("/")
def home():
    return "Головна сторінка сервера Flask."

@app.route("/about")
def about():
    return "Інформація про автора."

@app.route("/skills")
def skills():
    return "Список навичок."

@app.route("/contact")
def contact():
    return "Контактна інформація."

@app.route("/temperature/<int:t>")
def temperature(t):
    if t < 0:
        return "Мороз"
    elif t <= 20:
        return "Прохолодно"
    elif t < 30:
        return "Тепло"
    else:
        return "Спека"

@app.route("/math/<operation>/<int:a>/<int:b>")
def math(operation, a, b):
    if operation == "add":
        return str(a + b)
    elif operation == "sub":
        return str(a - b)
    elif operation == "mul":
        return str(a * b)
    elif operation == "div":
        return str(a / b)
    else:
        abort(404)

if __name__ == "__main__":
    app.run()
