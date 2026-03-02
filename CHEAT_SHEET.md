# Qt6 PyApp - Setup Cheat Sheet

## 🎯 Projekt Übersicht

- **Name**: me-qt6-app
- **Version**: 0.1.0
- **Tech Stack**: PyQt6, Qt6, CMake, Python 3.11+
- **Plattform**: macOS M4
- **Entwicklungsumgebung**: Virtual Environment (.venv)

---

## ✅ Durchgeführte Schritte

### 1. Python-Shebang-Fix (build.py)

**Problem**: `#!/usr/bin/env python` funktioniert nicht auf macOS (Python 2 entfernt)

**Lösung**:

```bash
# Alte Version:
#!/usr/bin/env python

# Neue Version:
#!/usr/bin/env python3
```

**Datei**: [build.py](build.py#L1)

**Reason**: macOS hat nur `python3` nativ oder via Homebrew/pyenv

---

### 2. Python-Version Korrektur (pyproject.toml)

**Problem**: `requires-python = ">=3.14"` ist unrealistisch (Python 3.14 noch nicht veröffentlicht)

**Lösung**:

```toml
# Alte Version:
requires-python = ">=3.14"

# Neue Version:
requires-python = ">=3.11"
```

**Datei**: [pyproject.toml](pyproject.toml#L7)

**Reason**: Python 3.11 ist stabil, breit verfügbar und unterstützt alle modernen Features

---

### 3. Python 3.13 Installation

**Command**:

```bash
brew install python@3.13
```

**Status**: ✅ Already installed (3.13.12_1)

**Reason**: Global verfügbarer Python für Fallback außerhalb venv

---

### 4. Dependencies Installation

**Packages**:

- `pyqt6>=6.10.2` - Qt6 Python Bindings
- `qtpy>=2.4.3` - Qt Abstraktions-Layer

**Installation**:

```bash
pip3 install pyqt6>=6.10.2 qtpy>=2.4.3
```

**Status**: ✅ Erfolgreich in venv installiert

---

### 5. Build Script Executable Machen

**Command**:

```bash
chmod +x build.py
```

**Status**: ✅ build.py hat execute-Permissions

---

### 6. Validierung & Tests

**Test 1 - Mit venv**:

```bash
source .venv/bin/activate
python build.py

```

**Output**: ✅ `Compiling ui/mainwindow.ui to ui/mainwindow.py`

**Test 2 - Direct Execution**:

```bash

./build.py
```

**Output**: ✅ `UI build complete!`

---

## 🚀 Befehle für zukünftige Nutzung

### Entwicklung starten

```bash
source .venv/bin/activate
```

### UI-Dateien kompilieren

```bash
./build.py
# oder
python build.py
```

### Mit Qt6 & PyQt6 arbeiten

```bash
python main.py
```

### Neue Abhängigkeiten hinzufügen

```bash
pip install <package>
pip freeze > requirements.txt  # (wenn vorhanden)
```

---

## 📁 Projekt-Struktur

```markdown

me_qt6_app/
├── build.py              # UI Compiler (✅ Shebang fixed)
├── main.py              # Main Entry Point
├── pyproject.toml       # Project Config (✅ Python 3.11)
├── README.md            # Dokumentation
├── .venv/               # Virtual Environment (✅ Active)
└── ui/
    ├── mainwindow.ui    # Qt Designer File
    ├── mainwindow.h     # Qt Header
    ├── mainwindow.cpp   # Qt Implementation
    ├── main.cpp         # Qt Entry Point
    ├── CMakeLists.txt   # CMake Config
    └── mainwindow.py    # Generated (✅ From .ui via build.py)
```

---

## 🔧 Fehlerbehandlung

### Problem: "env: python: No such file or directory"

**Ursache**: Shebang zeigt auf nicht vorhandenes `python`

**Lösungen**:

1. Shebang zu `#!/usr/bin/env python3` ändern ✅ DONE
2. Oder: `python3 build.py` statt `./build.py` ausführen

### Problem: "ModuleNotFoundError: No module named 'PyQt6'"

**Ursache**: Packages nicht in aktivem Python installiert

**Lösung**:

```bash
source .venv/bin/activate
pip install pyqt6 qtpy
```

### Problem: Python Version Konflikt

**Ursache**: Verschiedene Python-Versionen im System

**Lösung**:

```bash
which python3           # Check path
python3 --version       # Check version
which python            # Überprüfe ob python existiert
```

---

## 💡 Best Practices für Zukunft

✅ **Immer venv verwenden**

```bash
source .venv/bin/activate
```

✅ **Shebang mit python3** in allen Scripts

```bash
#!/usr/bin/env python3
```

✅ **pyproject.toml realistisch halten**

```toml
requires-python = ">=3.11"  # Statt 3.14 oder 2.7
```

✅ **Dependencies dokumentieren**

- In `pyproject.toml` oder
- In `requirements.txt`

✅ **Build & Runtime testen**

```bash
./build.py && python main.py
```

---

## 📚 Referenzen

```markdown
| Resource          | Link                                                  |
| ----------------- | ----------------------------------------------------- |
| PyQt6 Docs        | https://www.riverbankcomputing.com/static/Docs/PyQt6/ |
| PEP 394 (python3) | https://www.python.org/dev/peps/pep-0394/             |
| Homebrew Python   | https://formulae.brew.sh/formula/python@3.13          |
| Qt6 Official      | https://www.qt.io/product/qt6                         |

---

**Status**: ✅ Projekt einsatzbereit
**Letztes Update**: 23. Februar 2026
