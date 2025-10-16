from lib.db import get_connection

class Artwork:
    # 🟢 CREATE
    @staticmethod
    def add_artwork(title, medium, price, artist_id, status='available', image_url=None):
        conn = get_connection()
        if conn is None:
            return
        
        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO artworks (title, medium, price, status, artist_id, image_url)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (title, medium, price, status, artist_id, image_url))
            
            conn.commit()
            print(f"✅ Artwork '{title}' added successfully!")
        except Exception as e:
            print("❌ Error adding artwork:", e)
        finally:
            cur.close()
            conn.close()

    # 🟣 READ
    @staticmethod
    def view_all_artworks():
        conn = get_connection()
        if conn is None:
            return
        
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT a.id, a.title, a.medium, a.price, a.status, a.image_url, ar.name
                FROM artworks a
                JOIN artists ar ON a.artist_id = ar.id
                ORDER BY a.id;
            """)
            
            artworks = cur.fetchall()
            print("🎨 All Artworks:")
            for art in artworks:
                print(art)
        except Exception as e:
            print("❌ Error fetching artworks:", e)
        finally:
            cur.close()
            conn.close()

    # 🟡 UPDATE
    @staticmethod
    def update_artwork(artwork_id, title=None, medium=None, price=None, status=None, image_url=None):
        conn = get_connection()
        if conn is None:
            return
        
        try:
            cur = conn.cursor()
            updates = []
            values = []
            
            if title:
                updates.append("title = %s")
                values.append(title)
            if medium:
                updates.append("medium = %s")
                values.append(medium)
            if price:
                updates.append("price = %s")
                values.append(price)
            if status:
                updates.append("status = %s")
                values.append(status)
            if image_url:
                updates.append("image_url = %s")
                values.append(image_url)
            
            if not updates:
                print("⚠️ No fields provided to update.")
                return

            values.append(artwork_id)
            sql = f"UPDATE artworks SET {', '.join(updates)} WHERE id = %s;"
            cur.execute(sql, values)
            conn.commit()
            print(f"📝 Artwork ID {artwork_id} updated successfully!")
        except Exception as e:
            print("❌ Error updating artwork:", e)
        finally:
            cur.close()
            conn.close()

    # 🔴 DELETE
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
