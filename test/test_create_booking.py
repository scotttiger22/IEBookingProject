import allure
import pytest
import requests
import jsonschema

from core.settings.bookingschemas import CREATE_SCHEMA


@allure.feature('Test Ping')
@allure.story('Test create booking')
def test_create_booking(api_client, generate_random_booking_data):
    response_json = api_client.create_booking(booking_data=generate_random_booking_data)
    jsonschema.validate(response_json, CREATE_SCHEMA)
