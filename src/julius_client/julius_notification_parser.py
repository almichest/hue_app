import xmltodict
def parse(xml):
    print(xml)
    dict = xmltodict.parse(xml)
    return dict

