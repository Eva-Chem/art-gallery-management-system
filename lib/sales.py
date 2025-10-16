from lib.db import get_connection

class Sale:
    @staticmethod
    def add_sale(artwork_id, buyer_name, sale_amount, sale_date):
        conn = get_connection()
        if conn is None:
            return

        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO sales (artwork_id, buyer_name, sale_date, sale_amount)
                VALUES (%s, %s, %s::date, %s);
            """, (artwork_id, buyer_name, sale_date, sale_amount))
            
            conn.commit()
            print(f"✅ Sale added successfully for artwork ID {artwork_id}!")
        except Exception as e:
            print("❌ Error adding sale:", e)
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def view_all_sales():
        conn = get_connection()
        if conn is None:
            return

        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT s.id, a.title, s.buyer_name, s.sale_date, s.sale_amount
                FROM sales s
                JOIN artworks a ON s.artwork_id = a.id;
            """)
            sales = cur.fetchall()
            print("💰 All Sales:")
            for s in sales:
                print(s)
        except Exception as e:
            print("❌ Error fetching sales:", e)
        finally:
            cur.close()
            conn.close()
