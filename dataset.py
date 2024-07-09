# dataset.py
# this function loads the chose dataset

import xarray as xr

def load_dataset():
    ds = xr.tutorial.load_dataset("air_temperature")
    return ds
