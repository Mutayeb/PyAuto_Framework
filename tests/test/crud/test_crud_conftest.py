
import allure
import pytest
import json
import logging

from src.constants.apiconstants import apiConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

class TestCrudBooking():

    @allure.title("Test CRUD operation Update(PUT)")
    @allure.description("Verify that Full Update with the booking ID and Token is working.")
    def test_update_booking_id_token(self,create_token,get_booking):
        booking_id=get_booking_id
        token=create_token
        response=put_request(
            url=apiConstants().url_patch_put_delete(booking_id=booking_id),
            headers=Util().header_put_delete_patch_cookie(token=token),
            auth=None,
            payload=payload_create_booking(),
            in_json=False
        )
        verify_status_code(response_data=response,expect_data=200)
        verify_response_key_should_not_be_none(key=response.json()["firstname"])
        verify_response_key_should_not_be_none(key=response.json()["lastname"])
        verify_response_key(key=response.json()["firstname"],expected_data="Manasa")
        verify_response_key(key=response.json()["lastname"],expected_data="P.")
    
    @allure.title("Test CRUD operation Delete(DELETE)")
    @allure.description("Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id_token(self,create_token,get_booking):
        logging.basicConfig(level=logging.INFO)
        logger=logging.getLogger(__name__)
        booking_id=get_booking
        token=create_token
        response=delete_request(
            url=apiConstants().url_patch_put_delete(booking_id=booking_id),
            headers=Util().header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        logger.info(f"Response Text :" +response)
        verify_status_code(response_data=response,expect_data=201)

        verify_response_delete(response=response.text)
