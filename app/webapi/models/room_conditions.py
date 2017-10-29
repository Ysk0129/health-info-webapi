from webapi.models.room_condition import RoomCondition

class RoomConditions():

    def __init__(self, room_condition_list):
        self.room_condition_list = room_condition_list

    def get_rows_dicts(self):
        return [rc.get_rows_dict() for rc in self.room_condition_list]
    
    def get_columns_dict(self):
        return self.room_condition_list[0].get_columns_dict()

    def get_all_dict(self):
        return {"rows": self.get_rows_dicts(), "columns": self.get_columns_dict()}
