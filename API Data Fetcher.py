import requests
while True:  
    user_input = input("Enter todo ID(or q to quit): ")  
    if user_input.lower == "q":
        exit()
    try:
        user_input = int(user_input)
    except ValueError:
        print("Enter a number only.")
        continue
    if  user_input not in range(1,201):
            print("Please enter an ID between 1 and 200.")
            continue
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{user_input}")
    data = response.json()
    if response.status_code == 200:
        print(f"Todo ID: {data['id']}")
        print(f"User ID: {data['userId']}")
        print(f"Title: {data['title']}")
        print(f"Completed: {data['completed']}")
    else:
       print("Todo not found!")
    