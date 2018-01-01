import sys

from cx_Freeze import setup, Executable

path = sys.path
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "re", "tkinter"],
                     "include_files": ["packages"],
                     "path": path, "optimize": 2}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
icone = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="cutting backboard.py",
      version="0.1",
      description="cutting backboard by scwall",
      options={"build_exe": build_exe_options},
      executables=[Executable("main.py", base=base, icon=icone)])
