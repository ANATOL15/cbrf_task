from urllib.request import urlopen
import xmltodict

html = urlopen("http://www.cbr.ru/scripts/XML_valFull.asp").read()
dct = xmltodict.parse(html)

def XML_data(tag_name):
    tag_list = []
    for tag in dct['Valuta']['Item']:
        if tag_name in tag:
            tag = tag[tag_name]
            tag_list.append(tag)
    return tag_list

ISO_Char_Code = sorted(list(filter(lambda x: type(x) is str, XML_data(('ISO_Char_Code')))))
ISO_Num_Code = sorted(filter(lambda x: type(x) is str, XML_data(('ISO_Num_Code'))))


