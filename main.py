
#PyQt6 imports
from PyQt6.QtWidgets import QApplication

# Local resource imports
from windows import FuckYouWindow

app = QApplication([])
window = FuckYouWindow()
app.exec()