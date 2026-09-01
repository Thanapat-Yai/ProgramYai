print("=====================")
print("Welcome to primative")
print("=====================")
print("This is 4 menu to use")
print(":search")
print(":undo")
print(":history")
print(":exit")

history = []
current_page = "Home"

while True:
    choice = input("Enter your choice: ").strip()

    if choice == "search":
        search = input("Enter your search website: ").strip()
        history.append(search)
        current_page = search
        print("Searching for:", search)
        print("User is now on:", current_page)

    elif choice == "undo":
        if len(history) == 0:
            print("No actions to undo.")
            print("User is now on:", current_page)
        else:
            last_action = history.pop()
            print("Undoing last action...")
            print("Removed:", last_action)

            if len(history) > 0:
                current_page = history[-1]
            else:
                current_page = "Home"

            print("User is now on:", current_page)

    elif choice == "history":
       print(f"history: {history}")

    elif choice == "exit":
        print("Exiting program.")
        break

    else:
         choice != "search" and  "undo" and "history" and "exit"
         print("Invalid choice. Make sure your type is correct")


