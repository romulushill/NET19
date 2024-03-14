
class Data:
    def __init__(self):
        self.training_data = [
            {"colour": 0.85, "damaged": 0.2, "speeding": 0.1, "gender": 0.3, "size": 0.6, "criminal": 0.3},
            {"colour": 0.72, "damaged": 0.1, "speeding": 0.8, "gender": 0.5, "size": 0.4, "criminal": 0.5},
            {"colour": 0.45, "damaged": 0.3, "speeding": 0.6, "gender": 0.7, "size": 0.2, "criminal": 0.5},
            {"colour": 0.92, "damaged": 0.5, "speeding": 0.2, "gender": 0.4, "size": 0.8, "criminal": 0.6},
            {"colour": 0.61, "damaged": 0.4, "speeding": 0.4, "gender": 0.6, "size": 0.5, "criminal": 0.5},
            {"colour": 0.33, "damaged": 0.6, "speeding": 0.7, "gender": 0.8, "size": 0.3, "criminal": 0.7},
            {"colour": 0.77, "damaged": 0.3, "speeding": 0.5, "gender": 0.2, "size": 0.7, "criminal": 0.6},
            {"colour": 0.49, "damaged": 0.2, "speeding": 0.3, "gender": 0.9, "size": 0.1, "criminal": 0},
            {"colour": 0.68, "damaged": 0.7, "speeding": 0.4, "gender": 0.1, "size": 0.9, "criminal": 0},
            {"colour": 0.55, "damaged": 0.8, "speeding": 0.9, "gender": 0.6, "size": 0.3, "criminal": 0},
            {"colour": 0.29, "damaged": 0.4, "speeding": 0.2, "gender": 0.3, "size": 0.8, "criminal": 0},
            {"colour": 0.82, "damaged": 0.5, "speeding": 0.7, "gender": 0.4, "size": 0.6, "criminal": 0},
            {"colour": 0.37, "damaged": 0.1, "speeding": 0.5, "gender": 0.8, "size": 0.4, "criminal": 0},
            {"colour": 0.91, "damaged": 0.3, "speeding": 0.1, "gender": 0.5, "size": 0.7, "criminal": 0},
            {"colour": 0.74, "damaged": 0.6, "speeding": 0.8, "gender": 0.2, "size": 0.5, "criminal": 0},
            {"colour": 0.58, "damaged": 0.2, "speeding": 0.3, "gender": 0.7, "size": 0.3, "criminal": 0},
            {"colour": 0.43, "damaged": 0.4, "speeding": 0.6, "gender": 0.4, "size": 0.8, "criminal": 0},
            {"colour": 0.65, "damaged": 0.7, "speeding": 0.4, "gender": 0.6, "size": 0.2, "criminal": 0},
            {"colour": 0.26, "damaged": 0.5, "speeding": 0.2, "gender": 0.1, "size": 0.6, "criminal": 0},
            {"colour": 0.87, "damaged": 0.2, "speeding": 0.9, "gender": 0.8, "size": 0.4, "criminal": 0},
            {"colour": 0.52, "damaged": 0.3, "speeding": 0.7, "gender": 0.2, "size": 0.9, "criminal": 0},
            {"colour": 0.39, "damaged": 0.6, "speeding": 0.4, "gender": 0.9, "size": 0.2, "criminal": 0},
            {"colour": 0.79, "damaged": 0.1, "speeding": 0.6, "gender": 0.3, "size": 0.7, "criminal": 0},
            {"colour": 0.47, "damaged": 0.8, "speeding": 0.3, "gender": 0.7, "size": 0.1, "criminal": 0},
            {"colour": 0.63, "damaged": 0.5, "speeding": 0.1, "gender": 0.4, "size": 0.8, "criminal": 0},
            {"colour": 0.31, "damaged": 0.2, "speeding": 0.8, "gender": 0.6, "size": 0.5, "criminal": 0},
            {"colour": 0.84, "damaged": 0.4, "speeding": 0.5, "gender": 0.2, "size": 0.9, "criminal": 0},
            {"colour": 0.56, "damaged": 0.7, "speeding": 0.2, "gender": 0.8, "size": 0.3, "criminal": 0},
            {"colour": 0.41, "damaged": 0.3, "speeding": 0.9, "gender": 0.5, "size": 0.6, "criminal": 0},
            {"colour": 0.71, "damaged": 0.6, "speeding": 0.3, "gender": 0.1, "size": 0.4, "criminal": 0},
            {"colour": 0.27, "damaged": 0.1, "speeding": 0.4, "gender": 0.7, "size": 0.2, "criminal": 0},
            {"colour": 0.93, "damaged": 0.8, "speeding": 0.6, "gender": 0.3, "size": 0.8, "criminal": 0},
            {"colour": 0.59, "damaged": 0.5, "speeding": 0.7, "gender": 0.9, "size": 0.1, "criminal": 0},
            {"colour": 0.35, "damaged": 0.2, "speeding": 0.3, "gender": 0.4, "size": 0.7, "criminal": 0},
            {"colour": 0.76, "damaged": 0.6, "speeding": 0.4, "gender": 0.2, "size": 0.5, "criminal": 0},
            {"colour": 0.48, "damaged": 0.3, "speeding": 0.1, "gender": 0.8, "size": 0.3, "criminal": 0},
            {"colour": 0.62, "damaged": 0.7, "speeding": 0.8, "gender": 0.5, "size": 0.6, "criminal": 0},
            {"colour": 0.28, "damaged": 0.4, "speeding": 0.6, "gender": 0.1, "size": 0.9, "criminal": 0},
            {"colour": 0.81, "damaged": 0.1, "speeding": 0.2, "gender": 0.6, "size": 0.4, "criminal": 0},
            {"colour": 0.54, "damaged": 0.8, "speeding": 0.5, "gender": 0.3, "size": 0.7, "criminal": 0},
            {"colour": 0.42, "damaged": 0.5, "speeding": 0.4, "gender": 0.7, "size": 0.2, "criminal": 0},
            {"colour": 0.67, "damaged": 0.2, "speeding": 0.1, "gender": 0.4, "size": 0.8, "criminal": 0},
            {"colour": 0.38, "damaged": 0.6, "speeding": 0.9, "gender": 0.2, "size": 0.5, "criminal": 0},
            {"colour": 0.88, "damaged": 0.3, "speeding": 0.4, "gender": 0.8, "size": 0.3, "criminal": 0},
            {"colour": 0.73, "damaged": 0.7, "speeding": 0.2, "gender": 0.5, "size": 0.6, "criminal": 0},
            {"colour": 0.57, "damaged": 0.4, "speeding": 0.5, "gender": 0.1, "size": 0.9, "criminal": 0},
            {"colour": 0.32, "damaged": 0.1, "speeding": 0.8, "gender": 0.6, "size": 0.2, "criminal": 0},
            {"colour": 0.86, "damaged": 0.6, "speeding": 0.3, "gender": 0.3, "size": 0.7, "criminal": 0},
            {"colour": 0.51, "damaged": 0.2, "speeding": 0.7, "gender": 0.9, "size": 0.4, "criminal": 0},
            {"colour": 0.36, "damaged": 0.8, "speeding": 0.6, "gender": 0.4, "size": 0.8, "criminal": 0},
            {"colour": 0.78, "damaged": 0.5, "speeding": 0.1, "gender": 0.7, "size": 0.3, "criminal": 0},
            {"colour": 0.44, "damaged": 0.3, "speeding": 0.4, "gender": 0.2, "size": 0.6, "criminal": 0},
            {"colour": 0.69, "damaged": 0.7, "speeding": 0.9, "gender": 0.8, "size": 0.1, "criminal": 0}
        ]
        return