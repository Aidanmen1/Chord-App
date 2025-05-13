#This is how you import other python modules
import chordapp_intervals
import chordapp_chord_analysis
import chordapp_roman_numeral_analysis
import chordapp_ear_training
#when you use "import" it makes the code form the module you're importing become available to your program

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
    """this is the main loop of the program, if it terminates, end the program"""
    print("Welcome to Music Theory Training")
    running = True

    while running:
        choice = show_menu()

        if choice == "1":
            chordapp_intervals.main()
        elif choice == "2":
            chordapp_chord_analysis.main()
        elif choice == "3":
            chordapp_roman_numeral_analysis.main()
        elif choice == "4":
            chordapp_ear_training.main()
        elif choice == "5":
            print("Goodbye")
            running = False
        else:
            print("\nNot a valid choice. Try again.")



if __name__ == "__main__":
    #This is the code that runs when you execute the program, this is the entry point
    #for everything else

    main()
