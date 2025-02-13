# payloads
# dict ->
from faker import Faker
import json

faker = Faker()

def payload_create_booking():
    payload = {
        "firstname": "Manasa",
        "lastname": "P.",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_booking_dynamic():
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "WiFi", "Extra Bed"))
    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

def payload_patch_booking():
    payload = {
        "firstname": "Drithi"
    }
    return payload

def payload_update_booking():
    payload = {
        "firstname": "Drithi",
        "lastname": "Potu",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload