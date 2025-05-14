#This is how you import other python modules to make their code accessible
import chordapp_intervals
import chordapp_chord_analysis
import chordapp_roman_numeral_analysis
import chordapp_ear_training

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
    running = True
    print("Welcome to Music Theory Training")
    while running:
        choice = show_menu()
        if choice == "1":
            chordapp_intervals.main() # this means - go to the intervals module and call its main function
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
    #This is the entry point for your program, when you run it this code gets executed
    main()
