import argparse
import json
import yaml
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji danych')
    parser.add_argument('input_file', help='Ścieżka pliku wejściowego')
    parser.add_argument('output_file', help='Ścieżka pliku wyjściowego')
    return parser.parse_args()

def load_json(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'Plik {input_file_path} nie został odnaleziony.')

def save_json(data, output_file_path):
    try:
        with open(output_file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f'Dane zostały zapisane do pliku {output_file_path}.')
    except FileNotFoundError:
        print(f'Nie można zapisać danych do pliku {output_file_path}.')

def load_yaml(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f'Plik {input_file_path} nie został odnaleziony.')

def save_yaml(data, output_file_path):
    try:
        with open(output_file_path, 'w') as file:
            yaml.dump(data, file)
            print(f'Dane zostały zapisane do pliku {output_file_path}.')
    except FileNotFoundError:
        print(f'Nie można zapisać danych do pliku {output_file_path}.')

def load_xml(input_file_path):
    try:
        tree = ET.parse(input_file_path)
        return tree.getroot()
    except FileNotFoundError:
        print(f'Plik {input_file_path} nie został odnaleziony.')

def save_xml(root, output_file_path):
    try:
        tree = ET.ElementTree(root)
        tree.write(output_file_path)
        print(f'Dane zostały zapisane do pliku {output_file_path}.')
    except FileNotFoundError:
        print(f'Nie można zapisać danych do pliku {output_file_path}.')

def main():
    args = parse_arguments()

    # Rozpoznawanie formatu pliku wejściowego
    if args.input_file.endswith('.json'):
        data = load_json(args.input_file)
    elif args.input_file.endswith(('.yml', '.yaml')):
        data = load_yaml(args.input_file)
    elif args.input_file.endswith('.xml'):
        root = load_xml(args.input_file)
    else:
        print('Nieobsługiwany format pliku wejściowego.')
        return

    # Konwersja i zapis danych do pliku wyjściowego
    if args.output_file.endswith('.json'):
        save_json(data, args.output_file)
    elif args.output_file.endswith(('.yml', '.yaml')):
        save_yaml(data, args.output_file)
    elif args.output_file.endswith('.xml'):
        save_xml(root, args.output_file)
    else:
        print('Nieobsługiwany format pliku wyjściowego.')

if __name__ == '__main__':
    main()
