from mysql import connector

class DatabaseManager:

    def __init__(
            self,
            host="localhost",
            port=3306,
            user="root",
            password="Hamid.mo83",
            database_name="vaultx"):
        
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database_name = database_name

        self.connection = None
        self.cursor = None

    def connect_server(self):
        try:
            self.connection = connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
            )

            self.cursor = self.connection.cursor()
            return True, "Connected to MySQL server successfully."
        
        except connector.Error as error:
            return False, str(error)

    def create_database(self):
        pass

    def connect_database(self):
        pass

    def create_tables(self):
        pass

    def close(self):
        pass