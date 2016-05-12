from cx_Freeze import setup, Executable

setup( 
	name = "main" , version = "0.1" , description = "main" , executables = [Executable("main.py")] , )