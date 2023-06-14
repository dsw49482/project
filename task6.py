import xml.etree.ElementTree as ET

try:
    tree = ET.parse(input_file_path)
    root = tree.getroot()
    # Obsługa danych z pliku XML
except FileNotFoundError:
    print(f'Plik {input_file_path} nie został odnaleziony.')
