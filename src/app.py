from src.menu import Menu
from src.database import DatabaseManager

class App:
    
    def __init__(self):
        self.menu = Menu()
        self.database = DatabaseManager()

    def run(self):
        status, message = self.database.connect_server()
        if not status:
            print(message)
            return
        print(message)
        
        status, message = self.database.create_database()
        if not status:
            print(message)
            self.database.close()
            return
        print(message)
        
        status, message = self.database.connect_database()
        if not status:
            print(message)
            self.database.close()
            return
        print(message)
        
        status, message = self.database.create_tables()
        if not status:
            print(message)
            self.database.close()
            return
        print(message)

        while True:
            self.menu.show_menu()
            choice = input("Enter your choice: ").strip()

            should_continue, message = self.handle_choice(choice)
            print(message)

            if not should_continue:
                break

        self.database.close()

    def handle_choice(self, choice):
        if choice == "1":
            print("\n=========================")
            print("        ADD PASSWORD")
            print("=========================")

            while True:
                website = input("Enter website: ").strip()
                if website:
                    break
                print("Website cannot be empty.\n")
                
            while True:
                username = input("Enter username: ").strip()
                if username:
                    break
                print("Username cannot be empty.\n")

            while True:
                password = input("Enter password: ").strip()
                if password:
                    break
                print("Password cannot be empty.\n")

            return self.database.add_password(
                website,
                username,
                password
            )
        
        elif choice == "2":
            print("\n=========================")
            print("      SAVED PASSWORDS")
            print("=========================\n")

            status, records = self.database.get_all_passwords()

            if not status:
                return status, records
            
            if not records:
                return True, "No passwords found."
            
            for record in records:
                id_, website, username, password = record
                print(f"ID: {id_}")
                print(f"Website: {website}")
                print(f"Username: {username}")
                print(f"Password: {password}")
                print("\n-------------------------\n")

            return True, "Passwords displayed successfully."
        elif choice == "3":
            return True, "You selected Search Password.\n"
        elif choice == "4":
            return True, "You selected Delete Password.\n"
        elif choice == "5":
            return False, "Goodbye!"
        else:
            return True, "Invalid option."