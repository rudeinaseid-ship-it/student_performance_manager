print("=" * 45)
print("          BISMILLAHI ALRAHMANI ALRAHIM")
print("=" * 45)
print("\n  Aselamu Aleykum!")
print("        STUDENT PERFORMANCE MANAGER")
print("-" * 45)
students = []
def register_student():
    print("\n--- STUDENT REGISTRATION ---")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    # Check for duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("This Student ID already exists!")
            return

    number = int(input("Enter number of subjects: "))

    subjects = []

    for i in range(number):
        subject = input(f"Enter subject {i + 1}: ")
        subjects.append(subject)

    student = {
        "id": student_id,
        "name": name,
        "subjects": subjects,
        "marks": []
    }

    students.append(student)

    print("\nStudent registered successfully!")
    # 2. Record Student Marks
def record_marks():
    print("\n--- RECORD STUDENT MARKS ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            marks = []

            for subject in student["subjects"]:
                mark = float(input(f"Enter mark for {subject}: "))
                marks.append(mark)

            student["marks"] = marks

            print("\nMarks recorded successfully!")
            return

    print("Student not found!")
    # 3. Search Student
def search_student():
    print("\n--- SEARCH STUDENT ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            print("\n--- STUDENT INFORMATION ---")
            print("Student ID:", student["id"])
            print("Name:", student["name"])

            print("\nSubjects and Marks:")

            for i in range(len(student["subjects"])):
                subject = student["subjects"][i]

                if len(student["marks"]) > i:
                    mark = student["marks"][i]
                    print(subject, ":", mark)
                else:
                    print(subject, ": Not recorded")

            return

    print("Student not found!")
    # 4. Calculate Student Results
def calculate_results():
    print("\n--- CALCULATE STUDENT RESULTS ---")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            if len(student["marks"]) == 0:
                print("No marks recorded for this student!")
                return

            total = sum(student["marks"])
            average = total / len(student["marks"])

            if average >= 90:
                grade = "A"
            elif average >= 80:
                grade = "B"
            elif average >= 70:
                grade = "C"
            elif average >= 60:
                grade = "D"
            else:
                grade = "F"

            print("\n--- STUDENT RESULTS ---")
            print("Name:", student["name"])
            print("Total Marks:", total)
            print("Average:", round(average, 2))
            print("Grade:", grade)

            if average >= 50:
                print("Status: PASS")
            else:
                print("Status: FAIL")

            return

    print("Student not found!")
    # 5. Display All Students
def display_students():
    print("\n--- ALL REGISTERED STUDENTS ---")

    if len(students) == 0:
        print("No students registered yet!")
        return

    for student in students:
        print("\n-------------------------")
        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Subjects:", ", ".join(student["subjects"]))

        if len(student["marks"]) > 0:
            print("Marks:", student["marks"])
        else:
            print("Marks: Not recorded")

    print("\n-------------------------")

while True:
    print("\n Main Menu")
    print("1. Register Student")
    print("2. Record Student Marks")
    print("3. Search Student")
    print("4. View Student Results")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        record_marks()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_results()

    elif choice == "5":
        display_students()

    elif choice == "6":
        print("\nJazakumuAllahu Khairan! Goodbye.")
        break

    else:
        print("Invalid choice. Please try again.")