cb = {}
while True:
    print("1. View contacts")
    print("2. Add contact")
    print("3. Delete contact")
    print("4. Update contact")
    print("5. Exit")

    cc = input("Choose: ")

    if cc == "1":
        if not cb:
            print("empty")
        else:
            for name,number in cb.items():
                print(f"{name}: {number}")

    if cc =="2":
        name = input("Enter name: ")
        number = input("Enter number: ")
        cb[name] = number
        print("Contact added!")

    if cc == "3":
        name = input("enter the name of contact to delete: ")
        if name in cb:
            del cb[name]
            print("Contact deleted!")
        else:
            print("Contact not found.")



    if cc == "5":
        break
    