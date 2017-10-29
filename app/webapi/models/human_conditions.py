from webapi.models.human_condition import HumanCondition

class HumanConditions():

    def __init__(self, human_condition_list):
        self.human_condition_list = human_condition_list

    def get_rows_dicts(self):
        return [hc.get_rows_dict() for hc in self.human_condition_list]
    
    def get_columns_dict(self):
        return self.human_condition_list[0].get_columns_dict()

    def get_all_dict(self):
        return {"rows": self.get_rows_dicts(), "columns": self.get_columns_dict()}
