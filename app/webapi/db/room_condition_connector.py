from webapi.db.dbconnector import DBConnector

class RoomConditionConnector(DBConnector):

    def select_room_condition(self, **conditions):
        
        if "name" not in conditions:
            return None

        if "startdate" in conditions and "enddate" in conditions:
            sql = "SELECT TEMPERATURE, HUMIDITY, NAME, TIME FROM ROOMCONDITION WHERE TIME >= %s AND TIME <= %s;"
            self.cur.execute(sql, [conditions["startdate"], conditions["enddate"]])
            result = self.cur.fetchall()
            return result

        if "startdate" in conditions:
            sql = "SELECT TEMPERATURE, HUMIDITY, NAME, TIME FROM ROOMCONDITION WHERE TIME >= %s;"
            self.cur.execute(sql, [conditions["startdate"]])
            result = self.cur.fetchall()
            return result

        if "enddate" in conditions:
            sql = "SELECT TEMPERATURE, HUMIDITY, NAME, TIME FROM ROOMCONDITION WHERE TIME <= %s;"
            self.cur.execute(sql, [conditions["enddate"]])
            result = self.cur.fetchall()
            return result

        sql = "SELECT TEMPERATURE, HUMIDITY, NAME, TIME FROM ROOMCONDITION WHERE NAME = %s;"
        self.cur.execute(sql, [conditions["name"]])
        result = self.cur.fetchall()
        return result

    def insert_room_condition(self, **values):

        if not is_contain_nessesary(values):
            return None

        sql = "INSERT INTO ROOMCONDITION (NAME, TEMPERATURE, HUMIDITY) VALUES (%s, %s, %s);"
        values = [values["name"], values["temperature"], values["humidity"]]
        try:
            self.cur.execute(sql, values)
            self.con.commit()
        except:
            self.con.rollback()
            raise

def is_contain_nessesary(values):

    if "name" not in values:
        return False

    if "temperature" not in values:
        return False
        
    if "humidity" not in values:
        return False

    return True
