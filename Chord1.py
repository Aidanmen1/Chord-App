print("Welcome to Music Theory Training")
ans = True

while ans:

    print("""
    Select training option:
    1. Intervals
    2. Chord Analysis
    3. Roman Numeral Analysis
    4. Ear Training
    5. Exit
    """)
    
    ans = input("Please select an option: ")  # Take actual user input
    if ans == "1":
        print("\nIntervals")
    elif ans == "2":
        print("\nChord Analysis")
    elif ans == "3":
        print("\nRoman Numeral Analysis")
    elif ans == "4":
        print("\nEar Training") 
    elif ans == "5":
        print("Goodbye")
        ans = None
    else:
        print("\nNot a valid choice. Try again.")
