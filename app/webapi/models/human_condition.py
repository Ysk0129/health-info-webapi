class HumanCondition():

    def __init__(self, heart, steps, distance, calories, name, time):
        self.heart = heart
        self.steps = steps
        self.distance = distance
        self.calories = calories
        self.name = name
        self.time = time

    def get_rows_dict(self):
        rows = {
            "heart": self.heart,
            "steps": self.steps,
            "distance": self.distance,
            "calories": self.calories,
            "name": self.name,
            "time": self.time
        }
        return rows

    def get_columns_dict(self):
        columns = [
            {
                "name": "heart",
                "friendly_name": "heart",
                "type": "float"
            },
            {
                "name": "steps",
                "friendly_name": "steps",
                "type": "int"
            },
            {
                "name": "distance",
                "friendly_name": "distance",
                "type": "float"
            },
            {
                "name": "calories",
                "friendly_name": "calories",
                "type": "int"
            },
            {
                "name": "name",
                "friendly_name": "name",
                "type": "string"
            },
            {
                "name": "time",
                "friendly_name": "time",
                "type": "datetime"
            }
        ]
        return columns
