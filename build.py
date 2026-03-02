#!/usr/bin/env -S uv run python
"""Compile Qt UI files to Python modules."""

import os
from typing import TYPE_CHECKING, TextIO

if TYPE_CHECKING:

    def compileUi(
        uifile: str,
        pyfile: TextIO,
        execute: bool = False,
        indent: int = 4,
    ) -> None:
        # Type-checking stub for PyQt6 uic helpers.
        ...
else:
    from PyQt6.uic.compile_ui import compileUi


def build_ui():
    """Compile all .ui files in ui/ directory to Python modules."""
    ui_dir = "ui"

    def postprocess_ui_py(py_path: str) -> None:
        """Patch generated files with stable typing to satisfy Pylance."""
        with open(py_path, "r", encoding="utf-8") as handle:
            content = handle.read()

        if "# pyright: reportUnusedImport=false" not in content:
            content = "# pyright: reportUnusedImport=false\n" + content

        content = content.replace(
            "from PyQt6 import QtCore, QtGui, QtWidgets",
            "from PyQt6 import QtCore, QtGui, QtWidgets  # type: ignore[reportUnusedImport]",
        )
        content = content.replace(
            "def setupUi(self, MainWindow):",
            "def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:",
        )
        content = content.replace(
            "def retranslateUi(self, MainWindow):",
            "def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:",
        )

        with open(py_path, "w", encoding="utf-8") as handle:
            handle.write(content)

    for filename in os.listdir(ui_dir):
        if filename.endswith(".ui"):
            ui_file = os.path.join(ui_dir, filename)
            py_file = os.path.join(
                ui_dir, f"{filename[:-3]}.py"
            )  # Replace .ui with .py

            print(f"Compiling {ui_file} to {py_file}")
            with open(py_file, "w") as out:
                compileUi(ui_file, out)
            postprocess_ui_py(py_file)


if __name__ == "__main__":
    build_ui()
    print("UI build complete!")
