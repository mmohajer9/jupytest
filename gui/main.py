#!/usr/bin/env python3
import sys
from PySide2.QtWidgets import (
    QApplication,
)
from qt_material import apply_stylesheet

from mainwindow import MainWindow
from widget import Widget


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    widget = Widget()
    window = MainWindow(widget)

    extra = {
        # Button colors
        "danger": "#dc3545",
        "warning": "#ffc107",
        "success": "#17a2b8",
        # Font
        "font-family": "Roboto",
    }

    apply_stylesheet(app, theme="dark_amber.xml" , extra=extra)

    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec_())
