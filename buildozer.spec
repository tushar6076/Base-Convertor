[app]

# (str) Title of your application
title = Base Convertor

# (str) Package name
package.name = baseconvertor

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,db

# (list) List of directory to exclude
source.exclude_dirs = venv, bin, __pycache__, .git, _COMPILED, _DOCS

# (list) List of exclusions using pattern matching
source.exclude_patterns = __pycache__/*, *.pyc, *.pyo, *.docx, *.exe, *.spec

# (str) Application versioning
version = 0.1

# (list) Application requirements
# -------------------------------------------------------------------------------------------------
# Option A (Stable / Universally Compatible - baseconvertor101 build):
requirements = python3, kivy==2.2.0, kivymd==1.0.2, sqlite3, pillow
#
# Option B (Later version - baseconvertor build):
# requirements = python3, kivy==2.2.0, kivymd==1.1.1, sqlite3, pillow
# -------------------------------------------------------------------------------------------------

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/presplash.jpg

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/icon.png

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0


# =======================================================
# Android specific
# =======================================================

# (string) Presplash background color
android.presplash_color = #0073B0

# (list) Permissions (None required - Base Convertor runs completely offline with local SQLite)
android.permissions =

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) screenOrientation to set for the main activity
android.manifest.orientation = portrait

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

# (bool) Skip byte compile for .py files
android.no-byte-compile-python = False

# (str) The format used to package the app for release mode
android.release_artifact = apk

# (str) The format used to package the app for debug mode
android.debug_artifact = apk

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1