#!/usr/bin/env python3

import sys
import random
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit, QDialog, QVBoxLayout
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl, Slot


@Slot()
def say_hello():
    print("Button clicked, Hello!")


class Form(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Form")
        # Create widgets
        self.edit = QLineEdit("Write my name here..")
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    @Slot()
    def greetings(self):
        print("Hello %s" % self.edit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # button = QPushButton("CLICK ME")
    # button.clicked.connect(say_hello)
    # button.show()

    # url = QUrl("view.qml")
    # view = QQuickView(url)
    # view.show()

    form = Form()
    form.show()

    sys.exit(app.exec_())
