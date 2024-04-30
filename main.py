from flask import Flask,render_template,request,redirect,url_for,flash
from database import get_data,insert_products,insert_sales


# flask instance

app = Flask(__name__)
app.secret_key = "betika"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

# products render a products.html file
@app.route("/products")
def products():
    products = get_data("products")
    return render_template("products.html",prods=products)

# adding products
@app.route("/add_products", methods=["GET","POST"])
def add_prods():
    p_name = request.form["products_name"]
    b_price = request.form["Buying_Price"]
    s_price = request.form["Selling_Price"]
    s_quantity = request.form["Stock_Quantity"]

    new = (p_name,b_price,s_price,s_quantity)
    insert_products(new)
    flash(f"{s_quantity},{p_name}added succesfully")

    return redirect(url_for("products"))
# dashboard and render
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/sales")
def sales():
    sales = get_data("sales")
    products = get_data("products")
    return render_template("sales.html",sales=sales,prods=products)

# making sales
@app.route("/make_sales", methods=["POST","GET"])
def make_sales():
    # get form data
    pid = request.form["pid"]
    quantity = request.form["Stock_Quantity"]
    new_sales = (pid,quantity)
    
    insert_sales(new_sales)
    return redirect(url_for("sales"))

app.run(debug=True)