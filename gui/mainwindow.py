from PySide2.QtCore import Slot
from PySide2.QtWidgets import QAction, QApplication, QFormLayout, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        self.setWindowTitle("Jugo")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        self.settings_menu = self.menu.addMenu("Settings")
        self.about_menu = self.menu.addMenu("About")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)
        
        # Adding exit action to file menu
        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()
