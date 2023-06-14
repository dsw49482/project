# Task1: parsowanie argumentów przekazywanych przy uruchomieniu programu
import sys

def parse_arguments():
    if len(sys.argv) < 3:
        print("Usage: program.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    return input_file, output_file


# Task2: wczytywanie danych z pliku JSON
import json

def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Task3: zapis danych do pliku w formacie JSON
def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


# Task4: wczytywanie danych z pliku YAML
import yaml

def parse_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data


# Task5: zapis danych do pliku w formacie YAML
def save_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)


# Task6: wczytywanie danych z pliku XML
import xml.etree.ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root


# Task7: zapis danych do pliku w formacie XML
def save_xml(file_path, root):
    tree = ET.ElementTree(root)
    with open(file_path, 'wb') as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)


# Główna funkcja programu
def convert_data(input_file_path, output_file_path):
    file_extension = input_file_path.split('.')[-1].lower()

    if file_extension == 'json':
        # Task2: wczytywanie danych z pliku JSON
        data = parse_json(input_file_path)
        # Task3: zapis danych do pliku w formacie JSON
        save_json(output_file_path, data)
    elif file_extension in ['yml', 'yaml']:
        # Task4: wczytywanie danych z pliku YAML
        data = parse_yaml(input_file_path)
        # Task5: zapis danych do pliku w formacie YAML
        save_yaml(output_file_path, data)
    elif file_extension == 'xml':
        # Task6: wczytywanie danych z pliku XML
        root = parse_xml(input_file_path)
        # Task7: zapis danych do pliku w formacie XML
        save_xml(output_file_path, root)
    else:
        print(f"Unsupported file format: {file_extension}")
        return

    print(f"Data converted successfully. Saved to {output_file_path}")


if __name__ == '__main__':
    input_file, output_file = parse_arguments()
    convert_data(input_file, output_file)
