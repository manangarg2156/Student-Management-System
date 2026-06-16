class Student:
    def __init__(self, sid, name, age, marks):
        self.sid = sid
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Student ID: {self.sid}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")


students = []


def read_int(prompt):
    value = input(prompt).strip()
    if value.isdigit():
        return int(value)
    print("Please enter a number.")
    return None


def read_float(prompt):
    value = input(prompt).strip()
    try:
        return float(value)
    except ValueError:
        print("Please enter a number.")
        return None


def add_single_student():
    sid = read_int("Enter student id: ")
    if sid is None:
        return False

    for student in students:
        if student.sid == sid:
            print("This student ID already exists.")
            return False

    name = input("Enter name: ").strip()
    age = read_int("Enter age: ")
    if age is None:
        return False

    marks = read_float("Enter marks: ")
    if marks is None:
        return False

    students.append(Student(sid, name, age, marks))
    print("Student added successfully.")
    return True


def add_student():
    count = read_int("How many students do you want to add? ")
    if count is None or count <= 0:
        print("Enter a valid number greater than 0.")
        return

    for i in range(1, count + 1):
        print(f"\nStudent {i} of {count}")
        add_single_student()


def view_all():
    if not students:
        print("No students to display.")
        return

    for student in students:
        print("--------------------------")
        student.display()
    print("--------------------------")


def find_student(sid):
    for student in students:
        if student.sid == sid:
            return student
    return None


def search_student():
    sid = read_int("Enter student id to search: ")
    if sid is None:
        return

    student = find_student(sid)
    if student:
        student.display()
    else:
        print("Student not found.")


def update_marks():
    sid = read_int("Enter student id to update: ")
    if sid is None:
        return

    student = find_student(sid)
    if not student:
        print("Student not found.")
        return

    marks = read_float("Enter new marks: ")
    if marks is None:
        return

    student.marks = marks
    print("Marks updated.")


def delete_student():
    sid = read_int("Enter student id to delete: ")
    if sid is None:
        return

    student = find_student(sid)
    if not student:
        print("Student not found.")
        return

    students.remove(student)
    print("Student deleted.")


def display_highest():
    if not students:
        print("No students available.")
        return

    highest = students[0]
    for student in students:
        if student.marks > highest.marks:
            highest = student

    print("Student with highest marks:")
    highest.display()


def show_menu():
    menu = [
        "Add a new student",
        "View all students",
        "Search student by ID",
        "Update student marks",
        "Delete student record",
        "Show highest marks student",
        "Exit"
    ]

    print("\nStudent Management System")
    for index, item in enumerate(menu, start=1):
        print(f"{index}. {item}")


def main():
    while True:
        show_menu()
        choice = input("Choose option (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            display_highest()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1 to 7.")


main()