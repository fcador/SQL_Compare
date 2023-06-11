import os
import csv
import re
import tkinter as tk
from tkinter import filedialog
from sqlparse import parse

def main():
    # Demander à l'utilisateur d'entrer les chemins des fichiers SQL
    file_path_a = choose_open_file()
    file_path_b = choose_open_file()

    # Vérifier si les fichiers existent
    if not os.path.exists(file_path_a) or not os.path.exists(file_path_b):
        print("L'un ou les deux fichiers n'existent pas.")
        return

    # Lire le contenu des fichiers SQL
    with open(file_path_a, 'r') as file_a, open(file_path_b, 'r') as file_b:
        sql_a = file_a.read()
        sql_b = file_b.read()

    # Analyser les fichiers SQL
    statements_a = parse(sql_a)
    statements_b = parse(sql_b)

    # Vérifier si les fichiers contiennent des données
    if contains_data(statements_a) or contains_data(statements_b):
        print("Les fichiers contiennent des requêtes d'insertion de données. Veuillez vous assurer qu'ils contiennent uniquement la structure de la base de données.")
        return

    # Extraire les schémas des fichiers SQL
    schema_a = extract_schema(statements_a)
    schema_b = extract_schema(statements_b)

    # Comparez les schémas des modèles A et B
    compare_schemas(schema_a, schema_b)

def compare_schemas(schema_a, schema_b):
    differences = []

    # Vérifier les tables existantes dans A mais non présentes dans B
    for table_name in schema_a:
        if table_name not in schema_b:
            differences.append((table_name, "", "", f"La table '{table_name}' existe dans le modèle source mais n'est pas présente dans le modèle de destination."))

    # Vérifier les tables avec des différences de champs entre A et B
    for table_name in schema_a:
        if table_name in schema_b:
            columns_a = schema_a[table_name]
            columns_b = schema_b[table_name]

            if columns_a != columns_b:
                differences.append((table_name, "", "", f"La table '{table_name}' a des différences de champs entre le modèle source et le modèle de destination."))

    # Vérifier les différences de paramètres de champs entre A et B
    for table_name in schema_a:
        if table_name in schema_b:
            columns_a = schema_a[table_name]
            columns_b = schema_b[table_name]

            for column in columns_a:
                column_name, params_a = column
                found_column = False

                for b_column in columns_b:
                    b_column_name, params_b = b_column

                    if column_name == b_column_name:
                        found_column = True

                        if params_a != params_b:
                            differences.append((table_name, column_name, params_a, f"La table '{table_name}', le champ '{column_name}' a des différences de paramètres entre le modèle source et le modèle de destination."))

                if not found_column:
                    differences.append((table_name, column_name, params_a, f"La table '{table_name}', le champ '{column_name}' existe dans le modèle source mais n'est pas présent dans le modèle de destination."))

    # Écrire les différences dans un fichier CSV
    file_path = choose_save_file_path()
    if not file_path:
        print("Aucun emplacement de fichier sélectionné.")
        return

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Table", "Champ", "Paramètres", "Différence"])
        writer.writerows(differences)

    print("Le rapport des différences a correctement été enregistré.")

def extract_schema(statements):
    schema = {}

    for statement in statements:
        if statement.get_type() == 'CREATE':
            table_name = None
            columns = []

            # Recherche du nom de la table
            match = re.search(r"CREATE\s+TABLE\s+`([^`]+)`", statement.value, re.IGNORECASE)
            if match:
                table_name = match.group(1)

            # Recherche des champs composant la table
            match_columns = re.search(r"\((.+)\)", statement.value, re.DOTALL)
            if match_columns:
                columns_str = match_columns.group(1)
                columns_list = columns_str.split(',')

                for column in columns_list:
                    column = column.strip()

                    # Exclusion de tokens spécifiques
                    # TODO exclusion de tout ce qui ne se trouve pas entre simple quotes
                    if re.search(r"(PRIMARY KEY|UNIQUE KEY|KEY|CONSTRAINT)", column):
                        continue

                    match_column = re.search(r"`([^`]+)`\s+([^,]+)", column)
                    if match_column:
                        column_name = match_column.group(1)
                        column_params = match_column.group(2).strip()
                        columns.append((column_name, column_params))

            if table_name:
                schema[table_name] = columns

    return schema


def contains_data(statements):
    for statement in statements:
        if statement.get_type() == 'INSERT':
            return True
    return False

def choose_save_file_path():
    root = tk.Tk()
    root.withdraw()  # Cache la fenêtre principale de tkinter

    file_path = filedialog.asksaveasfilename(
        defaultextension='.csv',
        filetypes=[('CSV files', '*.csv')],
        title='Choisir un emplacement pour votre fichier de différences'
    )

    return file_path

def choose_open_file():
    root = tk.Tk()
    root.withdraw()  # Cache la fenêtre principale de tkinter

    file_path = filedialog.askopenfilename(
        filetypes=[('SQL files', '*.sql')],
        title='Choisir un fichier SQL à comparer'
    )

    return file_path



if __name__ == "__main__":
    main()
