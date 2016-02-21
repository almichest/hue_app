import xmltodict
def parse(xml):
    try:
        dict = xmltodict.parse(xml)
        return dict
    except:
        print("parsing error")
        print(xml)
        return ''


