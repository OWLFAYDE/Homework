def add(participants):
    first_name = input("Enter  first name: ")
    last_name = input("Enter  last name: ")
    key = (first_name,last_name)
    raw_interest = input("Enter  interest: ")
    interest_list = raw_interest.split(",")
    interest_set = set(interest_list)
    participants[key] = interest_set

def remove(participants):
    first_name = input("Enter  first name: ")
    last_name = input("Enter  last name: ")
    key = (first_name,last_name)
    if key in participants:
        del participants[key]
    else: print("participant not found")

def show_list(participants):
    if not participants:
        print("No participants")
    else:
        for (first_name, last_name), interests in participants.items():
            print(f"{first_name} {last_name} {interests}")

print("\n-----MENU-----")
print("add")
print("remove")
print("list")
print("exit")
participants = {}
while True:
    command = input("Enter command: ").strip().lower()
    if command == "add":
        add(participants)
    elif command == "remove":
        remove(participants)
    elif command == "list":
        show_list(participants)
    elif command == "exit":
        print("Bye")
        break
    else: print("Enter valid command")
