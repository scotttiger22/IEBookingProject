import allure
import pytest
import requests
from pydantic import ValidationError
from core.models.booking import BookingResponse
import requests
from requests.exceptions import HTTPError



@allure.feature('Test Create Booking')
@allure.story('Test creating booking with random data')
def test_create_booking_with_random_data(api_client, generate_random_booking_data):
    response = api_client.create_booking(booking_data=generate_random_booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")

    assert response['booking']['firstname'] == generate_random_booking_data['firstname']
    assert response['booking']['lastname'] == generate_random_booking_data['lastname']
    assert response['booking']['totalprice'] == generate_random_booking_data['totalprice']
    assert response['booking']['depositpaid'] == generate_random_booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == generate_random_booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == generate_random_booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == generate_random_booking_data['additionalneeds']

@allure.feature('Test Create Booking')
@allure.story('Test creating booking with custom data')
def test_create_booking_with_custom_data(api_client):
    booking_data = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2026-01-01",
        "checkout" : "2026-03-21"
    },
    "additionalneeds" : "Breakfast"
}
    response = api_client.create_booking(booking_data=booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test Create Booking')
@allure.story('Test creating booking with false name data')
def test_create_booking_with_false_name_data(api_client):
    false_booking_data = {
    "firstname" : 111,
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2019-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

    with pytest.raises(HTTPError) as e:
        response = api_client.create_booking(booking_data=false_booking_data)

        assert response.status_code == 500, f"Expected status 200 but got {response.status_code}"
        assert str(e.value) == '500 Server Error'

@allure.feature('Test Create Booking')
@allure.story('Test creating booking with null data')
def test_create_booking_with_null_data(api_client):
    false_booking_data = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : None,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2019-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    with pytest.raises(HTTPError) as e:
        response = api_client.create_booking(booking_data=false_booking_data)

        assert response.status_code == 500, f"Expected status 200 but got {response.status_code}"
        assert str(e.value) == '500 Server Error'

@allure.feature('Test Create Booking')
@allure.story('Test creating booking with no name data')
def test_create_booking_with_no_name_data(api_client):
    booking_data_no_name = {
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "01-02-2026",
        "checkout" : "2026-03-21"
    },
    "additionalneeds" : "Breakfast"
}
    with pytest.raises(HTTPError) as e:
        response = api_client.create_booking(booking_data=booking_data_no_name)

        assert response.status_code == 500, f"Expected status 200 but got {response.status_code}"
        assert str(e.value) == '500 Server Error'