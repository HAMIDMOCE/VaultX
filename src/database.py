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
        
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database_name = database_name

        self.connection = None
        self.cursor = None

        self.columns = "id, website, username, password"

    def connect_server(self):
        try:
            self.connection = connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password
            )

            self.cursor = self.connection.cursor()
            return True, "Connected to MySQL server successfully."
        
        except connector.Error as error:
            return False, str(error)

    def create_database(self):
        try:
            self.cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {self.database_name}"
            )

            return True, "Database created successfully."
        
        except connector.Error as error:
            return False, str(error)

    def connect_database(self):
        try:
            self.connection = connector.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                database = self.database_name
            )

            self.cursor = self.connection.cursor()
            return True, f"Connected to '{self.database_name}' successfully."
        
        except connector.Error as error:
            return False, str(error)

    def create_tables(self):
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS passwords(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    website VARCHAR(255) NOT NULL,
                    username VARCHAR(255) NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

            return True, "Tables created successfully."
        
        except connector.Error as error:
            return False, str(error)

    def close(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None

        if self.connection:
            self.connection.close()
            self.connection = None

    def add_password(self, website, username, password):
        try:
            self.cursor.execute(
                """
                INSERT INTO passwords (website, username, password)
                VALUES (%s, %s, %s)
                """,
                (website, username, password)
            )

            self.connection.commit()

            return True, "Password added successfully."
        
        except connector.Error as error:
            return False, str(error)
        

    def get_all_passwords(self):
        try:
            self.cursor.execute(
                f"""
                SELECT {self.columns}
                FROM passwords
                """
            )

            records = self.cursor.fetchall()
            
            return True, records
        except connector.Error as error:
            return False, str(error)
        
    def search_password(self, website):
        search_value = f"%{website}%"

        try:
            self.cursor.execute(
                f"""
                SELECT {self.columns}
                FROM passwords
                WHERE website LIKE %s
                """,
                (search_value,)
            )

            records = self.cursor.fetchall()

            return True, records
        
        except connector.Error as error:
            return False, str(error)

    def delete_password(self, id_):
        try:
            self.cursor.execute(
                """
                DELETE FROM passwords WHERE id = %s
                """,
                (id_,)
            )
            
            self.connection.commit()
            
            count = self.cursor.rowcount
            
            if count == 0:
                return True, "No password found with this ID."
            
            return True, "Password deleted successfully."

        except connector.Error as error:
            return False, str(error)

    def update_password(self, id_, new_website, new_username, new_password):
        try:
            self.cursor.execute(
                """
                UPDATE passwords SET
                    website=%s,
                    username=%s,
                    password=%s
                WHERE id=%s
                """,
                (new_website, new_username, new_password, id_)
            )

            self.connection.commit()

            count = self.cursor.rowcount

            if count == 0:
                return True, "No password found with this ID."

            return True, "Updated successfully."

        except connector.Error as error:
            return False, str(error)