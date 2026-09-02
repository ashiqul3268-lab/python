print("1. Add student")
print("2. View students")
print("3. Search students")
print("4. Delete student")
print("5. Show class average")
print("6. Show highest marks")
print("7. Show lowest marks")
print("8. Exit")
students = []
total_student = 0
total_marks = 0
while True:
    try:
        user_input = int(input("Chose: "))
    except ValueError:
        print("Input a valid number")
        continue
    if user_input not in range(1 , 9):
        print("Input a valid number")
    elif user_input == 1:
        first_question = input("Name: ")
        second_question = input("Age: ")
        last_question = int(input("Marks: "))
        student_details = {
            "student_name" : first_question,
            "student_age" : second_question,
            "student_marks" : last_question
        }
        students.append(student_details)
        total_student += 1
        print("Student added!")
    elif user_input == 2:
        for number, all_students in enumerate(students , start=1):
            print(f"{number}. {all_students['student_name']} | Age: {all_students['student_age']} | Marks: {all_students['student_marks']}")
    elif user_input == 3:
        user_find = input("Enter student name: ")
        found = False
        for student in students:
            if user_find == student["student_name"]:
                print("Student found!")
                print(f"{student['student_name']} | {student['student_age']} | {student['student_marks']}")
                found = True
        if not found:
               print("No student found!")
    elif user_input == 4:
        try:
          delete_input = int(input("Enter the student serial number to delete: "))
        except ValueError:
            print("Input a valid number") 
            continue
        if delete_input in range(1 , len(students) + 1):
            delete_student = delete_input - 1
            students.pop(delete_student)
            print(f"{delete_input} Number Student removed!")
            total_student -= 1
        else:
            print("Input a valid number")  
    elif user_input == 5:
        if total_student > 0:
          total_marks = 0
          for student in students:
           total_marks += student["student_marks"]
          average = total_marks / total_student
          print(average)
        else:
            print("There are no student")
    elif user_input == 6:
        marks = []
        if total_student > 0:
          for student in students:
            marks.append(student["student_marks"])
          highest = max(marks)
          print(highest)
        else:
           print("There are no student")
    elif user_input == 7:
        marks = []
        if total_student > 0:
          for student in students:
            marks.append(student["student_marks"])
          lowest = min(marks)
          print(lowest)
        else:
           print("There are no student")
    elif user_input == 8:
        exit()