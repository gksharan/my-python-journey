expense = []
while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    user = input("Enter your choice: ")
    if user == '1':
        amt = float(input("Enter expense amount: "))
        cat = input("Enter expense category: ")
        description = input("Enter expense description: ")
        expense.append({'amount': amt, 'category': cat, 'description': description})