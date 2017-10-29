from webapi.db.dbconnector import DBConnector

class HumanConditionConnector(DBConnector):

    def select_human_condition(self, **conditions):
        
        if "name" not in conditions:
            return None

        if "startdate" in conditions and "enddate" in conditions:
            sql = "SELECT HEART, STEPS, DISTANCE, CALORIES, NAME, TIME FROM HUMANCONDITION WHERE TIME >= %s AND TIME <= %s;"
            self.cur.execute(sql, [conditions["startdate"], conditions["enddate"]])
            result = self.cur.fetchall()
            return result

        if "startdate" in conditions in conditions:
            sql = "SELECT HEART, STEPS, DISTANCE, CALORIES, NAME, TIME FROM HUMANCONDITION WHERE TIME >= %s AND TIME <= %s;"
            self.cur.execute(sql, [conditions["startdate"], conditions["enddate"]])
            result = self.cur.fetchall()
            return result

        sql = "SELECT HEART, STEPS, DISTANCE, CALORIES, NAME, TIME FROM HUMANCONDITION WHERE NAME = %s;"
        self.cur.execute(sql, [conditions["name"]])
        result = self.cur.fetchall()
        return result

    def insert_human_condition(self, **values):

        if not is_contain_nessesary(values):
            return None

        sql = "INSERT INTO HUMANCONDITION (HEART, STEPS, DISTANCE, CALORIES, NAME) VALUES (%s, %s, %s, %s, %s);"
        values = [values["heart"], values["steps"], values["distance"], values["calories"], values["name"]]
        try:
            self.cur.execute(sql, values)
            self.con.commit()
        except:
            self.con.rollback()
            raise

def is_contain_nessesary(values):

    if "name" not in values:
        return False

    if "heart" not in values:
        return False
        
    if "steps" not in values:
        return False

    if "distance" not in values:
        return False

    if "calories" not in values:
        return False

    return True
