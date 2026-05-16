# Expenses-Tracker-Python
# I Have done my first project in python

print("Welcome To Expense Tracker")

expenses = []

while True:

    print("===== MENU =====")
    print("1. ADD EXPENSES")
    print("2. VIEW EXPENSES")
    print("3. TOTAL EXPENSES ")
    print("4. EXIT")

    choice = int(input("Enter value here: "))

    if (choice == 1):
        date = input("Enter date: ")
        category = input("Enter Category: ")
        details = input("Enter Details(depth to unerstand): ")
        amount = float(input("Enter amount: "))

        expense = {
            "date" : date,
            "category" : category,
            "details" : details,
            "amount" : amount
        }

        expenses.append(expense)
        print("Succesfully Added!!:)")


    elif (choice == 2):
        if(len(expenses) == 0):
            print("NO Match Found")
        else:
            print("====== Expenses ======")
            count = 1
        for item in expenses:
            print(f"expenses {count} => {item["date"]}, {item["category"]}, {item["details"]}, {item["amount"]}" )
            count += 1

    elif (choice == 3):
        total = 0

        for item in expenses:
            total = total + item["amount"]
            print("Total", total)

    elif (choice == 4):
        print("thankyou!")
        break

else:
    print("InCorrect number!")


