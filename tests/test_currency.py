from cbrf_task.data.ISO_example import *
from cbrf_task.data.daily_example import CharCode, NumCode
from cbrf_task.asserts import *

def test_check():
    response1 = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    check_status_code(response=response1, expected_code=200)

def test_assert_CharCode_valid():
    assert_in_list(ISO_Char_Code, CharCode)

def test_assert_Num_Code_valid():
    assert_in_list(ISO_Num_Code, NumCode)

def test_number_is_int():
    assert_number_is_int(NumCode)
