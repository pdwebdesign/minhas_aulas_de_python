from cx_Freeze import setup, Executable

setup(
		name = "HAS",
		version = "1.0",
		description = ".py to .exe",
		executables = [Executable("hashtag.py")])