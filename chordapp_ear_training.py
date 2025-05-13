def show_menu():
    print("""
    1. Example Ear Training Option
    2. Back
    """)
    return input("Please select an option: ") 


def main():
    """main loop of this sub-menu"""
    print("Welcome to Ear Training")
    running = True

    while running:
        choice = show_menu()

        if choice == "1":
            pass
        elif choice == "2":
            running = False
        else:
            print("\nNot a valid choice. Try again.")
