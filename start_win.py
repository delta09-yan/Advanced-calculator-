import sys

from PyQt6.QtWidgets import QApplication
from main_win import Calculator


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())