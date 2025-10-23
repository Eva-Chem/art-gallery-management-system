# lib/artists.py

from lib.db import get_connection

class Artist:
    @staticmethod
    def add_artist(name, nationality, birth_year):
        """Add a new artist to the database"""
        conn = get_connection()
        if conn is None:
            return
        
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
        """View all artists in the database"""
        conn = get_connection()
        if conn is None:
            return
        
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM artists ORDER BY id;")
            artists = cur.fetchall()

            print("🎨 All Artists:")
            if not artists:
                print("⚠️ No artists found.")
            else:
                for artist in artists:
                    print(artist)
        except Exception as e:
            print("❌ Error fetching artists:", e)
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def update_artist(artist_id, name=None, nationality=None, birth_year=None):
        """Update an existing artist’s details"""
        conn = get_connection()
        if conn is None:
            return
        
        try:
            cur = conn.cursor()
            fields = []
            values = []

            if name:
                fields.append("name = %s")
                values.append(name)
            if nationality:
                fields.append("nationality = %s")
                values.append(nationality)
            if birth_year:
                fields.append("birth_year = %s")
                values.append(birth_year)

            if not fields:
                print("⚠️ No fields to update.")
                return

            query = f"UPDATE artists SET {', '.join(fields)} WHERE id = %s;"
            values.append(artist_id)

            cur.execute(query, tuple(values))
            conn.commit()

            if cur.rowcount > 0:
                print(f"✅ Artist ID {artist_id} updated successfully!")
            else:
                print(f"⚠️ No artist found with ID {artist_id}.")
        except Exception as e:
            print("❌ Error updating artist:", e)
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def delete_artist(artist_id):
        """Delete an artist (with friendly handling for foreign key constraints)"""
        conn = get_connection()
        if conn is None:
            return

        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM artists WHERE id = %s;", (artist_id,))
            conn.commit()

            if cur.rowcount > 0:
                print(f"🗑️ Artist ID {artist_id} deleted successfully!")
            else:
                print(f"⚠️ No artist found with ID {artist_id}.")
        except Exception as e:
            if "violates foreign key constraint" in str(e):
                print(f"⚠️ Cannot delete artist ID {artist_id}: they still have artworks linked to them.")
            else:
                print("❌ Error deleting artist:", e)
        finally:
            cur.close()
            conn.close()
