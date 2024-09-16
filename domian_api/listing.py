import subprocess
import json


def get_listing(auth_token, listing):
    curl_command = [
        'curl',
        '-X', 'GET',
        f'https://api.domain.com.au/sandbox/v1/listings/{listing}',
        '-H', 'accept: application/json',
        '-H', f'Authorization: Bearer {auth_token}'
    ]

    result = subprocess.run(curl_command, capture_output=True, text=True, check=True)

    if result.stdout.__contains__("""title": "Not Found"""):
        response_data = None
    elif result.stdout.__contains__("""title": "Quota Exceeded"""):
        response_data = None

    else:
        response_data = json.loads(result.stdout)

    return response_data


def get_listing_offline(response):
    if response.__contains__("""title": "Not Found"""):
        response_data = None
    elif response.__contains__("""title": "Quota Exceeded"""):
        response_data = None

    else:
        response_data = json.loads(response)

    return response_data
