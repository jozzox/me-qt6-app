import sys

from qtpy import QtWidgets


def main():
    # Initialize application
    app = QtWidgets.QApplication(sys.argv)

    # Create main window
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("me-qt6-app")
    window.setGeometry(100, 100, 800, 600)
    window.show()

    # Run event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
