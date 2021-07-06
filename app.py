from flask import Flask, render_template

#  создание экземпляра сервера
app = Flask(__name__)

# Проверака переменной __name__
# print(__name__)

# Оснойной код -  Основная логика сервера
@app.route("/")
def index_page():
    # return "Hello, browser! I am Flask server!"
    # возврат страницы
    return render_template("index.html")

@app.route("/product")
def product_page():
    return render_template("product.html")

# точка входа
if __name__ == "__main__":
    app.run(debug=True)