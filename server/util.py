import pickle
import json
import numpy as np

__state = None
__type = None
__data_columns = None
__model = None

def get_estimated_price(State,Type, Lot, Bathrooms, Floors, Garages, rooms):
    try:
        loc_index = __data_columns.index(State.lower())
    except:
        loc_index = -1
    try:
        type_index = __data_columns.index(Type.lower())
    except:
        type_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Lot
    
    x[1] = Bathrooms
    x[2] = Floors
    x[3] = Garages
    x[4] = rooms
    if loc_index >= 0:
        x[loc_index] = 1
    if type_index >= 0:
        x[type_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __state
    global __type

    with open(r"C:\Users\k.belhadj\Desktop\Repos\Home_prices_prediction_app\model\columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __state = __data_columns[3:] 
        __type = __data_columns[3:] 

    global __model
    if __model is None:
        with open(r'C:\Users\k.belhadj\Desktop\Repos\Home_prices_prediction_app\model\germany_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_State_names():
    return __state
def get_Type_names():
    return __type

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_State_names())
    print(get_Type_names())
    print(get_estimated_price('Hessen','Mid-terrace house',300, 3, 3,2,2))