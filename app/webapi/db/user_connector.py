from webapi.db.dbconnector import DBConnector

class UserConnector(DBConnector):

    def select_user(self, **conditions):

        if "name" not in conditions:
            return None

        sql = "SELECT * FROM USER WHERE NAME = %s;"
        self.cur.execute(sql, [conditions["name"]])
        result = self.cur.fetchall()
        return result

    def insert_user(self, **values):

        if not is_contain_nessesary(values):
            return None

        sql = "INSERT INTO USER (NAME) VALUES (%s);"
        values = [values["name"]]
        try:
            self.cur.execute(sql, values)
            self.con.commit()
        except:
            con.rollback()
            raise

def is_contain_nessesary(values):

    if "name" not in values:
        return False

    return True
