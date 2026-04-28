from database.db import Database

class KeuanganController:
    def __init__(self):
        self.db = Database()

    def tambah(self, data):
        self.db.insert_data(data)

    def tampil(self):
        return self.db.get_all()