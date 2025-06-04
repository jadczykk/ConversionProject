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
