from PySide2.QtCore import Slot
from PySide2.QtWidgets import (
    QApplication,
    QFileDialog,
    QFormLayout,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpacerItem,
    QWidget,
)
import subprocess
import os


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.junit_button = QPushButton("Select File")
        self.junit_button.clicked.connect(self.open_junit_file_browser)
        self.junit_file_path = QLabel("Path to JUnit.jar File")

        self.java_package_dir_button = QPushButton("Select Directory")
        self.java_package_dir_button.clicked.connect(self.open_java_package_dir)
        self.java_package_dir = QLabel("Path to Java Package Directory")
        self.java_test_file = QLineEdit("")
        self.java_test_file.setPlaceholderText("e.g. com.pack.AppTest")

        self.python_dir_button = QPushButton("Select Directory")
        self.python_dir_button.clicked.connect(self.open_python_dir)
        self.python_dir = QLabel("Path to Python Tests Directory")

        self.python_file_button = QPushButton("Select File")
        self.python_file_button.clicked.connect(self.open_python_file_browser)
        self.python_file_path = QLabel("Path to test_*.py File")

        self.output_dir_button = QPushButton("Select Output Directory")
        self.output_dir_button.clicked.connect(self.open_output_dir_browser)
        self.output_dir_path = QLabel("Output Directory ...")

        self.run_tests_button = QPushButton("Run Test Execution")
        self.run_tests_button.clicked.connect(self.run_tests)
        self.run_tests_button.setProperty("class", "success")

        # QWidget Layout
        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(10)

        self.layout.addWidget(self.junit_button, 0, 0)
        self.layout.addWidget(self.junit_file_path, 0, 1)

        self.layout.addWidget(self.java_package_dir_button, 1, 0)
        self.layout.addWidget(self.java_package_dir, 1, 1)
        self.layout.addWidget(self.java_test_file, 1, 4)

        self.layout.addWidget(self.python_dir_button, 2, 0)
        self.layout.addWidget(self.python_dir, 2, 1)

        self.layout.addWidget(self.python_file_button, 3, 0)
        self.layout.addWidget(self.python_file_path, 3, 1)

        self.layout.addWidget(self.output_dir_button, 4, 0)
        self.layout.addWidget(self.output_dir_path, 4, 1)
        self.layout.addWidget(self.run_tests_button, 4, 4)

        # Set the layout to the QWidget
        self.setLayout(self.layout)

    @Slot()
    def run_tests(self, *args, **kwargs):
        junit = self.junit_file_path.text()
        jpack = self.java_package_dir.text()
        jfile = self.java_test_file.text()
        pydir = self.python_dir.text()
        pyfile = self.python_file_path.text()
        outdir = self.output_dir_path.text()

        if not outdir:
            return

        if os.path.exists(junit) and os.path.exists(jpack):
            command = []

        if os.path.exists(junit) and os.path.exists(jpack) and os.path.exists(jfile):
            command = []

        if os.path.exists(pydir):
            command = []

        if os.path.exists(pyfile):
            command = []

    @Slot()
    def open_output_dir_browser(self, *args, **kwargs):
        output_dir_path = (
            QFileDialog.getExistingDirectory(
                self,
                "Select Output Directory",
                "/home",
                options=QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
            ),
        )

        output_dir_path = output_dir_path[0]

        self.output_dir_path.setText(output_dir_path) if output_dir_path else None

    @Slot()
    def open_junit_file_browser(self, *args, **kwargs):
        junit_file_path, extension = QFileDialog.getOpenFileName(
            self, "Select JUnit.jar File", "/home", "Jar Files (*.jar)"
        )
        self.junit_file_path.setText(junit_file_path) if junit_file_path else None

    @Slot()
    def open_java_package_dir(self, *args, **kwargs):
        java_package_dir = (
            QFileDialog.getExistingDirectory(
                self,
                "Select Java Package Directory",
                "/home",
                options=QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
            ),
        )

        java_package_dir = java_package_dir[0]

        self.java_package_dir.setText(java_package_dir) if java_package_dir else None

    @Slot()
    def open_python_dir(self, *args, **kwargs):
        python_dir = (
            QFileDialog.getExistingDirectory(
                self,
                "Select Python Test Case Directory",
                "/home",
                options=QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
            ),
        )

        python_dir = python_dir[0]

        self.python_dir.setText(python_dir) if python_dir else None

    @Slot()
    def open_python_file_browser(self, *args, **kwargs):
        python_file_path, extension = QFileDialog.getOpenFileName(
            self, "Select test_*.py File", "/home", "Python Test Case Files (test_*.py)"
        )
        self.python_file_path.setText(python_file_path) if python_file_path else None
