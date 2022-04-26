import json

import requests
from xml.dom import minidom

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

dom = minidom.parseString(response.text)
dom.normalize()
elements = dom.getElementsByTagName("Valute")

def XML_daily_data():
    currency_dict = {}
    value_list = []
    CharCode = []
    NumCode = []
    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Value':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                        value_list.append(child.firstChild.data.replace(',', '.'))
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
                        CharCode.append(child.firstChild.data)
                if child.tagName == 'NumCode':
                    if child.firstChild.nodeType == 3:
                        NumCode.append(child.firstChild.data)
        currency_dict[char_code] = value
    return json.dumps(currency_dict, indent=2)


CharCode = XML_daily_data()
print(CharCode)
