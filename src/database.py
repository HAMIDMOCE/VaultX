from mysql import connector

class DatabaseManager:

    def __init__(
            self,
            host="localhost",
            port=3306,
            user="root",
            password="Hamid.mo83",
            database_name="vaultx"
            ):
        self.database_name = database_name
        self.port = port
        self.host = host
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                port = self.port,
                database = self.database_name
            )
            self.cursor = self.connection.cursor()
            return True, "Connected successfully"

        except connector.Error as error:
            return False, str(error)