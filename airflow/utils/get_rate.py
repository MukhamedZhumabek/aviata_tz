def get_rate_to_tenge(currency: str, tree: str):
    for child in tree:
        if 'title' in child.attrib and child.attrib["title"] == currency:
            return child.attrib["description"]
    return None