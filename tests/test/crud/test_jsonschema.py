from src.constants.apiconstants import apiConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_status_code, verify_json_key_for_not_null
from src.helpers.payload_manager import *
from src.utils.utils import Util

from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json
import pytest
import os
import allure
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestCreateBookingJsonschema:
    
    def load_schema(self, file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description("Creating a Booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_schema_positive(self):
        response = post_request(
            url=apiConstants.url_create_booking(),
            headers=Util().common_headers_json(),
            auth=None,
            payload=payload_create_booking(),
            in_json=False
        )
        logger.info(f"Response Text: {response.text}")
        logger.info(f"Content-Type: {response.headers.get('Content-Type')}")
        logger.info(f"Status Code: {response.status_code}")

        # Validate booking_id
        response_json = None
        try:
            response_json = response.json()
        except json.JSONDecodeError as e:
            logger.error("Failed to parse response as JSON.")
            pytest.fail(f"Response is not valid JSON: {e}")

        booking_id = response_json.get("bookingid")
        verify_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

        # Load and validate schema
        file_path = Path(__file__).parent / "create_booking_schema.json"
        schema = self.load_schema(file_path)
        logger.info(f"Current Directory: {os.getcwd()}")
        logger.info(f"Schema: {schema}")

        try:
            validate(instance=response_json, schema=schema)
            logger.info("JSON schema validation passed.")
        except ValidationError as e:
            logger.error(f"JSON schema validation failed: {e.message}")
            pytest.fail(f"JSON schema validation error: {e.message}")