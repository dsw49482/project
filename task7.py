import xml.etree.ElementTree as ET

try:
    tree = ET.ElementTree(root)  # root to wcześniej wczytany element
    tree.write(output_file_path)
    print(f'Dane zostały zapisane do pliku {output_file_path}.')
except FileNotFoundError:
    print(f'Nie można zapisać danych do pliku {output_file_path}.')
