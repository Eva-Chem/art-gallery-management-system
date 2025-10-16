# lib/artists.py
import psycopg2
from lib.db import get_connection  # ✅ match the function name in db.py

class Artist:
    @staticmethod
    def add_artist(name, nationality, birth_year):
        conn = get_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO artists (name, nationality, birth_year)
                    VALUES (%s, %s, %s);
                """, (name, nationality, birth_year))
                conn.commit()
                print(f"✅ Artist '{name}' added successfully!")
            except Exception as e:
                print("❌ Error adding artist:", e)
            finally:
                cur.close()
                conn.close()

    @staticmethod
    def view_all_artists():
        conn = get_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT * FROM artists;")
                artists = cur.fetchall()
                print("🎨 All Artists:")
                for artist in artists:
                    print(artist)
            except Exception as e:
                print("❌ Error fetching artists:", e)
            finally:
                cur.close()
                conn.close()
