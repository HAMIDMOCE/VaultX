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
            self.print_header("ADD PASSWORD")

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
            self.print_header("SAVED PASSWORDS")

            status, records = self.database.get_all_passwords()

            if not status:
                return status, records
            
            if not records:
                return True, "No passwords found."
            
            self.display_passwords(records)

            return True, "Passwords displayed successfully."
        
        elif choice == "3":
            self.print_header("SEARCH PASSWORDS")

            while True:
                website = input("Enter website: ").strip()

                if website:
                    break

                print("Website cannot be empty.\n")

            status, records = self.database.search_password(website)

            if not status:
                return False, records
            
            if not records:
                return True, "No passwords found."
            
            self.display_passwords(records)

            return True, "Passwords displayed successfully.\n"
        elif choice == "4":
            self.print_header("DELETE PASSWORD")

            status, records = self.database.get_all_passwords()

            if not status:
                return False, records

            if not records:
                return True, "No passwords found."
            
            self.display_passwords(records)

            while True:
                id_ = input("Enter ID: ").strip()

                if not id_:
                    print("ID cannot be empty.\n")
                    continue

                try:
                    id_ = int(id_)
                    break

                except ValueError:
                    print("ID must be a number.\n")

            while True:
                confirm = input("Are you sure? (y/n): ").strip().lower()

                if confirm in ("y","n"):
                    break

                print("Please enter y or n.\n")

            if confirm == "n":
                return True, "Delete operation cancelled."

            return self.database.delete_password(id_)
    
        elif choice == "5":
            self.print_header("UPDATE PASSWORD")

            status, records = self.database.get_all_passwords()

            if not status:
                return False, records

            if not records:
                return True, "No passwords found."

            self.display_passwords(records)

            while True:
                id_ = input("Enter ID: ").strip()
                
                if not id_:
                    print("ID cannot be empty.\n")
                    continue

                try:
                    id_ = int(id_)
                    break

                except ValueError:
                    print("ID must be a number.\n")


            record = [record for record in records if record[0] == id_]
            if not record:
                return True, "No password found with this ID."
            id_, website, username, password = record[0]

            print(f"Current Website: {website}")
            new_website = input("New Website (leave empty to keep): ").strip()
            if not new_website:
                new_website = website

            print(f"Current Username: {username}")
            new_username = input("New Username (leave empty to keep): ").strip()
            if not new_username:
                new_username = username

            print(f"Current Password: {password}")
            new_password = input("New password (leave empty to keep): ").strip()
            if not new_password:
                new_password = password

            while True:
                confirm = input("Are you sure? (y/n): ").strip().lower()
            
                if confirm in ("y","n"):
                    break
            
                print("Please enter y or n.\n")
            
            if confirm == "n":
                return True, "Update operation cancelled."

            return self.database.update_password(id_, new_website, new_username, new_password)

        elif choice == "6":
            return False, "Goodbye!"
        
        else:
            return True, "Invalid option."
        
    def display_passwords(self, records):
        for record in records:
            id_, website, username, password = record

            print(f"ID: {id_}")
            print(f"Website: {website}")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print("\n-------------------------\n")

    def print_header(self, title):
        print("=" * 40)
        print(title.center(40))
        print("=" * 40)
        print()