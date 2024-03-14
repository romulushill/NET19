import numpy as np
import tensorflow as tf
from modules.training import Training
from modules.graphing import Application
from datetime import datetime
import random
import json
import os
# Sample data - features of cars and their corresponding labels (0 for non-criminal, 1 for criminal)
# Each row represents a car, and each column represents a feature

# Define the neural network architecture

class Main:
    def __init__(self, aspects_reference=["darkness", "damaged", "speeding", "gender", "size"]):

        self.aspects_reference = aspects_reference
        self.trainer = Training(
            database_reference="./resources/datastore.json", aspects_reference=self.aspects_reference, result_reference = "criminal"
        )
        self.model = self.trainer.train()
        self.app = Application(number_of_nodes=len(self.trainer.data))

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
        car_features = np.reshape(car_features, (1, len(self.aspects_reference)))
        # Predict the probability of the car being criminal
        probability = self.model.predict(car_features)[0][0]
        # If the probability is greater than 0.5, classify as criminal
        if probability > 0.5:
            return True
        else:
            return False


network = Main()


with open("./resources/datastore.json", "r") as fp:
    contents = json.load(fp)
    datastore = contents["Dataset"]


while True:
    try:
        choice = input("[T] Test. [Q] Quit.\n")
        if choice.lower() == "t":
            manual = input("[M] Manual. [A] Automatic.\n")
            if manual.lower() == "m":
                darkness_input = input("Darkness --> ")
                damaged_input = input("Damaged --> ")
                speeding_input = input("Speeding --> ")
                gender_input = input("Gender --> ")
                size_input = input("Size --> ")
            else:
                darkness_input = random.uniform(0,1)
                damaged_input = random.uniform(0, 1)
                speeding_input = random.uniform(0, 1)
                gender_input = random.uniform(0, 1)
                size_input = random.uniform(0, 1)

            test_dict = {"darkness": float(darkness_input), "damaged": float(damaged_input), "speeding": float(speeding_input), "gender":float(gender_input),"size":float(size_input)}
            print(test_dict)
            is_criminal = network.predict_criminal_car(test_dict)
            print(f"Criminal Vehicle: {is_criminal}")

            correct = input("Correct? [Y] [N] --> ")
            if correct.lower() == "y":
                # add to initial datastore
                if is_criminal == True:
                    test_dict["criminal"] = 1
                else:
                    test_dict["criminal"] = 0
                datastore.append(test_dict)
                print("Appending initial datastore.")
                contents["Dataset"] = datastore
                with open("./resources/datastore.json", "w") as fp:
                    json.dump(contents, fp)
            else:
                if is_criminal == True:
                    test_dict["criminal"] = 0
                else:
                    test_dict["criminal"] = 1
                datastore.append(test_dict)
                # add to initial datastore
                print("Appending initial datastore.")
                contents["Dataset"] = datastore
                with open("./resources/datastore.json", "w") as fp:
                    json.dump(contents, fp)
            network.app.number_of_nodes+=1
        elif choice.lower() == "q":
            network.app.running = False
            break
            os.quit()
    except Exception as error:
        print(f"Failed: {error}\n\n")
        pass
