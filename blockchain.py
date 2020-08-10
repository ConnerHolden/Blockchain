# Initial block
genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": [],
}
# List of all blocks
blockchain = [genesis_block]
# List of all transactions made (bug) instead of transactions not add to bloackchain
open_transactions = []
# Local sender
owner = "Conner"
# Set of participants
participants = {"Conner"}


# Hash generator
def hash_block(block):
    """ Generate hash.
    """
    return "-".join([str(block[key]) for key in block])


def get_balance(participant):
    """ Return coin balance of participant.

        :transaction_sender:
        A nested list comprehension:
            For each block (dictionary) in blockchain (list),
            the open_transactions (dictionary value of block["transactions"])
            populates transaction_sender (list).
                For each transaction in open_transactions,
                the amount (dictionary value of transaction["amount"])
                populates open_transactions 
                if the sender (dictionary value of transaction["sender"])
                is the participant in question.
    """
    transaction_sender = [
        [
            transaction["amount"]
            for transaction in block["transactions"]
            if transaction["sender"] == participant
        ]
        for block in blockchain
    ]

    amount_sent = 0
    for transaction in transaction_sender:
        if len(transaction) > 0:
            amount_sent += transaction[0]

    transaction_recipient = [
        [
            transaction["amount"]
            for transaction in block["transactions"]
            if transaction["recipient"] == participant
        ]
        for block in blockchain
    ]

    amount_received = 0
    for transaction in transaction_recipient:
        if len(transaction) > 0:
            amount_received += transaction[0]

    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Return value of last block in the blockchain.
    """
    if not blockchain:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Add transaction (dictionary) to open_transactions (list).
        Add sender and recipient to participants (set).
    """
    transaction = {"recipient": recipient, "sender": sender, "amount": amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    """ Add block (dictionary) to blockchain (list).
    """
    last_block = blockchain[-1]
    # hashed_block creates a new list using 'list comprehensions': For each element (key)
    # in last_block, a new element is generated (the dictionary value last_block[key])
    # to fill a new list. The hash is generated using "".join(str()) to create a new
    # string from the list and join it together.
    hashed_block = hash_block(last_block)

    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": open_transactions,
    }
    blockchain.append(block)
    return True


def input_transaction_value():
    """ Return transaction input.
    """
    transaction_recipient = input("Enter the recipient of the transaction: ")
    transaction_amount = float(input("\nEnter your transaction amount: "))
    return (
        transaction_recipient,
        transaction_amount,
    )  # Tuple (do not need parentheses)


def input_user_choice():
    """ Prompt user.
    """
    user_choice = input("\n>> ").upper()
    return user_choice


def print_blockchain_elements():
    """ Print every block (dictionary) in the blockchain (list).
    """
    for block in blockchain:
        print(f"\nPrinting block {block['index']} ...")
        print(block)


def verify_chain():
    """ Determine if a block's previous_hash is the same as the hash of previous block.
    """
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True


# Determines whether while loop should run
waiting_for_input = True

while waiting_for_input:
    print("\n(A)dd new transaction.")
    print("(O)utput blockchain.")
    print("Output (p)articipants.")
    print("(M)ine new block.")
    print("(H)ack.")
    print("(Q)uit.")
    user_choice = input_user_choice()

    # Add transaction
    if user_choice == "A":
        transaction_data = input_transaction_value()
        (recipient, amount) = transaction_data  # Access tuple
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    # Output blockchain
    elif user_choice == "O":
        print_blockchain_elements()
    # Output participants
    elif user_choice == "P":
        print(participants)
    # Mine block
    elif user_choice == "M":
        if mine_block():
            open_transactions = []
    # Hack blockchain
    elif user_choice == "H":
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transactions": [
                    {"sender": "Chris", "recipient": "Conner", "amount": 100.0}
                ],
            }
    # Quit
    elif user_choice == "Q":
        waiting_for_input = False
    # Invalid entry
    else:
        print("\nInvalid entry.")
    # Verify
    if not verify_chain():
        print("Invalid blockchain!")
        print_blockchain_elements()
        break
    print(get_balance("Conner"))
else:
    print("\nUser left!")

print("\nDone.")
