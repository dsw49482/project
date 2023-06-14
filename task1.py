import argparse

parser = argparse.ArgumentParser(description='Program do konwersji danych')
parser.add_argument('input_file', help='Ścieżka pliku wejściowego')
parser.add_argument('output_file', help='Ścieżka pliku wyjściowego')
args = parser.parse_args()

input_file_path = args.input_file
output_file_path = args.output_file
