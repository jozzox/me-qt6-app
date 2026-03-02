import sys

from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow


def main():
    # Initialize application
    app = QtWidgets.QApplication(sys.argv)

    # Create main window
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("me-qt6-app")
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    # Run event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
