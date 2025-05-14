def show_menu():
    print("""
    Select training option:
    1. Example Ear Training Menu
    2. Back
    """)
    return input("Please select an option: ") 

    
def main():
    running = True
    print("Welcome to Interval Training")
    while running:
        choice = show_menu()
        if choice == "1":
            pass
        elif choice == "2":
            running = False
        else:
            print("\nNot a valid choice. Try again.")
