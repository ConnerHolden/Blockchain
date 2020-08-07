blockchain = []


def get_last_blockchain_value():
    if not blockchain:
        # blockchain.append(["initial"])
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def input_transaction_value():
    return float(input("\nEnter your transaction amount: "))


def input_user_choice():
    user_choice = input("\n>> ")
    return user_choice


def print_blockchain_elements():
    for block in blockchain:
        print(block)


while True:
    print("\n(1) Add a new transaction.")
    print("(2) Output blockchain.")
    print("(Q)uit.")
    user_choice = input_user_choice()
    if user_choice == "1":
        transaction_amount = input_transaction_value()
        add_value(transaction_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_elements()
    elif user_choice.upper() == "Q":
        break
        # <continue> would skip the rest of the loop and restart it
    else:
        print("\nInvalid choice.")

print("Done.")
