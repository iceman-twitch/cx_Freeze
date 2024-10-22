from cx_Freeze import setup, Executable

setup(
    name = "NAME",
    version = "1.0.2",
    description = "WriteDescription",
	author = "AUTHOR",
	license = "GNU GPLv3",
    executables = [Executable("filename.py")]
)
