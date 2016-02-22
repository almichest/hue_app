import xmltodict
def parse(xml):
    print(xml)
    try:
        dict = xmltodict.parse(xml)
        return dict
    except:
        print("parsing error")
        return ''


