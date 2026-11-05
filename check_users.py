import os
import sqlite3
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

db_name = os.getenv("DATABASE_NAME", "sharia_platform.db")
db_path = BASE_DIR / db_name

print("مسار قاعدة البيانات:", db_path)
print("هل الملف موجود؟", db_path.exists())

if db_path.exists():
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row

    users = db.execute("""
        SELECT id, username, length(password) AS hash_length, is_admin
        FROM users
    """).fetchall()

    print("\nالحسابات المسجلة:")

    for user in users:
        print(dict(user))

    db.close()