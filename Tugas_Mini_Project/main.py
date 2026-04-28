import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow

def load_style(app):
    try:
        with open("style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except:
        pass

app = QApplication(sys.argv)

load_style(app)

window = MainWindow()
window.show()

sys.exit(app.exec())