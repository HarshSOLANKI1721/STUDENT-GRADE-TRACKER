#student result tarcking system
# STUDENT-GRADE-TRACKER
# Simple Student Grade Tracker

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

students = {}

while True:
    print("\n--- Student Grade Tracker ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        subjects = int(input("How many subjects? "))
        marks = []

        for i in range(subjects):
            while True:
                mark = float(input(f"Enter marks for subject {i+1} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100. Please try again.")

        avg = sum(marks) / subjects
        grade = calculate_grade(avg)
        students[name] = {"Marks": marks, "Average": avg, "Grade": grade}
        print(f"{name}'s data saved! ✅")

    elif choice == "2":
        if not students:
            print("No student data available yet.")
        else:
            for student, info in students.items():
                print(f"\nName: {student}")
                print(f"Marks: {', '.join(map(str, info['Marks']))}")
                print(f"Average: {info['Average']:.2f}")
                print(f"Grade: {info['Grade']}")

    elif choice == "3":
        print("Exiting Grade Tracker. Goodbye!")
        break

    else:
        print("Invalid choice, try again.")


