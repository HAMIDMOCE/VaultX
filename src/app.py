from src.menu import Menu

class App:
    
    def __init__(self):
        self.menu = Menu()

    def run(self):
        self.menu.show_menu()

        while True:
            choice = input("Enter your choice: ").strip()
            should_continue, message = self.handle_choice(choice)
            
            print(message)

            if not should_continue:
                break

    def handle_choice(self, choice):
        if choice == "1":
            return True, "You selected Add Password.\n"
        elif choice == "2":
            return True, "You selected View Passwords.\n"
        elif choice == "3":
            return True, "You selected Search Password.\n"
        elif choice == "4":
            return True, "You selected Delete Password.\n"
        elif choice == "5":
            return False, "Goodbye!"
        else:
            return True, "Invalid option."