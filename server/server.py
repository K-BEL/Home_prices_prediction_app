from flask_openapi3 import Info, Tag, OpenAPI
from pydantic import BaseModel
import util

# Initialize OpenAPI app
info = Info(title="Home Price Prediction API", version="1.0.0")
app = OpenAPI(__name__, info=info)

# Define tags for categorizing endpoints
state_tag = Tag(name="State", description="Endpoints for retrieving state information")
type_tag = Tag(name="Type", description="Endpoints for retrieving property types")
prediction_tag = Tag(name="Prediction", description="Endpoints for home price prediction")

# Define Pydantic models for input validation
class PredictRequest(BaseModel):
    Lot: float
    State: str
    Type: str
    Bathrooms: int
    Floors: int
    Garages: int
    rooms: int

@app.get("/", summary="Home Page")
def home():
    """
    Welcome to the Home Price Prediction App!
    """
    return "Welcome to the Home Price Prediction App!"

@app.get("/get_State_names", tags=[state_tag], summary="Get State Names")
def get_state_names():
    """
    Retrieve a list of state names.
    """
    return {
        "state": util.get_State_names()
    }

@app.get("/get_Type_names", tags=[type_tag], summary="Get Property Type Names")
def get_type_names():
    """
    Retrieve a list of property type names.
    """
    return {
        "type": util.get_Type_names()
    }

@app.post("/predict_home_price", tags=[prediction_tag], summary="Predict Home Price")
def predict_home_price(body: PredictRequest):
    """
    Predict the home price based on input parameters.
    """
    Lot = body.Lot
    State = body.State
    Type = body.Type
    Bathrooms = body.Bathrooms
    Floors = body.Floors
    Garages = body.Garages
    rooms = body.rooms

    return {
        "estimated_price": util.get_estimated_price(State, Type, Lot, Bathrooms, Floors, Garages, rooms)
    }

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
