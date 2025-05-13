def show_menu():
    print("""
    1. Example Intervals ption
    2. Back
    """)
    return input("Please select an option: ") 


def main():
    """main loop of this sub-menu"""
    print("Welcome to Interval Training")
    running = True

    while running:
        choice = show_menu()

        if choice == "1":
            pass
        elif choice == "2":
            running = False
        else:
            print("\nNot a valid choice. Try again.")
