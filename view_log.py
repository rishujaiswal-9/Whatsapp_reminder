import sqlite3
import pandas as pd

print("\n📜 --- Message Logs ---\n")

conn = sqlite3.connect("messages.db")
df = pd.read_sql_query("SELECT * FROM logs ORDER BY id DESC", conn)
conn.close()

if df.empty:
    print("No logs found.")
else:
    for _, row in df.iterrows():
        print(f"👤 {row['name']} | 📱 {row['phone']}")
        print(f"💬 {row['message']}")
        print(f"📌 {row['status']} | ⏰ {row['sent_at']}")
        print("-" * 40)