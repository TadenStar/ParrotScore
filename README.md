# Timeline GUI

This project provides a simple desktop application using **PySide6**.

## Features

- Window titled "Timeline".
- Menu with actions **Select date** and **Reset**.
- Text field for entering a path to a date.
- "Fill in" button reserved for future functionality.

## Running

```bash
pip install PySide6
python timeline.py
```

## Packaging

Create an executable with [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile timeline.py
```
