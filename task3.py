import json

try:
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print(f'Dane zostały zapisane do pliku {output_file_path}.')
except FileNotFoundError:
    print(f'Nie można zapisać danych do pliku {output_file_path}.')
