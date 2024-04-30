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

# get_data("products")
get_data("sales")

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
insert_products(product_value)

# get_data('products')
# get_data('sales') 

# create a function to insert sales (2 ways)

def insert_sales(values):
    insert = f"insert into sales(pid,quantity,created_at)values{values}"
    sal.execute(insert)
    conn.commit()
sales_value = (1,20,"now()")
insert_sales(sales_value)

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
get_data('sales')