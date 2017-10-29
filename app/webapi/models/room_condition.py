class RoomCondition():

    def __init__(self, temperature, humidity, name, time):
        self.temperature = temperature
        self.humidity = humidity
        self.name = name
        self.time = time

    def get_rows_dict(self):
        rows = {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "name": self.name,
            "time": self.time
        }
        return rows

    def get_columns_dict(self):
        columns = [
            {
                "name": "temperature",
                "friendly_name": "temperature",
                "type": "float"
            },
            {
                "name": "humidity",
                "friendly_name": "humidity",
                "type": "float"
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
