def add_student():

    name = input("Enter Student Name: ")

    try:
        marks = float(input("Enter Marks: "))
    except ValueError:
        print("Please enter valid marks.")
        return

    file = open("students.txt", "a")

    file.write(f"{name},{marks}\n")

    file.close()

    print("Student Added Successfully.")


def view_students():

    try:

        file = open("students.txt", "r")

        data = file.readlines()

        file.close()

        if len(data) == 0:
            print("No Records Found.")
            return

        print("\nStudent Records")
        print("-" * 35)

        for line in data:

            name, marks = line.strip().split(",")

            print(f"Name : {name}")
            print(f"Marks: {marks}")
            print("-" * 35)

    except FileNotFoundError:

        print("No student file found.")


def search_student():

    name = input("Enter Student Name: ")

    try:

        file = open("students.txt", "r")

        found = False

        for line in file:

            student, marks = line.strip().split(",")

            if student.lower() == name.lower():

                print("\nStudent Found")
                print("Name :", student)
                print("Marks:", marks)

                found = True

                break

        file.close()

        if not found:

            print("Student Not Found.")

    except FileNotFoundError:

        print("No Records Found.")


def main():

    while True:

        print("\n==============================")
        print(" Student Marks Tracker")
        print("==============================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            print("Thank You")
            break

        else:

            print("Invalid Choice")


main()