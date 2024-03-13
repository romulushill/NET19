import numpy as np
import tensorflow as tf
from modules.datastore import Data
from datetime import datetime

# Sample data - features of cars and their corresponding labels (0 for non-criminal, 1 for criminal)
# Each row represents a car, and each column represents a feature

data = Data()


features_array = []
labels_array = []

for element in data.training_data:
    features_array.append([element["colour"],element["damaged"],element["speeding"],element["gender"],element["size"]])
    labels_array.append([element["criminal"]])

features = np.array(features_array)
labels = np.array(labels_array)  # Labels for the corresponding cars

""" features = np.array(
    [
        [0.2, 0.3, 0.5],  # Innocent car 1
        [0.4, 0.4, 0.6],  # Criminal car 2
        [0.1, 0.5, 0.4],  # Innocent car 3
        [0.7, 0.8, 0.2],  # Criminal car 4
    ]
) """


# Define the neural network architecture
model = tf.keras.Sequential(
    [
        tf.keras.layers.Dense(4, activation="relu", input_shape=(5,)),
        tf.keras.layers.Dense(4, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ]
)
# tf.keras.layers.Dense(outputs, activation="relu", input_shape=(number_of_inputs,)),


# Compile the model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(features, labels, epochs=100, batch_size=1)
current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = str(current_datetime.strftime("%H.%M.%S"))
model.save_weights(f"weightings-{formatted_date}-{formatted_time}.h5")

# Function to predict if a car is criminal
def predict_criminal_car(car_properties):
    # car_properties is a dictionary containing the properties of the car
    # Convert the dictionary to a numpy array
    car_features = np.array(
        [
            car_properties["colour"],
            car_properties["damaged"],
            car_properties["speeding"],
            car_properties["gender"],
            car_properties["size"],
        ]
    )
    # Reshape the array to match the input shape of the model
    car_features = np.reshape(car_features, (1, 5))
    # Predict the probability of the car being criminal
    probability = model.predict(car_features)[0][0]
    # If the probability is greater than 0.5, classify as criminal
    if probability > 0.5:
        return True
    else:
        return False


# Example input dictionary for car properties
car_properties = {"colour": 0.6, "damaged": 0.7, "speeding": 0.3, "gender":0.2,"size":0.9}

# Predict if the car is criminal
is_criminal = predict_criminal_car(car_properties)
print("Is the car criminal?", is_criminal)
