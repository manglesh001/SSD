import csv
participants = []
expenses = []
def is_valid_participant(name):
    return name.isalpha() and name not in participants
def add_participants():
    num_participants = int(input("No of participants: "))
    for _ in range(num_participants):
        while True:
            name = input("Enter participant's name: ").strip()
            try:
                if not is_valid_participant(name):
                    raise ValueError("Invalid participant name or name already exists.")
                participants.append(name)
                break
            except ValueError as e:
                print(f"Error: {e}")

def is_valid_amount(amount):
    return amount >= 0

def add_expense():
    print("Add Expense")
    while True:
        paid_by = input("Paid by: ").strip()
        try:
            if paid_by not in participants:
                raise ValueError("Invalid participant. Paid by participant not present")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
            
        amount = float(input("Amount: "))
        try:

            if not is_valid_amount(amount):

                raise ValueError("Invalid amount. Amount must be greater than or equal to 0.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    while True:
           
        try:
          
            participants_involved = input("Distributed amongst Participant use comma separate ").strip().split(',')
            if not all(participant in participants for participant in participants_involved):
                raise ValueError("Invalid participants")

            if len(participants_involved)!=0:



                expenses.append([paid_by,amount,"Gets_Back"])
                split_amount = amount / len(participants_involved)
                amt = split_amount * (len(participants_involved) - 1)
                for participant in participants_involved:
                    if paid_by == participant:
                        expenses.append([participant, amt, "Gets Back"])
                    else:
                        expenses.append([participant, split_amount, "Owes"])
                print("Expense added successfully!")
                break
            else:
                print("Enter at least one participant: ")
        except ValueError as e:
                
                print(f"Error: {e}")

def show_expenses():
    print("Expense Data:-")
    print("{:<20} {:<10} {:<20}".format("Participant's Name", "Amount", "Owes / Gets Back"))

    net_balance = {}
    for expense in expenses:
        name, amount, status = expense
        if status == "Owes":
            net_balance[name] = net_balance.get(name, 0) + amount
        else:
            net_balance[name] = net_balance.get(name, 0) - amount
    for participant in participants:
        balance = net_balance.get(participant, 0)
        if balance > 0:
            print("{:<20} ${:<10.2f} Owes".format(participant, balance))
        elif balance < 0:
            print("{:<20} ${:<10.2f} Gets Back".format(participant, -balance))
        else:
            print("{:<20} $0.00       Owes/Gets Back".format(participant))

            
def save_data_to_csv():
    with open("expenses.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Participant's Name", "Amount", "Status"])
        writer.writerows(expenses)
    print("Written in 'expenses.csv' file")

def main():
    while True:
        print("\nMenu:")
        print("1. Add participants")
        print("2. Add expense")
        print("3. Show all participant")
        print("4. Show expenses")
        print("5. Export/Exit..")

        choice = input("Choice ")

        if choice == "1":
            add_participants()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            print("All Participants:")
            for participant in participants:
                print(participant)
        elif choice == "4":
            show_expenses()
        elif choice == "5":
            save_data_to_csv()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
