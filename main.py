from flask import Flask,render_template,request,redirect,url_for,flash
from database import get_data,insert_products,insert_sales,prof_per_prod,profit_per_day,sales_per_day,sales_per_prod,insert_user


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
    s_price = request.form["Selling_Price"]
    b_price = request.form["Buying_Price"]
    s_quantity = request.form["Stock_Quantity"]

    new = (p_name,b_price,s_price,s_quantity)
    insert_products(new)
    flash(f"{s_quantity},{p_name}added succesfully")

    return redirect(url_for("products"))
# dashboard and render
@app.route("/dashboard")
def dashboard():
    p_product = prof_per_prod()
    p_day = profit_per_day()
    s_day = sales_per_day()
    s_prod  = sales_per_prod()
    # print(p_product)
    # print(p_day)
    # print(s_day)
    print(s_prod)
    p_name = []
    p_profit = []
    day = []
    d_profit = []
    sales_day = []
    sales_prod = []
    x = []
    y = []
    for i in p_product:
        p_name.append(i[0])
        p_profit.append(float(i[1]))
    
    for i in p_day:
        day.append(str(i[0]))
        d_profit.append(float(i[1]))

    for i in s_day:
        sales_day.append(str(i[0]))
        sales_prod.append(float(i[1]))

    for i in s_prod:
        x.append(i[0])
        y.append(float(i[1]))
    return render_template("dashboard.html",name=p_name,profit=p_profit,day = day,d_profit=d_profit,pro_name=x,pro_sales=y,sales_prod=sales_prod)


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

@app.route("/login")
def login():
    return render_template("login.html")

# register user
@app.route("/register", methods=["POST","GET"])
def register():
    # get form data
    if request.method == "POST":
        f_name = request.form["full_name"]
        email = request.form["email"]
        password = request.form["password"]
        # insert user
        new_user = (f_name,email,password)
        insert_user(new_user)
        return redirect(url_for("login"))
    return render_template("register.html")



app.run(debug=True)