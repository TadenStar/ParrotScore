"""Simple PySide6 starter application with a movable square."""

from __future__ import annotations

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget


class MovableSquare:
    """Represents a square that can move within the play area."""

    def __init__(self, x: int = 580, y: int = 380, size: int = 40, step: int = 20,
                 color: QColor = QColor("white")) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.step = step
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

    def draw(self, painter: QPainter) -> None:
        painter.setBrush(self.color)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.x, self.y, self.size, self.size)


class PlayArea(QWidget):
    """Widget responsible for rendering the movable square."""

    def __init__(self, square: MovableSquare, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.square = square
        self.setStyleSheet("background-color: #555555;")

    def paintEvent(self, event) -> None:  # type: ignore[override]
        painter = QPainter(self)
        self.square.draw(painter)


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Starter Window")
        self.setFixedSize(1200, 800)
        self.square = MovableSquare()
        self.play_area = PlayArea(self.square)
        self.setCentralWidget(self.play_area)

    def keyPressEvent(self, event) -> None:  # type: ignore[override]
        key = event.key()
        if key == Qt.Key_W:
            self.square.move(0, -self.square.step)
        elif key == Qt.Key_S:
            self.square.move(0, self.square.step)
        elif key == Qt.Key_A:
            self.square.move(-self.square.step, 0)
        elif key == Qt.Key_D:
            self.square.move(self.square.step, 0)
        else:
            super().keyPressEvent(event)
            return
        self.play_area.update()


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
