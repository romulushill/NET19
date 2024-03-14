import numpy as np
import tensorflow as tf
from modules.training import Training
from datetime import datetime

# Sample data - features of cars and their corresponding labels (0 for non-criminal, 1 for criminal)
# Each row represents a car, and each column represents a feature

# Define the neural network architecture

class Main:
    def __init__(self):
        self.trainer = Training(
            database_reference="./resources/datastore.json", aspects_reference=["darkness", "damaged", "speeding", "gender", "size"], result_reference = "criminal"
        )
        self.model = self.trainer.train()

    # Prediction Function
    def predict_criminal_car(self, car_properties):
        # Make dict into numpy array
        car_features = np.array(
            [
                car_properties["darkness"],
                car_properties["damaged"],
                car_properties["speeding"],
                car_properties["gender"],
                car_properties["size"],
            ]
        )
        # Reshaping Procedure for the array to fit the model
        car_features = np.reshape(car_features, (1, 5))
        # Predict the probability of the car being criminal
        probability = self.model.predict(car_features)[0][0]
        # If the probability is greater than 0.5, classify as criminal
        if probability > 0.5:
            return True
        else:
            return False


network = Main()

# Example input dictionary for car properties
car_properties = {"darkness": 0.6, "damaged": 0.7, "speeding": 0.3, "gender":0.2,"size":0.9}

# Predict if the car is criminal
is_criminal = network.predict_criminal_car(car_properties)
print("Is the car criminal?", is_criminal)
