students = []
total_students = 0
total_marks = 0 
while True:
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Show class average")
    print("6. Show highest marks")
    print("7. Show lowest marks")
    print("8. Exit")
    while True:
        try:
            user_input = int(input("Choose an option: "))
        except ValueError:
            print("Enter a valid number.")
            continue
        if user_input not in range(1, 9):
            print("Enter a valid number.")
            continue
        break
    if user_input == 1:
        first_questiion = input("Name: ")
        while True:
            try:
                second_question = int(input("Age: "))
            except ValueError:
                print("Enter a valid number.")
                continue
            if second_question <= 0:
                print("Enter a valid number.")
                continue
            break
        while True:
            try:
               third_question = int(input("Marks: "))
            except ValueError:
                print("Enter a valid number.")
                continue
            if third_question < 0:
                print("Enter a valid number.")
                continue
            break
        all_about_student = {
            "Name" : first_questiion,
            "Age" : second_question,
            "Marks" : third_question
        }
        students.append(all_about_student)
        total_students += 1
        print("Student added.")
    elif user_input == 2:
        for number,all_students in enumerate(students, start=1):
            print(f"{number}. Name: {all_students['Name']} | Age: {all_students['Age']} | Marks: {all_students['Marks']} |")
    elif user_input == 3:
        search_student = input("Enter student name: ")
        found = False
        for student in students:
            if search_student == student['Name']:
                print(f"Name: {student['Name']} | Age: {student['Age']} | Marks: {student['Marks']}")
                found = True
        if not found:
            print("No students found.")
    elif user_input == 4:
        while True:
            try:
                delete_student = int(input("Enter the student's serial number to delete: "))
            except ValueError:
                print("Enter a right serial number")
                continue
            break
        if delete_student in range(1, len(students) +1):
            remove_student = delete_student - 1
            students.pop(remove_student)
            total_students -= 1
            print("Student removed.")
    elif user_input == 5:
        if total_students > 0:
            total_marks = 0
            for student in students:
                total_marks += student['Marks']
            average = total_marks / total_students
            print(f"Average: {average}")
        else:
            print("No student added yet!")
    elif user_input == 6:
        marks = []
        if total_students > 0:
            for student_highest_mark in students:
                marks.append(student_highest_mark['Marks'])
        else:
            print("No student added yet!")
        highest = max(marks)
        print(f"Highest mark: {highest}")
    elif user_input == 7:
        marks = []
        if total_students > 0:
                for student_lowest_mark in students:
                    marks.append(student_lowest_mark['Marks'])
        else:
            print("No student added yet!")
        lowest = min(marks)
        print(f"Lowest mark: {lowest}")
    elif user_input == 8:
        exit()