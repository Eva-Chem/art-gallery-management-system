from lib.db import get_connection

class Artwork:
    @staticmethod
    def add_artwork(title, medium, year_created, price, artist_id, image_url=None):
        conn = get_connection()
        if conn is None:
            return
        
        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO artworks (title, medium, year_created, price, artist_id, image_url)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (title, medium, year_created, price, artist_id, image_url))
            
            conn.commit()
            print(f"✅ Artwork '{title}' added successfully!")
        except Exception as e:
            print("❌ Error adding artwork:", e)
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def view_all_artworks():
        conn = get_connection()
        if conn is None:
            return
        
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT a.id, a.title, a.medium, a.year_created, a.price, a.status, a.image_url, ar.name
                FROM artworks a
                JOIN artists ar ON a.artist_id = ar.id;
            """)
            
            artworks = cur.fetchall()
            if artworks:
                print("🎨 All Artworks:")
                for art in artworks:
                    print(art)
            else:
                print("⚠️ No artworks found.")
        except Exception as e:
            print("❌ Error fetching artworks:", e)
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def update_artwork(artwork_id, **kwargs):
        conn = get_connection()
        if conn is None:
            return

        try:
            cur = conn.cursor()
            fields = ", ".join([f"{key} = %s" for key in kwargs.keys()])
            values = list(kwargs.values())
            values.append(artwork_id)

            cur.execute(f"""
                UPDATE artworks
                SET {fields}
                WHERE id = %s;
            """, tuple(values))

            conn.commit()
            print(f"✅ Artwork ID {artwork_id} updated successfully!")
        except Exception as e:
            print("❌ Error updating artwork:", e)
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def delete_artwork(artwork_id):
        conn = get_connection()
        if conn is None:
            return

        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM artworks WHERE id = %s;", (artwork_id,))
            conn.commit()
            print(f"🗑️ Artwork ID {artwork_id} deleted successfully!")
        except Exception as e:
            print("❌ Error deleting artwork:", e)
        finally:
            cur.close()
            conn.close()
