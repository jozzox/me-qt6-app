#!/usr/bin/env python3
"""Compile Qt UI files to Python modules."""

import os

from PyQt6.uic.compile_ui import compileUi


def build_ui():
    """Compile all .ui files in ui/ directory to Python modules."""
    ui_dir = "ui"

    for filename in os.listdir(ui_dir):
        if filename.endswith(".ui"):
            ui_file = os.path.join(ui_dir, filename)
            py_file = os.path.join(
                ui_dir, f"{filename[:-3]}.py"
            )  # Replace .ui with .py

            print(f"Compiling {ui_file} to {py_file}")
            with open(py_file, "w") as out:
                compileUi(ui_file, out)


if __name__ == "__main__":
    build_ui()
    print("UI build complete!")
