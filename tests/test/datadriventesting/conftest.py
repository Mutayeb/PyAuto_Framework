import allure
import pytest

from src.constants.apiconstants import apiConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


@pytest.fixture(scope="session")
def create_token(self):
    response = post_request(
        url=apiConstants.url_create_token(),
        headers=Util().common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json=False)
    token = response.json()["token"]
    verify_json_key_for_not_null_token(key=token)
    verify_status_code(response_data=response, expect_data=200)
    return token

@pytest.fixture(scope="session")
def get_booking(self):
    response = post_request(
        url=apiConstants.url_create_booking(),
        headers=Util().common_headers_json(),
        auth=None,
        payload=payload_create_booking(),
        in_json=False)
    booking_id = response.json()["bookingid"]
    verify_json_key_for_not_null(key=booking_id)
    verify_status_code(response_data=response, expect_data=200)
    return booking_id


@pytest.fixture(scope="session")
def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(filename=file_path) #The load_workbook() function opens file for reading
    sheet1 = workbook.active #The object of the workbook.active has been created in the script to read the values of the max_row and the max_column properties.
    #for loop to read each row from the excel sheet
    for row in sheet1.iter_rows(min_row=2,values_only=True):
        username,password = row
        credentials.append({"username":username,
                            "password":password})
    return credentials

