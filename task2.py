import json

try:
    with open(input_file_path, 'r') as file:
        data = json.load(file)
        # Obsługa danych z pliku JSON
except FileNotFoundError:
    print(f'Plik {input_file_path} nie został odnaleziony.')
