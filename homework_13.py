from idlelib.window import registry


def main():
    registry = {}

print("=== MENU ===")
print("unlok command: add, remove, list, exit\n")

while True:
    command = input("command: ")
    if command == "exit":
        print("bye")
        break
    elif command == "add":
        first_name = input("first name: ")
        last_name = input("last name: ")
        participant_key = (first_name, last_name)
        interest_input = input("interest input: ")
        interest_set = (interest.strip().capitalize() for interest in interest_input.split(",") if interest_input)
        if participant_key in registry:
            registry[participant_key].update(interest_set)
            print(f"{first_name} {last_name} added successful")
        else:
            registry[participant_key] = interest_set
            print(f"{first_name} {last_name} added successfully")
    elif command == "remove":
        first_name = input("first name: ")
        last_name = input("last name: ")
        participant_key = (first_name, last_name)
        if participant_key in registry:
            del registry[participant_key]
            print(f"{first_name} {last_name} removed successful")
        else:
            print("participant not found")
    elif command == "list":
        if not registry:
            print("registry is empty")
        else:
            print("\n---listing all participants---")
            for index, ((first_name, last_name), interest_set) in enumerate(registry.items(), start=1):
                interest_str = ", ".join(interest_set) if interest_set else "no interest "
                print(f"{index}. {first_name} {last_name} ({interest_str})")
    else:
        print("invalid command")

    print()

if __name__ == "__main__":
    main()
