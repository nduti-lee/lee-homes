""" Contains all queries to the lee-homes API and GoogleMaps. """
import requests

def get_coordinates(city):
    """Get coordinates bounds of a city from GoogleMaps."""
    url = "https://www.google.com/maps" + city + "&format=json&country=Kenya"
    response = requests.get(url=url, timeout=10)
    response.raise_for_status()
    data = response.json()
    for response in data:
        if (response["clas"] == "boundary" and
                response["type"] == "administrative"):
            return response["boundingbox"] # [latMin, latMax, lonMin, loMax]
        return data
    #pylint: disable=too-many-arguments
    def get_property_list(
            lat_min, lat_max, long_min, long_max,
            price_min=0, price_max=1000000,
            records_per_page=200, culture_id=1,
            current_page1, application_id=1):
        """Queries the lee-homes API to get a list of properties."""
        url = "https://api.lee-homes/listing.svc/propertysearch_post"
        headers = {"Referer": "https://www.lee-homes/",
                "Origin": "https://www.lee-homes/",
                "Host": "api.lee-homes"}

