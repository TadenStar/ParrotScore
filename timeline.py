import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QFileDialog, QAction
)


class TimelineWindow(QMainWindow):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Timeline")
        self._setup_ui()
        self._create_menu()

    def _setup_ui(self) -> None:
        """Create widgets and layout."""
        self.path_edit = QLineEdit()
        self.fill_button = QPushButton("Fill in")

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.path_edit)
        layout.addWidget(self.fill_button)

        self.setCentralWidget(central_widget)

    def _create_menu(self) -> None:
        """Create menu with 'Select date' and 'Reset' items."""
        menu = self.menuBar().addMenu("File")

        select_action = QAction("Select date", self)
        select_action.triggered.connect(self._select_date)
        menu.addAction(select_action)

        reset_action = QAction("Reset", self)
        reset_action.triggered.connect(self._reset_path)
        menu.addAction(reset_action)

    def _select_date(self) -> None:
        """Open dialog for selecting a directory."""
        directory = QFileDialog.getExistingDirectory(self, "Select date folder")
        if directory:
            self.path_edit.setText(directory)

    def _reset_path(self) -> None:
        """Clear the path input field."""
        self.path_edit.clear()


def main() -> None:
    """Application entry point."""
    app = QApplication(sys.argv)
    window = TimelineWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
