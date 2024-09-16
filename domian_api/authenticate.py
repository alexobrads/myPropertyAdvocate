import subprocess
import json
from data_model.credential_data import Credentials


def get_credentials():
    # Read the configuration from the file
    with open('credentials.json', 'r') as config_file:
        config_data = json.load(config_file)

    # Access the variables
    client_id = config_data['client_id']
    client_secret = config_data['client_secret']

    curl_command = [
        'curl',
        '-X', 'POST', '-u',
        f'{client_id}:{client_secret}',
        '-H', 'Content-Type: application/x-www-form-urlencoded',
        '-d', 'grant_type=client_credentials&scope=api_listings_read',
        'https://auth.domain.com.au/v1/connect/token'
    ]

    try:
        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        response_data = json.loads(result.stdout)
        return Credentials(
            access_token=response_data['access_token'],
            expires_in=response_data['expires_in'],
            token_type=response_data['token_type'],
            scope=response_data['scope']
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None
