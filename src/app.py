from src.menu import Menu

class App:
    
    def __init__(self):
        self.menu = Menu()

    def run(self):
        self.menu.show_menu()

        while True:
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                print("You selected Add Password.\n")
            elif choice == "2":
                print("You selected View Passwords.\n")
            elif choice == "3":
                print("You selected Search Password.\n")
            elif choice == "4":
                print("You selected Delete Password.\n")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")