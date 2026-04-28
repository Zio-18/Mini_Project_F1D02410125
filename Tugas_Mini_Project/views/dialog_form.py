from PySide6.QtWidgets import (
    QDialog, QFormLayout, QLineEdit,
    QPushButton, QComboBox, QDateEdit,
    QVBoxLayout, QWidget
)
from PySide6.QtCore import QDate, Qt

class FormDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tambah Data Keuangan")
        self.setFixedWidth(350)
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        form_container = QWidget()
        layout = QFormLayout(form_container)
        layout.setSpacing(12)
        layout.setLabelAlignment(Qt.AlignLeft)

        self.tanggal = QDateEdit()
        self.tanggal.setDate(QDate.currentDate())
        self.tanggal.setCalendarPopup(True)
        self.tanggal.setDisplayFormat("dd/MM/yyyy")

        self.kategori = QLineEdit()
        self.kategori.setPlaceholderText("Misal: Makanan")
        
        self.deskripsi = QLineEdit()
        self.deskripsi.setPlaceholderText("Keterangan transaksi")
        
        self.jumlah = QLineEdit()
        self.jumlah.setPlaceholderText("0")

        self.tipe = QComboBox()
        self.tipe.addItems(["Pemasukan", "Pengeluaran"])

        self.btn_simpan = QPushButton("Simpan")
        self.btn_simpan.setCursor(Qt.PointingHandCursor)

        layout.addRow("Tanggal", self.tanggal)
        layout.addRow("Kategori", self.kategori)
        layout.addRow("Deskripsi", self.deskripsi)
        layout.addRow("Jumlah", self.jumlah)
        layout.addRow("Tipe", self.tipe)

        main_layout.addWidget(form_container)
        main_layout.addWidget(self.btn_simpan)

        self.btn_simpan.clicked.connect(self.accept)

    def ambil_data(self):
        return (
            self.tanggal.date().toString("yyyy-MM-dd"),
            self.kategori.text(),
            self.deskripsi.text(),
            int(self.jumlah.text() if self.jumlah.text().isdigit() else 0),
            self.tipe.currentText()
        )