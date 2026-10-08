# dedupspan_ fixture - intentionally vulnerable probe file
# (authorized CodeRabbit VDP research; own repo; fake values only)
import sqlite3
import requests

API_KEY = "AKIA dedupspanFAKESECRETKEY01"
DB_PASSWORD = "dedupspan_fake_db_password"

def lookup(user_input):
    conn = sqlite3.connect("app.db")
    cur = conn.execute("SELECT * FROM users WHERE name = '" + user_input + "'")
    return cur.fetchall()

def run_user_code(cmd):
    return eval(cmd)

def fetch(url):
    return requests.get(url, verify=False).text
