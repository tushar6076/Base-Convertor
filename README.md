# Base Convertor

Base Convertor is an offline number-base conversion app built with Python, Kivy, and KivyMD. It converts values between decimal, binary, octal, and hexadecimal, and keeps a local history of successful conversions in SQLite.

## Features

- Convert between all pairs of decimal, binary, octal, and hexadecimal.
- Convert integer and fractional values. Fractional calculations use floating-point arithmetic; non-decimal fractional expansions are limited to 10 digits, so results may be approximate.
- Choose a conversion mode from the on-screen menu and see validation feedback for invalid input.
- View previous successful conversions, including their conversion mode and timestamp.
- Use the app without network access or special Android permissions.
- Build an Android APK with the included Buildozer configuration.

## Requirements

- Python 3.10 is recommended (see the version note in `requirements.txt`).
- `pip` and a virtual environment for local development.
- For Android builds, Buildozer's Android SDK/NDK toolchain requirements. A Linux environment is recommended; on Windows, use WSL.

## Run locally

Create and activate a virtual environment, then install the app dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install kivy==2.2.0 kivymd==1.0.2 pillow
```

Run the app from the project root:

```bash
python main.py
```

The full [`requirements.txt`](requirements.txt) also includes tools for packaging, including Buildozer and PyInstaller. Those tools are not needed just to run the app locally.

## Use the app

1. Choose a conversion direction from the menu (for example, **Decimal to Binary**).
2. Enter a value using digits valid for the selected source base. Use `A`–`F` for hexadecimal digits.
3. Press **Convert** or submit the input.
4. Read the result below the input. Successful conversions are added to the history drawer.

## Build for Android

Buildozer and its Android prerequisites must be installed and configured for your environment. From the project root, build a debug APK with:

```bash
buildozer android debug
```

The generated APK is placed in `bin/`. The current [`buildozer.spec`](buildozer.spec) configures a portrait app targeting Android API 33, with a minimum API level of 21 and `arm64-v8a`/`armeabi-v7a` architectures. It also specifies the app icon, presplash, and runtime requirements.

## Conversion history

The app creates and uses `history.db` in its working/private app storage. On desktop, run `main.py` from the project root to keep the database in the expected location. The database stores the conversion mode, input/output summary, and timestamp; no remote service is used.

## Project files

```text
.
├── assets/          # App icon and presplash image
├── _COMPILED/       # Previously generated distribution files
├── _DOCS/           # Project documents
├── main.py          # App UI, conversion logic, and history handling
├── requirements.txt # Runtime and packaging dependencies
├── buildozer.spec   # Android packaging configuration
├── LICENSE
└── README.md
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for the terms.
