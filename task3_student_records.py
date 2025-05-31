# Dictionary to store all the student records
students = {}

# Function to add a student
def add_student():
    print("\n--- Add Student ---")
    rollno = input("Enter Roll Number (Unique): ")
    if rollno in students:
        print("Student with this roll number already exists!")
        return

    name = input("Enter Name: ")
    try:
        marks = float(input("Enter Marks: "))
    except ValueError:
        print("Invalid marks. Must be a number.")
        return

    contact = input("Enter Contact Number: ")

    students[rollno] = {
        'name': name,
        'marks': marks,
        'contact': contact
    }
    print("Student added successfully.")

# Function to search for a student
def search_student():
    print("\n--- Search Student ---")
    rollno = input("Enter Roll Number to search: ")
    if rollno in students:
        student = students[rollno]
        print("\nStudent Found:")
        print(f" Name    : {student['name']}")
        print(f" Marks   : {student['marks']}")
        print(f" Contact : {student['contact']}")
    else:
        print("No record found.")

# Function to display all students
def display_students():
    print("\n--- All Student Records ---")
    if not students:
        print("No records found.")
        return
    print("{:<12}{:<15}{:<10}{:<15}".format("Roll No", "Name", "Marks", "Contact No"))
    print("-" * 60)
    for rollno, info in students.items():
        print("{:<12}{:<15}{:<10}{:<15}".format(
            rollno, info['name'], info['marks'], info['contact']
        ))

# Main menu loop
while True:
    print("\n===== Student Record Menu =====")
    print("1. Add Student")
    print("2. Search Student by Roll Number")
    print("3. Display All Students")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        display_students()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
