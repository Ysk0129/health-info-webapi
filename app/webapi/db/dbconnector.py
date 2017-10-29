import mysql.connector
from webapi.db.dbconfig import dbconfig

class DBConnector:

    def __init__(self):
        self.host = dbconfig["DB_HOST"]
        self.port = dbconfig["DB_PORT"]
        self.db = dbconfig["DB_NAME"]
        self.user = dbconfig["DB_USER"]
        self.password = dbconfig["DB_PASSWORD"]
        self.con = mysql.connector.connect(
                    host=self.host,
                    port=self.port,
                    db=self.db,
                    user=self.user,
                    passwd=self.password)
        self.cur = self.con.cursor()
