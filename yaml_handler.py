import yaml

def load_yaml(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print(f"Błąd składni YAML w pliku '{path}': {e}")
        exit(1)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku YAML '{path}': {e}")
        exit(1)


def save_yaml(data, path):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True, default_flow_style=False)
        print(f"Zapisano dane do pliku YAML: {path}")
    except Exception as e:
        print(f"Błąd podczas zapisu do pliku YAML '{path}': {e}")
        exit(1)
