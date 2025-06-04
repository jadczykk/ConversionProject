import json

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Błąd składni JSON w pliku '{path}': {e}")
        exit(1)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku JSON '{path}': {e}")
        exit(1)


def save_json(data, path):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Zapisano dane do pliku JSON: {path}")
    except Exception as e:
        print(f"Błąd podczas zapisu do pliku JSON '{path}': {e}")
        exit(1)