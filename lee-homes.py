"""Wrapper the queries module to get property data from lee-lomes."""
from time import sleep
from math import ceil
import os
from random import randint
from requests import HTTPError
import pandas as pd
from queries import get_coordinates, get_property_list, get_property_details

def get_property_list_by_city(city):
    """Get a list of properties for a given city, and return it as a cvs file."""
    cords = get_coordinates(city) 
    max_pages = 1
    current_page = 1
    filename = city.replace(" ","").replace(",","") + ".csv"
