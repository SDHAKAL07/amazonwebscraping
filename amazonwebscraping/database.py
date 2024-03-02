import sqlite3

con = sqlite3.connect('amazon.db')
cur = con.cursor()

cur.execute("""
create table if not exists products(
    product_name text,
    product_price text,
    product_review text,
    product_type text,
    product_imagelink text
    )
    """)
con.commit()
con.close()


