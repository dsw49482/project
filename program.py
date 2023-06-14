import sys
import json
import yaml
import xml.etree.ElementTree as ET

def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def parse_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def save_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def save_xml(file_path, root):
    tree = ET.ElementTree(root)
    with open(file_path, 'wb') as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: File not found:", file_path)
        return None
    except json.JSONDecodeError as e:
        print("Error parsing JSON file:", str(e))
        return None

def convert_data(input_file_path, output_file_path):
    file_extension = input_file_path.split('.')[-1].lower()

    if file_extension == 'json':
        data = parse_json(input_file_path)
        save_json(output_file_path, data)
    elif file_extension in ['yml', 'yaml']:
        data = parse_yaml(input_file_path)
        save_yaml(output_file_path, data)
    elif file_extension == 'xml':
        root = parse_xml(input_file_path)
        save_xml(output_file_path, root)
    else:
        print(f"Unsupported file format: {file_extension}")
        return

    print(f"Data converted successfully. Saved to {output_file_path}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: program.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        
        json_data = read_json_file(input_file)
        if json_data is not None:
            print("JSON data:")
            print(json_data)
        
        convert_data(input_file, output_file)
