 LEE HOMES REAL ESTATE 
 
 Python scraper for Lee Homes real estate website. Use it to scrape real-estate listings easily.

INSTALLATION

Use the package manager pip to install the package requirements.

pip install git+https://github.com/nduti-lee/lee-homes.git

Local Development
git clone https://github.com/nduti-lee/lee-homes.git
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt

CONTEXT

PropertySearch_Post and PropertyDetails are two of Lee Homes' API endpoints. A list of properties in a .json format, along with some sparse details, will be returned by querying PropertySearch_Post. Each property's specific information can be found by executing a query on PropertyDetails. You can query either one, depending on what you're looking for, but be aware that it takes time to get information about each property. Lee Homes has a rate cap, which is a bummer. An Error 403: Unauthorized error will be returned if you submit too many queries too frequently. Uncertainty regarding the rate limit prevents the freeze-out, but waiting approximately ten minutes between limits does.

USAGE

In queries.py you will find queries to Lee Homes for both the PropertySearch_Post endpoint and the PropertyDetails endpoint. It also contains a query to get the coordinate bounding box of a city, as that's what Lee Homes uses to determine which properties to list.

In lee-homes.py there are two functions to automate the scraping of Lee Homes.
 
AUTHOR

Ashley Linda 
<https://github.com/nduti-lee>

LICENSE

