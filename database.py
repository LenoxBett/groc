import psycopg2

# connecting to the postgresql database
conn = psycopg2.connect( 
    dbname = "myduka",
    user = "postgres",
    password = "5555",
    host = "localhost",
    port = 5432,
)
# open a cursor to perform database operation

cur = conn.cursor()

def get_products():  
    prods = cur.execute("select * from products;")
    prods = cur.fetchall()  
    return prods  
    # print(prods)
    # for i in prods:
    #     print(i) 
# prods = get_products()
# print(prods)

sal = conn.cursor()

def get_sales():
    sales = sal.execute("select * from sales;")
    sales = sal.fetchall()
    # for i in sales:
    #     print(i)
        

# get_sales()
  
def get_data(table):
    select = f"select * from {table}"
    cur.execute(select)
    data = cur.fetchall()
    return data

get_data("products")
# get_data("sales")

# function to insert products
        
# def insert_products(values):
#     insert = f"insert into products(name,selling_
#     price,buying_price
#     ,stock_quantity)values{values}"
#     cur.execute(insert)
#     conn.commit()
# product_value = ("milk",50,20,3)
# insert_products(product_value)

# get_data('products')
# get_data('sales')


def insert_products(values):
    insert = """insert into products(name,selling_price,
    buying_price
    ,stock_quantity)values(%s,%s,%s,%s)"""
    cur.execute(insert,values)
    conn.commit()
product_value = ("cookies",50,20,3)
# insert_products(product_value)

# get_data('products')
# get_data('sales') 

# create a function to insert sales (2 ways)

def insert_sales(values):
    insert = f"insert into sales(pid,quantity,created_at)values{values}"
    sal.execute(insert)
    conn.commit()
sales_value = (1,20,"now()")
# insert_sales(sales_value)

# get_data('products')
# get_data('sales') 

def insert_sales(values):
    insert = """insert into sales(pid,quantity,created_at
    )values(%s,%s,now())"""
    cur.execute(insert,values)
    conn.commit()
# sales_value = (1,90,"now()")
# insert_sales(sales_value)

# get_data('products')
# get_data('sales')

# profit function
def prof_per_prod():
    query = f"SELECT products.name, sum((selling_price - buying_price) * sales.quantity) AS profit FROM products JOIN sales ON products.id = sales.pid GROUP BY products.name;"
    cur.execute(query)
    data = cur.fetchall()
    return data

# prof = prof_per_prod()
# print(prof)
    

def profit_per_day():
    per_day = 'select DATE(created_at) as days,sum((selling_price-buying_price)*(quantity)) as profit from products join sales on sales.pid=products.id group by days;'
    cur.execute(per_day)
    data = cur.fetchall()
    return data
per_d = profit_per_day()
# print(per_d)

def sales_per_prod():
    sale = 'select name,sum(selling_price*quantity) as p_sales from sales join products on sales.pid = products.id group by name;'
    cur.execute(sale)
    data = cur.fetchall()
    return data
s_prod = sales_per_prod()
# print(s_prod)

def sales_per_day():
    sale = 'select DATE(created_at) as day,sum(selling_price*quantity) as d_sales from sales join products on sales.pid=products.id group by day;'
    cur.execute(sale)
    data = cur.fetchall()
    return data
s_day = sales_per_day()
print(s_day)


def insert_user(values):
    query = "insert into users(full_name,email,password) values(%s,%s,%s)"
    cur.execute(query,values)
    conn.commit()


def check_email(email):
    query = 'select * from users where email = %s'
    cur.execute(query,(email,))
    data = cur.fetchone()
    return data


# email and password

def check_email_pass(email,password):
    query = 'select * from users where email = %s and password = %s'
    cur.execute(query,(email,password,))
    data = cur.fetchall()
    return data