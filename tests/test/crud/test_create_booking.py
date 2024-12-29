import allure
import pytest
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from src.constants.apiconstants import apiConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_status_code, verify_json_key_for_not_null
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description("Creating a Booking from the paylaod and verfiy that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        response = post_request(url=apiConstants.url_create_booking(), headers=Util().common_headers_json(), auth=None, payload=payload_create_booking(), in_json=False)
        logger.info(f"Response Text: {response.text}")
        logger.info(f"Content-Type: {response.headers.get('Content-Type')}")
        logger.info(f"Status Code: {response.status_code}")


        booking_id = response.json()["bookingid"]
        verify_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

    @pytest.mark.negative
    def test_create_booking_negative(self):
        response=post_request(url=apiConstants.url_create_booking(),headers=Util().common_headers_json(),auth=None, payload={}, in_json=False)
        verify_status_code(response_data=response, expect_data=500)
