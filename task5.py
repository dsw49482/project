import yaml

try:
    with open(output_file_path, 'w') as file:
        yaml.dump(data, file)
        print(f'Dane zostały zapisane do pliku {output_file_path}.')
except FileNotFoundError:
    print(f'Nie można zapisać danych do pliku {output_file_path}.')
