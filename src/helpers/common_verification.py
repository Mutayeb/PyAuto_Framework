def verify_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Failed! Expected HTTP Status Code " + str(expect_data)

def verify_json_key_for_not_null(key):
    assert key is not None, "Failed-Key is Empty"
    assert key != 0, "Failed-Key is 0"
    assert key > 0, "Failed-Key is not greater than 0"


def verify_json_key_for_not_null_token(key):
    assert key is not None, "Failed-Key is Empty"

def key_not_null(key):  # null-check for all the fields in response e.g., first_name, last_name, Id...
    assert key is not None, "Failed-Key is None"