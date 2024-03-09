import matplotlib.pyplot as plt
import csv

n=input("Enter 1 to visualize expenses data and Enter 2 to visualize Cricket data: ")
if n=="2":


    first_names, last_names, batting_strike_rates, bowling_strike_rates = [], [], [], []

    with open('cricketer_directory.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            first_name = row['First Name']
            last_name = row['Last Name']
            runs = int(row['Runs'])
            balls = int(row['Balls'])
            wickets = int(row['Wickets'])

            if balls > 0:
                batting_strike_rate = runs / balls
            else:
                batting_strike_rate = 0

            if balls > 0:
                bowling_strike_rate = wickets / balls
            else:
                bowling_strike_rate = 0

            first_names.append(first_name)
            last_names.append(last_name)
            batting_strike_rates.append(batting_strike_rate)
            bowling_strike_rates.append(bowling_strike_rate)

    x = range(len(first_names))
    width = 0.4

    plt.figure(figsize=(12, 6))
    plt.bar(x, batting_strike_rates, width=width, label='Batting Strike Rate')
    plt.bar([i + width for i in x], bowling_strike_rates, width=width, label='Bowling Strike Rate')
    plt.xlabel('Players')
    plt.ylabel('Strike Rate')
    plt.title('Batting and Bowling Strike Rates of Cricketers')
    plt.xticks([i + width / 2 for i in x], [f'{first} {last}' for first, last in zip(first_names, last_names)], rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.show()



elif n=="1":

    owes = {}
    gets_back = {}
    with open('expenses.csv', 'r') as csvfile:
        rd = csv.DictReader(csvfile)
        for row in rd:
            participant = row["Participant's Name"]
            amount = float(row['Amount'])

            if row['status'] == 'Owes':
                owes[participant] = amount
            elif row['status'] == 'Gets Back':
                gets_back[participant] = amount

    max_percentage_owes = max(owes.values())
    max_percentage_gets_back = max(gets_back.values())

    plt.figure(1)
    explode_owes = [0.1 if amount == max_percentage_owes else 0 for amount in owes.values()]  
    plt.pie(owes.values(), labels=owes.keys(), autopct='%1.1f%%', startangle=140, explode=explode_owes)
    plt.title("Owes")
    plt.legend(owes.keys(), title="partis", loc="best")


    plt.figure(2)
    explode_gets_back = [0.1 if amount == max_percentage_gets_back else 0 for amount in gets_back.values()] 
    plt.pie(gets_back.values(), labels=gets_back.keys(), autopct='%1.1f%%', startangle=140, explode=explode_gets_back)
    plt.title("Gets Back")
    plt.legend(gets_back.keys(), title="Participants", loc="best")

    plt.show()
