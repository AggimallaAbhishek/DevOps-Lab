# Student Management System (CLI)

students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    cgpa = float(input("Enter CGPA: "))

    student = {
        "roll": roll,
        "name": name,
        "dept": dept,
        "cgpa": cgpa
    }

    students.append(student)
    print("✅ Student added successfully!\n")


def view_students():
    if not students:
        print("⚠️ No students found.\n")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Dept: {s['dept']}, CGPA: {s['cgpa']}")
    print()


def search_student():
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s["roll"] == roll:
            print("\n🎯 Student Found")
            print(s)
            print()
            return
    print("❌ Student not found.\n")


def update_student():
    roll = input("Enter Roll Number to update: ")
    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new Name: ")
            s["dept"] = input("Enter new Department: ")
            s["cgpa"] = float(input("Enter new CGPA: "))
            print("✅ Student updated successfully!\n")
            return
    print("❌ Student not found.\n")


def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("🗑️ Student deleted successfully!\n")
            return
    print("❌ Student not found.\n")


def menu():
    print("====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def main():
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
