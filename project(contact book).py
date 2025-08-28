contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        name = input("Enter contact name: ")
        gmail = input("Enter contact gmail: ")
        contacts[name] = gmail
        print("✅ Contact added!")

    elif choice == "2":
        if contacts:
            print("\n--- Your Contacts ---")
            for name, gmail in contacts.items():
                print(name, ":", gmail)
        else:
            print("No contacts found.")

    elif choice == "3":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("❌ Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
