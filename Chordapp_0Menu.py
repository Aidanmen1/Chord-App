import subprocess

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
            subprocess.run(["python", "Chordapp_1Intervals.py"])
        elif choice == "2":
            subprocess.run(["python", "Chordapp_2ChordAnalysis.py"])
        elif choice == "3":
            subprocess.run(["python", "Chordapp_3RomanNumeralAnalysis.py"])
        elif choice == "4":
            subprocess.run(["python", "Chordapp_4EarTraining.py"])
        elif choice == "5":
            print("Goodbye")
            break  
        else:
            print("\nNot a valid choice. Try again.")

main()
