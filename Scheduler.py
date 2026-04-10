import pywhatkit
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import time
import os
import re

FILE = "contacts.xlsx"

MAX_RETRIES = 3
RETRY_DELAY = 2      # minutes
CHECK_INTERVAL = 60  # seconds


# ----------- clean phone -----------
def clean_phone(phone):
    phone = str(phone)
    phone = re.sub(r'\D', '', phone)
    return "+91" + phone[-10:]


# ----------- main function -----------
def run():

    if not os.path.exists(FILE):
        print("❌ contacts.xlsx not found")
        return False

    df = pd.read_excel(FILE)

    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    # logs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        message TEXT,
        status TEXT,
        sent_at TEXT
    )
    """)

    # status table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS status_table (
        phone TEXT PRIMARY KEY,
        status TEXT,
        retries INTEGER,
        last_attempt TEXT
    )
    """)

    # 🔥 RESET EVERY RUN (important)
    cursor.execute("DELETE FROM status_table")
    conn.commit()

    print("\n🔄 Fresh start (old status cleared)\n")

    all_done = True

    for _, row in df.iterrows():

        name = row["name"]
        message = row["message"]

        try:
            phone = clean_phone(row["phone"])
            hour = int(row["hour"])
            minute = int(row["minute"])
        except:
            print(f"⚠️ Skipping {name} (invalid data)")
            continue

        status = "PENDING"
        retries = 0
        last_attempt = ""

        if status != "DONE":
            all_done = False

        print(f"📩 Sending to {name}")

        try:
            pywhatkit.sendwhatmsg(
                phone,
                message,
                hour,
                minute,
                wait_time=25,
                tab_close=True,
                close_time=3
            )

            status = "DONE"
            print(f"✅ Sent to {name}")

            log_status = "SUCCESS"

        except Exception as e:
            status = "FAILED"
            retries += 1
            print(f"❌ Failed for {name}")

            log_status = f"FAILED: {str(e)}"
            all_done = False

        last_attempt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # save status
        cursor.execute("""
        INSERT OR REPLACE INTO status_table (phone, status, retries, last_attempt)
        VALUES (?, ?, ?, ?)
        """, (phone, status, retries, last_attempt))

        # save log
        cursor.execute("""
        INSERT INTO logs (name, phone, message, status, sent_at)
        VALUES (?, ?, ?, ?, ?)
        """, (name, phone, message, log_status, last_attempt))

        conn.commit()

        time.sleep(15)

    conn.close()
    return all_done


# ----------- run once and stop -----------
print("🚀 Scheduler started...\n")

run()

print("\n🎉 Process finished. You can run again anytime.\n")