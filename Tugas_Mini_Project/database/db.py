import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("keuangan.db")
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS keuangan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT,
            kategori TEXT,
            deskripsi TEXT,
            jumlah INTEGER,
            tipe TEXT
        )
        """)
        self.conn.commit()

    def insert_data(self, data):
        self.conn.execute("""
        INSERT INTO keuangan (tanggal, kategori, deskripsi, jumlah, tipe)
        VALUES (?, ?, ?, ?, ?)
        """, data)
        self.conn.commit()

    def get_all(self):
        return self.conn.execute("SELECT * FROM keuangan").fetchall()