import sys
import json
import yaml
import xml.etree.ElementTree as ET


def parse_json(file_path):
    try:
        with open(file_path, 'r') as file:
            json_str = file.read()
            if not json_str.strip():
                print(f"Error: File is empty: {file_path}")
                return None
            data = json.loads(json_str)
        return data
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {str(e)}\nJSON String: {json_str}")
        return None
    except Exception as e:
        print(f"Error parsing JSON file: {str(e)}")
        return None


def save_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving JSON file: {str(e)}")


def parse_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {str(e)}")
        return None
    except Exception as e:
        print(f"Error parsing YAML file: {str(e)}")
        return None


def save_yaml(file_path, data):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
    except Exception as e:
        print(f"Error saving YAML file: {str(e)}")


def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML file: {str(e)}")
        return None
    except Exception as e:
        print(f"Error parsing XML file: {str(e)}")
        return None


def save_xml(file_path, root):
    try:
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as e:
        print(f"Error saving XML file: {str(e)}")


def convert_data(input_file_path, output_file_path):
    file_extension = input_file_path.split('.')[-1].lower()

    if file_extension != 'json':
        print(f"Unsupported file format: {file_extension}")
        return

    data = parse_json(input_file_path)
    if data is not None:
        save_json(output_file_path, data)

    print(f"Data converted successfully. Saved to {output_file_path}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: program.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_data(input_file, output_file)
