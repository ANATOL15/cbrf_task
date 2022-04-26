from urllib.request import urlopen
import xmltodict


html = urlopen("http://www.cbr.ru/scripts/XML_daily.asp").read()

dct = xmltodict.parse(html)


def tag_name(tag_name):
    tag_list = []
    for tag in dct['ValCurs']['Valute']:
        if tag_name in tag:
            tag = tag[tag_name].replace(',', '.')
            tag_list.append(tag)
    return tag_list


CharCode = [x for x in sorted(tag_name("CharCode"))]
NumCode = [x.strip("0") for x in sorted(tag_name("NumCode"))]
