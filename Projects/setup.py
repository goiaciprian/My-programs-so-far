import sys
from cx_Freeze import setup, Executable
import os.path
import tkinter

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

build_exe_options = {"packages": ["os", "tkinter"]}

base = None
if sys.platform == 'win32':
    base = "Win32GUI"
setup(
    name='Alarma',
    version='0.1',
    description='Alarma cu interfata.',
    options={"build_exe": build_exe_options},
    executables=[Executable("ceas.py", base=base)]
)
