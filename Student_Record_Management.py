import csv


def add_student(students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")

    students.append({
        "name": name,
        "age": age,
        "course": course
    })

    print("Student added.")


def display_students(students):
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(
            "Name:", student["name"],
            "| Age:", student["age"],
            "| Course:", student["course"]
        )


def save_students(students):
    with open("students.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "age", "course"]
        )

        writer.writeheader()
        writer.writerows(students)

    print("Student records saved.")


students = []

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Save Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            save_students(students)

        elif choice == "4":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid age.")
    except OSError as error:
        print("File error:", error)
