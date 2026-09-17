
students_cl = {}

def show_class():
    if not students_cl:
        print("the classroom is empty")
    else:
        for student, grade in students_cl.items():
            print(f"{student}: {grade}")

def add_student():
    name = input("Enter name student: ")
    if name not in students_cl:
        students_cl[name] = []
        print(f"student {name} added")
    else:
        print(f"student {name} already added")

def remove_student():
    name = input("Enter name student: ")
    if name in students_cl:
        del students_cl[name]
        print(f"student {name} removed")
    else:
        print(f"student {name} not found")

def add_grade():
    name = input("Enter name student: ")
    if name in students_cl:
        grade = input("Enter grade: ")
        students_cl[name].append(grade)
        print(f"grade {grade} added student {name}")
    else:
        print(f"student {name} not found")

def remove_grade():
    name = input("Enter name student: ")
    if name in students_cl:
        grade = input("Enter grade: ")
        students_cl[name].remove(grade)
        print(f"grade{grade} removed student {name}")
    else:
        print(f"student {name} not found")

def edit_grade():
    name = input("Enter name student: ")
    if name in students_cl:
        old_grade = input("Enter old grade: ")
        if old_grade in students_cl[name]:
            new_grade = input("Enter new grade: ")
            inx = students_cl[name].index(old_grade)
            students_cl[name][inx] = new_grade
            print(f"grade{new_grade} edited student {name}")
        else:
            print(f"grade not")
    else:
        print(f"student {name} not found")

while True:
    print("\n--- Menu ---")
    print("1. Show one's class")
    print("2. Add student")
    print("3. Remove student")
    print("4. Add grade")
    print("5. Remove grade")
    print("6. to charge a grade")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_class()
    elif choice == 2:
        add_student()
    elif choice == 3:
        remove_student()
    elif choice == 4:
        add_grade()
    elif choice == 5:
        remove_grade()
    elif choice == 6:
        edit_grade()
    elif choice == 0:
        print("exit for program")
        break
    else:
        print("invalid choice")
