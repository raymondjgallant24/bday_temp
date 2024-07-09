# helpers.py
# these functions generate the random data for testing

import random
import datetime

#generates a random irthday within the dataset
def gen_rand_bday():
    start_date = datetime.date(2013, 1, 1)
    end_date = datetime.date(2014, 12, 31)
    delta = end_date - start_date
    total_days = delta.days
    random_days = random.randint(0, total_days)
    random_date = start_date + datetime.timedelta(days=random_days)
    formatted_date = random_date.strftime("%m/%d/%Y")
    return formatted_date

#generates random latitude values
def gen_lat_values():
    return random.uniform(-90, 90)

#generates random longitude values
def gen_lon_values():
    return random.uniform(-180, 180)

#takes random values of lat, lon, birthday and creates a dictionary of random data 
def gen_test_case():
    test_lat = gen_lat_values()
    test_lon = gen_lon_values()
    test_bday = gen_rand_bday()
    test_case = {
        "name": "Testing",
        "birthday": test_bday,
        "lat": test_lat,
        "lon": test_lon
    }
    return test_case

#generates a list and appends dictionaries full of random data to create a mass amount of test cases
def gen_mass_cases(cases):
    mass_cases = []
    for _ in range(cases):
        test_case = gen_test_case()
        mass_cases.append(test_case)
    return mass_cases
