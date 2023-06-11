from cx_Freeze import setup, Executable

# Paramètres de l'exécutable
executables = [Executable("sql_compare.py")]

# Options de configuration
build_options = {
    'build_exe': {
        'packages': [],
        'excludes': [],
        'include_files': []
    }
}

# Configuration du setup
setup(
    name="SQL Compare",
    version="1.0",
    description="Outil de comparaison de 2 schémas MySQL",
    options=build_options,
    executables=executables
)

