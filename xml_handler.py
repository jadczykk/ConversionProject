import xml.etree.ElementTree as ET

def load_xml(path):
    try:
        tree = ET.parse(path)
        root = tree.getroot()

        def xml_to_dict(element):
            data = {}
            if element.attrib:
                data.update(element.attrib)
            for child in element:
                child_data = xml_to_dict(child)
                if child.tag in data:
                    if not isinstance(data[child.tag], list):
                        data[child.tag] = [data[child.tag]]
                    data[child.tag].append(child_data)
                else:
                    data[child.tag] = child_data
            if element.text and element.text.strip():
                data['text'] = element.text.strip()
            return data

        return {root.tag: xml_to_dict(root)}
    except ET.ParseError as e:
        print(f"Błąd składni XML w pliku '{path}': {e}")
        exit(1)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku XML '{path}': {e}")
        exit(1)

def dict_to_xml(tag, data):
    element = ET.Element(tag)

    for key, val in data.items():
        if isinstance(val, dict):
            child = dict_to_xml(key, val)
            element.append(child)
        elif isinstance(val, list):
            for item in val:
                child = dict_to_xml(key, item)
                element.append(child)
        elif key == 'text':
            element.text = str(val)
        else:
            child = ET.Element(key)
            child.text = str(val)
            element.append(child)

    return element

def save_xml(data, path):
    try:
        if len(data) != 1:
            raise ValueError("Dane do zapisania muszą mieć dokładnie jeden korzeń XML.")

        root_tag = list(data.keys())[0]
        root_element = dict_to_xml(root_tag, data[root_tag])

        tree = ET.ElementTree(root_element)
        tree.write(path, encoding='utf-8', xml_declaration=True)
        print(f"Zapisano dane do pliku XML: {path}")
    except Exception as e:
        print(f"Błąd podczas zapisu do pliku XML '{path}': {e}")
        exit(1)
