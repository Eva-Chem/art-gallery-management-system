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
                INSERT INTO sales (artwork_id, buyer_name, sale_amount, sale_date)
                VALUES (%s, %s, %s, %s);
            """, (artwork_id, buyer_name, sale_amount, sale_date))
            
            conn.commit()
            print(f"✅ Sale recorded for artwork ID {artwork_id} (Buyer: {buyer_name})!")
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
                SELECT s.id, a.title, s.buyer_name, s.sale_amount, s.sale_date
                FROM sales s
                JOIN artworks a ON s.artwork_id = a.id
                ORDER BY s.sale_date DESC;
            """)
            
            sales = cur.fetchall()
            print("💰 All Sales:")
            for sale in sales:
                print(sale)
        except Exception as e:
            print("❌ Error fetching sales:", e)
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def update_sale(sale_id, buyer_name=None, sale_amount=None, sale_date=None):
        conn = get_connection()
        if conn is None:
            return
        
        try:
            fields = []
            values = []

            if buyer_name:
                fields.append("buyer_name = %s")
                values.append(buyer_name)
            if sale_amount:
                fields.append("sale_amount = %s")
                values.append(sale_amount)
            if sale_date:
                fields.append("sale_date = %s")
                values.append(sale_date)

            if not fields:
                print("⚠️ No fields provided for update.")
                return

            values.append(sale_id)
            sql = f"UPDATE sales SET {', '.join(fields)} WHERE id = %s;"
            
            cur = conn.cursor()
            cur.execute(sql, tuple(values))
            conn.commit()

            if cur.rowcount > 0:
                print(f"✅ Sale ID {sale_id} updated successfully!")
            else:
                print(f"⚠️ No sale found with ID {sale_id}.")
        except Exception as e:
            print("❌ Error updating sale:", e)
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def delete_sale(sale_id):
        conn = get_connection()
        if conn is None:
            return
        
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM sales WHERE id = %s;", (sale_id,))
            conn.commit()
            
            if cur.rowcount > 0:
                print(f"🗑️ Sale ID {sale_id} deleted successfully!")
            else:
                print(f"⚠️ No sale found with ID {sale_id}.")
        except Exception as e:
            print("❌ Error deleting sale:", e)
        finally:
            cur.close()
            conn.close()
