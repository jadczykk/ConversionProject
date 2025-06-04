import sys
import os
from json_handler import load_json
from json_handler import save_json

def parse_arguments():
    if len(sys.argv) != 3:
        print("Użycie: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isfile(input_path):
        print(f"Błąd: plik wejściowy '{input_path}' nie istnieje.")
        sys.exit(1)

    supported_extensions = ('.json', '.xml', '.yml', '.yaml')

    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in supported_extensions or output_ext not in supported_extensions:
        print("Błąd: obsługiwane formaty to .json, .xml, .yml, .yaml")
        sys.exit(1)

    return input_path, output_path, input_ext, output_ext

if __name__ == "__main__":
    input_file, output_file, input_ext, output_ext = parse_arguments()
    print("Plik wejściowy:", input_file)
    print("Plik wyjściowy:", output_file)
    print("Format wejściowy:", input_ext)
    print("Format wyjściowy:", output_ext)
    if input_ext == ".json":
        data = load_json(input_file)
        print("Poprawnie wczytano dane JSON:")
        print(data)
    if output_ext == ".json":
        save_json(data, output_file)
        print("Poprawnie zapisano dane JSON do pliku:", output_file)
