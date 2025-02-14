import json
import numpy as np
import pickle

# Load the model and columns
__model = None
__data_columns = None
__locations = None

def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    with open("columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]  # Extract location names

    with open("banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

def get_location_names():
    return __locations

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower()) if location.lower() in __data_columns else -1
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

load_saved_artifacts()
