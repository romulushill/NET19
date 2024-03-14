import json
import time
import numpy as np
import tensorflow as tf
from datetime import datetime

class Training:
    def __init__(self, database_reference=None, aspects_reference=[], result_reference=None):
        self.model = None
        self.aspects_reference = aspects_reference
        self.result_reference = result_reference
        try:
            with open(database_reference, "r") as fp:
                self.database = json.load(fp)
            self.data = self.database["Dataset"]
            print("Loaded dataset.")
            return
        except Exception as error:
            self.database = None
            self.data = None
            print(f"Failed to load dataset:\n{error}")
            return None

    def train(self):
        try:
            features_array = []
            labels_array = []

            for element in self.data:
                print(element)
                internal = []
                for aspect in self.aspects_reference:
                    internal.append(element[aspect])
                features_array.append(
                    internal
                )
                labels_array.append([element[self.result_reference]])

            features = np.array(features_array)
            labels = np.array(labels_array)  # Labels for the corresponding cars

            # Define the neural network architecture
            self.model = tf.keras.Sequential(
                [
                    tf.keras.layers.Dense(4, activation="relu", input_shape=(len(self.aspects_reference),)),
                    tf.keras.layers.Dense(4, activation="relu"),
                    tf.keras.layers.Dense(1, activation="sigmoid"),
                ]
            )
            # tf.keras.layers.Dense(outputs, activation="relu", input_shape=(number_of_inputs,)),

            # Compile the model
            self.model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

            # Train the model - Need to move this to independent file.
            self.model.fit(features, labels, epochs=100, batch_size=1)
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime("%Y-%m-%d")
            formatted_time = str(current_datetime.strftime("%H.%M.%S"))
            self.path = f"./resources/models/weightings-{formatted_date}-{formatted_time}.weights.h5"
            self.model.save_weights(self.path)
            self.model.load_weights(self.path)

            return self.model
        except Exception as error:
            print(error)
            return None
