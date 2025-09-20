#student result tarcking system
student_list = []
def add_student():
    name = input("Enter a name:")
    roll_no = int(input("Enter a roll number:"))
    subjects = ['Science','history','geography','maths']
    mark = {}
    for subject in subjects:
        marks = float(input("Enter a marks:"))
        mark[subjects]= marks
        average = sum(marks.values()/len(marks))
        passed = marks >= 40
        student_record = {
            'name':name,
            'roll_no':roll_no,
            'mark':mark,
            'average':average,
            'passed':passed
        }
        student_list.append(student_record)
        def display_students():
            if not student_list:
                print("No student found!")
                return
            for student in student_list:
                print("\n---Student Report---")
                print(f"Name:{student['name']}")
                print(f"Roll_no:{student['roll_no']}")
                print(f"Marks:")
                for subject,mark in student['mark'].items():
                    print(f"{subject}:{mark}")
                    print(f"Average:{student['average']:.2f}")
                    print(f"Result:{'passed'if student['passed'] else 'Failed'}")
                    def main():
                        while True:
                            print("\n--Student Grade Tracker Menu---")
                            print("1.Add Student")
                            print("2.Display Students")
                            print("3.Exit")
                            choice = input("Enter your choice:")
                            if choice == "1":
                                add_student()
                            elif choice == "2":
                                display_students
                            elif choice == "3":
                                print("Thank you for using the student grade tracker!")
                                break
                            else:
                                print("Invalid choice please try again later")

                                main()


