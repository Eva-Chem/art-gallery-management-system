import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="art_gallery_db",
            user="eva",
            password="",  # leave empty if no password is set
            host="localhost",
            port="5432"
        )
        print("✅ Database connection successful!")
        return conn
    except Exception as e:
        print("❌ Database connection failed:", e)
        return None


# --- test connection when file is run directly ---
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT current_database();")
        db_name = cur.fetchone()[0]
        print(f"Connected to database: {db_name}")
        cur.close()
        conn.close()
