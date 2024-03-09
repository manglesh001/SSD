import csv
cricketer_directory = []

csv_file = "cricketer_directory.csv"

def load_entries():
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            cricketer_directory.extend(reader)
    except FileNotFoundError:
        print("CSV file not found")

def display_directory():
    if not cricketer_directory:
        print("Cricketer Directory is empty.")
        return

    print("{:<12} {:<12} {:<4} {:<12} {:<12} {:<6} {:<6} {:<6} {:<10}".format(
        "First Name", "Last Name", "Age", "Nationality", "Role", "Runs", "Balls", "Wickets", "Strike Rate"))
    for entry in cricketer_directory:
        print("{:<12} {:<12} {:<4} {:<12} {:<12} {:<6} {:<6} {:<6} {:<10}".format(
            entry["First Name"], entry["Last Name"], entry["Age"], entry["Nationality"],
            entry["Role"], entry["Runs"], entry["Balls"], entry["Wickets"], entry["Strike Rate"]))

def add_entry():
    entry = {}
    entry["First Name"] = input("Enter First Name: ")
    entry["Last Name"] = input("Enter Last Name: ")
    entry["Age"] = input("Enter Age: ")
    entry["Nationality"] = input("Enter Nationality: ")
    entry["Role"] = input("Enter Role (Batsmen, Bowler, All-rounder, Wk-Batsmen): ")
    entry["Runs"] = input("Enter Runs: ")
    entry["Balls"] = input("Enter Balls: ")
    entry["Wickets"] = input("Enter Wickets: ")

    if entry["Role"] in ["Batsmen", "All-rounder"]:
        entry["Strike Rate"] = float(entry["Runs"]) / float(entry["Balls"])
    elif entry["Role"] == "Bowler":
        entry["Strike Rate"] = float(entry["Wickets"]) / float(entry["Balls"])
    else:
        entry["Strike Rate"] = max(float(entry["Runs"]) / float(entry["Balls"]), float(entry["Wickets"]) / float(entry["Balls"]))

    cricketer_directory.append(entry)
  
def remove_entry():
    last_name = input("Enter the Last Name of the cricketer to remove: ")
    for entry in cricketer_directory:
        if entry["Last Name"] == last_name:
            cricketer_directory.remove(entry)
            
            return
    print("not found in the directory.")

def update_entry():
    last_name = input("Enter the Last Name of the cricketer to update: ")
    for entry in cricketer_directory:
        if entry["Last Name"] == last_name:
            print("Cricketer found in the directory.")
            print("Select the field to update:")
            print("1. First Name")
            print("2. Last Name")
            print("3. Age")
            print("4. Nationality")
            print("5. Role")
            print("6. Runs")
            print("7. Balls")
            print("8. Wickets")
            print("9. Strike Rate")
            choice = int(input("Enter the number of the field to update: "))

            if choice == 1:
                entry["First Name"] = input("Enter updated First Name: ")
            elif choice == 2:
                entry["Last Name"] = input("Enter updated Last Name: ")
            elif choice == 3:
                entry["Age"] = input("Enter updated Age: ")
            elif choice == 4:
                entry["Nationality"] = input("Enter updated Nationality: ")
            elif choice == 5:
                entry["Role"] = input("Enter updated Role: ")
            elif choice == 6:
                entry["Runs"] = int(input("Enter updated Runs: "))
            elif choice == 7:
                entry["Balls"] = int(input("Enter updated Balls: "))
            elif choice == 8:
                entry["Wickets"] = int(input("Enter updated Wickets: "))
            elif choice == 9:
                entry["Strike Rate"] = float(input("Enter updated Strike Rate: "))
            else:
                print("Invalid field choice.")
                return

            print("Entry updated successfully.")
            return

    print("Cricketer not found in the directory.")

def display_entry(entry):
    print("Cricketer Details:")
    for key, value in entry.items():
        print(f"{key}: {value}")
    print()

def search_entries():
    attribute = input("Enter the attribute to search for (e.g., First Name): ")
    value = input(f"Enter the {attribute} to search: ")
    matching_entries = [entry for entry in cricketer_directory if entry.get(attribute) == value]
    
    if not matching_entries:
        print("No matching entries found.")
    else:
        print("Matching Entry:")
        for entry in matching_entries:
            display_entry(entry)


def write_to_csv():
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ["First Name", "Last Name", "Age", "Nationality", "Role", "Runs", "Balls", "Wickets", "Strike Rate"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cricketer_directory)
    print("Data written to the CSV file.")

def main():
    load_entries()
    while True:
        print("\nCricketer's Directory Menu:")
        print("1. Display Directory")
        print("2. Add Entry")
        print("3. Remove Entry")
        print("4. Update Entry")
        print("5. Search Entries")
        print("6. Write to CSV")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_directory()
        elif choice == "2":
            add_entry()
        elif choice == "3":
            remove_entry()
        elif choice == "4":
            update_entry()
        elif choice == "5":
            search_entries()
        elif choice == "6":
            write_to_csv()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
