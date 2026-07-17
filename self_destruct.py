
"""
Self-Destruct Message
----------------------
Message encrypt karke ek code deta hai. Wo code sirf ek baar
use ho sakta hai (ya expiry time khatam hone tak) — uske baad
message database se permanently delete ho jata hai.

Usage:
    python self_destruct.py --create
    python self_destruct.py --create --expires 1
    python self_destruct.py --read SD-xxxxxx
"""

import argparse
import random
import sqlite3
import string
from datetime import datetime, timedelta
from pathlib import Path

from cryptography.fernet import Fernet

DB_PATH = Path(__file__).parent / "messages.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS messages (
            code TEXT PRIMARY KEY,
            encrypted_text TEXT NOT NULL,
            key TEXT NOT NULL,
            expires_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn


def generate_code():
    chars = string.ascii_lowercase + string.digits
    return "SD-" + "".join(random.choice(chars) for _ in range(6))


def create_message(conn, expires_hours):
    text = input("Apna message likhein: ")

    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(text.encode()).decode()

    code = generate_code()
    # Ensure code unique hai (chance kam hai but phir bhi check)
    while conn.execute("SELECT 1 FROM messages WHERE code=?", (code,)).fetchone():
        code = generate_code()

    expires_at = (datetime.now() + timedelta(hours=expires_hours)).isoformat()

    conn.execute(
        "INSERT INTO messages (code, encrypted_text, key, expires_at) VALUES (?, ?, ?, ?)",
        (code, encrypted, key.decode(), expires_at),
    )
    conn.commit()

    print("\nMessage save ho gaya.")
    print(f"Code   : {code}")
    print(f"Expiry : {expires_hours} ghante mein (ya read hote hi turant delete)")
    print("\nYe code kisi ko bhejo — read hone ke baad ye hamesha ke liye delete ho jayega.")


def read_message(conn, code):
    row = conn.execute(
        "SELECT encrypted_text, key, expires_at FROM messages WHERE code=?", (code,)
    ).fetchone()

    if not row:
        print("Ye message exist nahi karta — ya to already read ho chuka hai, ya galat code hai.")
        return

    encrypted_text, key, expires_at = row

    # Expiry check
    if datetime.now() > datetime.fromisoformat(expires_at):
        conn.execute("DELETE FROM messages WHERE code=?", (code,))
        conn.commit()
        print("Ye message expire ho chuka hai. Ab delete kar diya gaya hai.")
        return

    fernet = Fernet(key.encode())
    try:
        decrypted = fernet.decrypt(encrypted_text.encode()).decode()
    except Exception:
        print("Message decrypt nahi ho saka — data corrupt ho sakta hai.")
        return

    # Read hone ke baad turant delete
    conn.execute("DELETE FROM messages WHERE code=?", (code,))
    conn.commit()

    print("\n" + "=" * 40)
    print("MESSAGE:")
    print(decrypted)
    print("=" * 40)
    print("Ye message ab permanently delete ho chuka hai.")


def main():
    parser = argparse.ArgumentParser(description="Self-Destruct Message Tool")
    parser.add_argument("--create", action="store_true", help="Naya message banao")
    parser.add_argument("--expires", type=float, default=24, help="Expiry time ghanton mein (default: 24)")
    parser.add_argument("--read", metavar="CODE", help="Message read karo code se")
    args = parser.parse_args()

    conn = init_db()

    if args.create:
        create_message(conn, args.expires)
    elif args.read:
        read_message(conn, args.read)
    else:
        parser.print_help()

    conn.close()


if __name__ == "__main__":
    main()
