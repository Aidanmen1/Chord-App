def show_menu():
    print("""
    Select training option:
    1. Intervals
    2. Chord Analysis
    3. Roman Numeral Analysis
    4. Ear Training
    5. Exit
    """)
    return input("Please select an option: ") 

def main():
    print("Welcome to Music Theory Training")
    while True:
        choice = show_menu()
        if choice == "1":
            print("\nIntervals")
        elif choice == "2":
            print("\nChord Analysis")
        elif choice == "3":
            print("\nRoman Numeral Analysis")
        elif choice == "4":
            print("\nEar Training") 
        elif choice == "5":
            print("Goodbye")
            break  
        else:
            print("\nNot a valid choice. Try again.")

main()
