students = []

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        usn = input("Enter USN: ")
        branch = input("Enter Branch: ")

        student = {
            "Name": name,
            "USN": usn,
            "Branch": branch
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            for student in students:
                print("----------------------")
                print("Name   :", student["Name"])
                print("USN    :", student["USN"])
                print("Branch :", student["Branch"])

    elif choice == "3":
        usn = input("Enter USN to search: ")
        found = False

        for student in students:
            if student["USN"] == usn:
                print("\nStudent Found")
                print("Name   :", student["Name"])
                print("USN    :", student["USN"])
                print("Branch :", student["Branch"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        usn = input("Enter USN to delete: ")
        found = False

        for student in students:
            if student["USN"] == usn:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")s