import requests


def assert_equal(left_part, right_part, message, soft_assert=False):
    try:
        assert left_part == right_part, message
    except AssertionError as err:
        if not soft_assert:
            raise err


def assert_in(left_part, right_part, soft_assert=False):
    check = any(item in left_part for item in right_part)
    try:
        assert check
    except AssertionError as err:
        if not soft_assert:
            raise err

def isint(expected_value):
    for nummber in expected_value:
        try:
            int(nummber)
            return True
        except ValueError:
            return False

def check_status_code(response: requests.Response, expected_code: int):
    error_message = f"Actual status code '{response.status_code}' not equal expected status code '{expected_code}'"
    assert_equal(left_part=response.status_code, right_part=expected_code, message=error_message)


def check_field_equals(field, expected_value, assertion_message='Invalid field value'):
    assert field == expected_value, assertion_message


def assert_in_list(left_part, right_part, soft_assert=False):
    assert_in(left_part, right_part, soft_assert)

def assert_number_is_int(expected_value):
    isint(expected_value)
