from flask import Flask,render_template

# flask instance

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Bett"

@app.route("/home")
def home():
    return "Hello Lynne"

# products render a products.html file
@app.route("/products")
def products():
    return render_template("products.html")

# dashboard and render
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/sales")
def sales():
    return render_template("sales.html")

@app.route("/index")
def index():
    return render_template("index.html")

app.run(debug=True)