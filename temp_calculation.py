# temp_calculation.py

import pandas as pd

# subsets data by the user input parameters and outputs the air temperature on the users birthday
def get_birthday_temp(ds, test_case):
    date = pd.to_datetime(test_case['birthday'])
    temp_at_location = ds.sel(lat=float(test_case['lat']), lon=float(test_case['lon']), method='nearest')
    temp_on_date = temp_at_location.sel(time=date, method='nearest')
    air_temp = temp_on_date['air'].item()
    air_temp = (air_temp - 273.15) * 1.8 + 32  # Convert from Kelvin to Fahrenheit
    return air_temp
