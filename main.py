from domian_api.authenticate import get_credentials
from domian_api.listing import get_listing
from data_model.property_data import Property
import json

import csv

if __name__ == '__main__':
    credentials = get_credentials()

    listing_ids = 'listings.csv'

    results = []

    with open(listing_ids, mode='r') as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            property_data = get_listing(credentials.access_token, row['id'])
            print(row['id'], property_data)
            if property_data is None:
                pass
            else:
                results.append(Property(**property_data))

    with open("results2.json", 'w') as file:
        json.dump(results, file, indent=2)


