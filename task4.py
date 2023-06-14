import yaml

try:
    with open(input_file_path, 'r') as file:
        data = yaml.safe_load(file)
        # Obsługa danych z pliku YAML
except FileNotFoundError:
    print(f'Plik {input_file_path} nie został odnaleziony.')
