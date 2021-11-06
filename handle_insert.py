import mysql.connector

db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="pricechecker",
    )

print(db)
cursor = db.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)


def insert_sites(vals):
    query = "INSERT INTO pricefetcher_items (site, item_url, image_url, last_fetched_at, created_at, updated_at) VALUES (%s, %s, %s, %s,%s, %s)"
    cursor.executemany(query, vals)
    db.commit()
    print(cursor.rowcount, "record inserted.")



def insert_price_logs(vals):
    query = "INSERT INTO pricefetcher_fetch_logs (site, item_url, image_url, last_fetched_at, created_at, updated_at) VALUES (%s, %s, %s, %s,%s, %s)"
    cursor.executemany(query, vals)
    db.commit()
    print(cursor.rowcount, "record inserted.")


