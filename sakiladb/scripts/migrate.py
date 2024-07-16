import sqlite3


# Function to create a connection and cursor to the database
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn


# Function to insert data into the database
def insert_data(conn, rows, sql_insert_data, row_schema):
    try:
        for row in rows:
            print(dict(row))
            c = conn.cursor()
            c.execute(sql_insert_data, [row[schema] for schema in row_schema])
            conn.commit()
            print("Data inserted successfully")
    except sqlite3.Error as e:
        print(e)


# Function to fetch and display data from the database
def fetch_data(conn, sql_fetch_data):
    print(sql_fetch_data)
    try:
        c = conn.cursor()
        c.execute(sql_fetch_data)
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)


def migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data):
    # Fetch and display data
    rows = fetch_data(conn1, sql_fetch_data)

    # Insert some data
    insert_data(conn2, rows, sql_insert_data, row_schema)


def migrate_language(conn1, conn2):
    row_schema = ("language_id", "name", "last_update")
    sql_fetch_data = "SELECT language_id, name, last_update FROM language;"
    sql_insert_data = (
        "INSERT INTO film_language (id, name, last_update) VALUES (?, ?, ?);"
    )
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_country(conn1, conn2):
    row_schema = ("country_id", "country", "last_update")
    sql_fetch_data = "SELECT country_id,country, last_update FROM country;"
    sql_insert_data = (
        "INSERT INTO payment_country (id,country, last_update) VALUES (?, ?);"
    )
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_actor(conn1, conn2):
    row_schema = ("first_name", "last_name", "last_update")
    sql_fetch_data = "SELECT first_name,last_name, last_update FROM actor;"
    sql_insert_data = (
        "INSERT INTO actor_actor(first_name,last_name,last_update) VALUES (?, ?, ?);"
    )
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_category(conn1, conn2):
    row_schema = ("category_id", "name", "last_update")
    sql_fetch_data = "SELECT category_id, name, last_update FROM category;"
    sql_insert_data = (
        "INSERT INTO actor_category (id, name, last_update) VALUES (?, ?, ?);"
    )
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_film(conn1, conn2):
    row_schema = (
        "film_id",
        "title",
        "description",
        "release_year",
        "rental_duration",
        "rental_rate",
        "length",
        "replacement_cost",
        "rating",
        "special_features",
        "last_update",
        
    )
    sql_fetch_data = "SELECT film_id, title, description, release_year, rental_duration, rental_rate, length, replacement_cost, rating,special_features, last_update FROM film;"
    sql_insert_data = "INSERT INTO film_film(id, title, description, release_year, rental_duration, rental_rate, length, replacement_cost, rating,special_features, last_update,is_featured) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?);"
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_filmactor(conn1, conn2):
    row_schema = ("film_id", "actor_id", "last_update")
    sql_fetch_data = "SELECT actor_id, film_id, last_update FROM film_actor;"
    sql_insert_data = (
        "INSERT INTO film_filmactor(film_id, actor_id, last_update) VALUES (?, ?, ?);"
    )
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_filmcategory(conn1, conn2):
    row_schema = ("film_id", "category_id", "last_update")
    sql_fetch_data = "SELECT category_id,film_id,last_update FROM film_category;"
    sql_insert_data = "INSERT INTO film_filmcategory(film_id,category_id,last_update) VALUES (?, ?, ?);"
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_filmtext(conn1, conn2):
    row_schema = (
        "film_id",
        "title",
        "description",
    )
    sql_fetch_data = "SELECT film_id,title,description FROM film_text;"
    sql_insert_data = (
        "INSERT INTO film_filmtext(film_id,title,description) VALUES (?, ?, ?);"
    )
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_address(conn1, conn2):
    row_schema = (
        "address_id",
        "address",
        "address2",
        "district",
        "postal_code",
        "phone",
        "city_id",
        "last_update",
    )
    sql_fetch_data = "SELECT address_id, address, address2, district, postal_code, phone, city_id, last_update FROM address;"
    sql_insert_data = "INSERT INTO payment_address(id, address, address2, district, postal_code, phone, city_id, last_update) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_city(conn1, conn2):
    row_schema = (
        "city_id",
        "city",
        "country_id",
        "last_update",
    )  # Include city in the schema
    sql_fetch_data = "SELECT city_id, city, country_id, last_update FROM city;"  # Include city in the fetch query
    sql_insert_data = "INSERT INTO payment_city(id, name, country_id, last_update) VALUES (?, ?, ?, ?);"  # Ensure the insert matches the fetched data
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_country(conn1, conn2):
    row_schema = ("country_id", "country", "last_update")
    sql_fetch_data = "SELECT country_id,country,last_update FROM country;"
    sql_insert_data = (
        "INSERT INTO payment_country(id,name,last_update) VALUES (?, ?, ?);"
    )
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_customer(conn1, conn2):
    row_schema = (
        "first_name",
        "last_name",
        "email",
        "active",
        "create_date",
        "address_id",
        "store_id",
        "last_update",
    )
    sql_fetch_data = "SELECT first_name,last_name,email,active,create_date,address_id,store_id,last_update FROM customer;"
    sql_insert_data = "INSERT INTO payment_customer(first_name,last_name,email,active,create_date,address_id,store_id,last_update) VALUES (?, ?, ?, ?, ?, ? , ?, ?);"
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


def migrate_inventory(conn1, conn2):
    row_schema = ("film_id", "store_id", "last_update")
    sql_fetch_data = "SELECT film_id,store_id,last_update FROM inventory;"
    sql_insert_data = (
        "INSERT INTO payment_inventory(film_id,store_id,last_update) VALUES (?, ?, ?);"
    )
    migrate(conn1, conn2, row_schema, sql_fetch_data, sql_insert_data)


# Main function to demonstrate usage
def main():
    source_db = "../sakila_master.db"
    destination_db = "../db.sqlite3"
    conn1 = create_connection(source_db)
    conn2 = create_connection(destination_db)
    if conn1 is not None and conn2 is not None:
        # migrate_language(conn1, conn2)
        # migrate_country(conn1, conn2)
        # migrate_actor(conn1, conn2)
        # migrate_category(conn1,conn2)
        # migrate_filmcategory(conn1, conn2)
        migrate_film(conn1, conn2)
        # migrate_filmactor(conn1, conn2)
        # migrate_filmtext(conn1,conn2)     
        # migrate_address(conn1, conn2)
        # migrate_city(conn1, conn2)
        # migrate_country(conn1,conn2)
        # migrate_inventory(conn1,conn2)
        # migrate_customer(conn1,conn2)
        # conn1.close()
        conn2.close()
    else:
        print("Error! Cannot create the database connection.")


if __name__ == "__main__":
    main()
