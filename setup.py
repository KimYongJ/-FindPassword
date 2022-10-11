from cx_Freeze import setup, Executable
buildOptions = dict(packages=['os', 'itertools','zipfile','winsound','time','datetime'], excludes = ["tkinter", "numpy"])

exe = [Executable('zippassword.py')] 
setup(
    name='FindPassword',
    version='0.0.1',
    description='FindPassword',
    options=dict(build_exe=buildOptions),
    executables=exe
)
