# Base Convertor

A Python-based mobile utility app for converting numbers between common numeral systems, including decimal, binary, octal, and hexadecimal. Built with Kivy and KivyMD, the app provides a simple touchscreen interface, instant conversion results, and a local conversion history stored in SQLite.

## Overview

Base Convertor is designed to make number-system conversions quick and easy on mobile devices. It supports both integer and fractional values and allows users to switch conversion types from a dropdown menu without leaving the screen.

The project is structured as a KivyMD app and is also configured for Android packaging via Buildozer, making it suitable for development, testing, and APK generation.

## Features

- Convert between:
  - Decimal ↔ Binary
  - Decimal ↔ Octal
  - Decimal ↔ Hexadecimal
  - Binary ↔ Octal
  - Binary ↔ Hexadecimal
  - Octal ↔ Hexadecimal
- Support for fractional inputs such as `10.5`, `101.011`, etc.
- Live conversion results with contextual validation messages
- Local history of prior conversions saved in `history.db`
- Drawer-based history panel for recent conversions
- Mobile-friendly UI built with Material Design styling
- Android packaging support via `buildozer.spec`

## Tech Stack

- Python 3
- Kivy
- KivyMD
- SQLite3
- Buildozer (for Android packaging)

## Project Structure

```text
Base Convertor/
├── main.py                 # Main application logic and UI definitions
├── buildozer.spec         # Android packaging configuration
├── history.db             # Local SQLite database for conversion history
├── .gitignore             # Git ignore rules
├── LICENSE                # Project license
├── assets/                # App assets / visual resources
├── _COMPILED/             # Compiled artifacts or packaged output
├── _DOCS/                 # Project documentation files
├── README.md              # Project overview and usage guide
└── .DS_Store              # macOS metadata file
```

## Installation

### Prerequisites

- Python 3.8+
- pip
- A virtual environment is recommended

### Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install kivy kivymd
```

## Running the App

From the project root, run:

```bash
python main.py
```

This launches the KivyMD application window locally.

## Android Build

This project includes a `buildozer.spec` file for Android packaging.

To build an APK:

```bash
pip install buildozer
buildozer android debug
```

If you are deploying to Android, Buildozer will package the app according to the settings defined in `buildozer.spec`.

## How It Works

1. Select the conversion mode from the dropdown menu.
2. Enter a number in the input field.
3. Tap the Convert button.
4. The app converts the value and displays the result.
5. Successful conversions are saved to the local SQLite database and shown in the history drawer.

## Notes

- The app stores conversion records using the current timestamp and a generated conversion summary.
- Conversion validation is handled in the main app logic, with detailed error messages shown for invalid inputs.
- The app uses a local SQLite database rather than a remote service, keeping the feature self-contained and lightweight.

## License

This project is licensed under the terms of the included [LICENSE](LICENSE) file.

## Contributing

Contributions are welcome. If you want to improve the app, you can:

- add more numeral-system conversions
- improve validation for edge cases
- add a cleaner settings panel
- enhance the UI for better accessibility and responsiveness
- refine Android packaging for release builds

## Author

This project was created as a personal utility application for quick base conversion tasks and is suitable for learning, experimentation, and mobile app prototyping.
