print("==============================")
print("       EXPENSE TRACKER")
print("==============================")

expenses = []
amounts = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        expense = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append(expense)
        amounts.append(amount)

        print("Expense added successfully!")

    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:")

            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]} - Rs. {amounts[i]}")

    elif choice == 3:
        if len(amounts) == 0:
            print("No expenses recorded.")
        else:
            total = 0

            for amount in amounts:
                total = total + amount

            print(f"Total Expense: Rs. {total}")

    elif choice == 4:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")