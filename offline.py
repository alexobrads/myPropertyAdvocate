from data_handling.data_loader import load_to_elastic
from data_handling.data_loader import create_geo_index
from data_model.property_data import Property, GeoLocation
import json
from dataclasses import asdict
from domian_api.listing import get_listing_offline

if __name__ == '__main__':

    results = []

    with open("examples.json", 'r') as file:
        data = json.load(file)

        for row in data:

            property_data = get_listing_offline(json.dumps(row))

            if property_data is None:
                pass
            else:

                if 'geoLocation' in property_data and 'latitude' in property_data['geoLocation']:
                    property_data['geoLocation']['lat'] = property_data['geoLocation'].pop('latitude')

                if 'geoLocation' in property_data and 'longitude' in property_data['geoLocation']:
                    property_data['geoLocation']['lon'] = property_data['geoLocation'].pop('longitude')

                results.append(Property(**property_data))

    property_dicts = [asdict(prop) for prop in results]

    create_geo_index()
    load_to_elastic(property_dicts)








