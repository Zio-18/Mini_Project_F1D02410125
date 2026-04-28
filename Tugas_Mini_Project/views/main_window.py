from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget,
    QTableWidgetItem, QMessageBox,
    QMenuBar, QLabel, QFrame
)
from views.dialog_form import FormDialog
from controllers.keuangan_controller import KeuanganController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance Pro - Management")
        self.resize(1000, 650)

        self.controller = KeuanganController()

        container = QWidget()
        self.setCentralWidget(container)
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(30, 20, 30, 30)
        main_layout.setSpacing(20)

        header_widget = QWidget()
        header_layout = QVBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 0)

        self.title = QLabel("💰 Manajemen Keuangan Pribadi")
        self.title.setObjectName("titleLabel")
        
        self.info = QLabel("Nama: Muhammad Zia Ul Haq | NIM: F1D02410125")
        self.info.setObjectName("infoLabel")

        header_layout.addWidget(self.title)
        header_layout.addWidget(self.info)
        
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("color: #dcdfe6;")

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Tanggal", "Kategori", "Deskripsi", "Jumlah", "Tipe"]
        )
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)

        button_layout = QHBoxLayout()
        self.btn_tambah = QPushButton("＋ Tambah Data Baru")
        self.btn_tambah.setFixedWidth(200)
        self.btn_tambah.setFixedHeight(45)
        button_layout.addStretch()
        button_layout.addWidget(self.btn_tambah)

        main_layout.addWidget(header_widget)
        main_layout.addWidget(line)
        main_layout.addWidget(self.table)
        main_layout.addLayout(button_layout)

        self.btn_tambah.clicked.connect(self.tambah_data)
        self.load_data()
        self.buat_menu()

    def buat_menu(self):
        menu = QMenuBar()
        self.setMenuBar(menu)
        tentang = menu.addMenu("Tentang")
        action = tentang.addAction("Tentang Aplikasi")
        action.triggered.connect(self.show_about)

    def show_about(self):
        QMessageBox.information(
            self,
            "Tentang",
            "Aplikasi Keuangan v1.0\n\nDikembangkan oleh:\nMuhammad Zia Ul Haq\nNIM: F1D02410125"
        )

    def tambah_data(self):
        dialog = FormDialog()
        if dialog.exec():
            try:
                data = dialog.ambil_data()
                self.controller.tambah(data)
                QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
                self.load_data()
            except ValueError:
                QMessageBox.warning(self, "Error", "Input tidak valid! Pastikan 'Jumlah' adalah angka.")

    def load_data(self):
        data = self.controller.tampil()
        self.table.setRowCount(len(data))
        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row_idx, col_idx, item)