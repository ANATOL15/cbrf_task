import os
from lxml import etree
import lxml
import requests

XML_daily_quotes = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").content
XML_currency_code_guide = requests.get("http://www.cbr.ru/scripts/XML_val.asp").content
XML_ISO_codes = requests.get("http://www.cbr.ru/scripts/XML_valFull.asp").content
XSD_daily_quotes = "C:/Users/HONOR/PycharmProjects/my_currency/ValCurs.xsd"
XSD_currency_code_guide = "C:/Users/HONOR/PycharmProjects/my_currency/Valuta.xsd"
XSD_ISO_codes = "C:/Users/HONOR/PycharmProjects/my_currency/XML_valFull.xsd"


def daily_currrency_validation(XML, XSD):
    with open('file.asp', 'wb') as foutput:
        foutput.write(XML)
    xml_file = lxml.etree.parse("file.asp")
    xml_validator = lxml.etree.XMLSchema(file=XSD)
    is_valid = xml_validator.validate(xml_file)
    os.remove("file.asp")
    return is_valid


print(daily_currrency_validation(XML_daily_quotes, XSD_daily_quotes))
print(daily_currrency_validation(XML_currency_code_guide, XSD_currency_code_guide))
print(daily_currrency_validation(XML_ISO_codes, XSD_ISO_codes))