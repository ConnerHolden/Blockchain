from functools import reduce

# Mining reward
mining_reward = 10
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

    # Since get_balance() calculates sender/recipient balances from blockchain, the
    # balance of the sender must be updated from open_transactions as well so that the
    # sender isn't allowed to send more than they have before the next block is added.
    open_transaction_sender = [
        transaction["amount"]
        for transaction in open_transactions
        if transaction["sender"] == participant
    ]

    transaction_sender.append(open_transaction_sender)

    # amount_sent = reduce(
    #     lambda transaction_sum, transaction_amount: transaction_sum
    #     + transaction_amount[0]
    #     if len(transaction_amount) > 0
    #     else 0,
    #     transaction_sender,
    #     0,
    # )
    amount_sent = 0
    for block in transaction_sender:
        for transaction in block:
            if transaction > 0:
                amount_sent += transaction

    transaction_recipient = [
        [
            transaction["amount"]
            for transaction in block["transactions"]
            if transaction["recipient"] == participant
        ]
        for block in blockchain
    ]

    # amount_received = reduce(
    #     lambda transaction_sum, transaction_amount: transaction_sum
    #     + transaction_amount[0]
    #     if len(transaction_amount) > 0
    #     else 0,
    #     transaction_recipient,
    #     0,
    # )
    amount_received = 0
    for block in transaction_recipient:
        for transaction in block:
            if transaction > 0:
                amount_received += transaction

    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Return value of last block in the blockchain.
    """
    if not blockchain:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction["amount"]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Add transaction (dictionary) to open_transactions (list).
        Add sender and recipient to participants (set).
    """

    # Transaction
    transaction = {
        "recipient": recipient,
        "sender": sender,
        "amount": amount,
    }

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    """ Add block (dictionary) to blockchain (list).
    """
    last_block = blockchain[-1]
    # hashed_block creates a new list using 'list comprehensions': For each element (key)
    # in last_block, a new element is generated (the dictionary value last_block[key])
    # to fill a new list. The hash is generated using "".join(str()) to create a new
    # string from the list and join it together.
    hashed_block = hash_block(last_block)

    # Reward transaction
    reward_transaction = {
        "sender": "mining",
        "recipient": owner,
        "amount": mining_reward,
    }

    # The reward for mining is added before a block is successfully incorporated into the
    # blockchain

    # A separate copy of the *values* in a preexisting list are not copied in variable
    # assignment, e.g. copied_transactions = open_transactions, but rather a mirror image
    # of the *references* is created. This means that changes to one affect the other.
    # In order to create a separate copy of a list's values, a range must be specified in
    # the original, e.g. copied_transactions = open_transactions[:].
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)

    # Block
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": copied_transactions,
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


def validate_transactions():
    return all([verify_transaction(transaction) for transaction in open_transactions])


# Determines whether while loop should run
waiting_for_input = True

while waiting_for_input:
    print("\n(A)dd new transaction")
    print("(B)lockchain")
    print("(O)pen transactions")
    print("(C)oin balance")
    print("(P)articipants")
    print("(M)ine new block")
    print("(V)alidate transactions")
    print("(H)ack")
    print("(Q)uit")
    user_choice = input_user_choice()

    # Add transaction
    if user_choice == "A":
        transaction_data = input_transaction_value()
        # The tuple of values returned by input_transaction_value() is assigned to
        # transaction_data. These values are then assigned to a tuple of variables that
        # can be used by add_transaction()
        (recipient, amount) = transaction_data  # Access tuple
        if add_transaction(recipient, amount=amount):
            print("\nAdded transaction!")
        else:
            print("\nTransaction failed!")
        print(f"Open transacitons: {open_transactions}")
    # Output blockchain
    elif user_choice == "B":
        print_blockchain_elements()
    # Output open transactions
    elif user_choice == "O":
        print(f"\nOpen transacitons: {open_transactions}")
    # Output balance
    elif user_choice == "C":
        print("\nPrinting balance ...")
        print("Balance of {}: {:->10.2f}".format("Conner", get_balance("Conner")))
    # Output participants
    elif user_choice == "P":
        print(participants)
    # Mine block
    elif user_choice == "M":
        if mine_block():
            open_transactions = []
    # Validate transactions
    elif user_choice == "V":
        if validate_transactions():
            print("\nAll transactions are valid.")
        else:
            print("\nThere are invalid transactions.")
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
else:
    print("\nUser left!")

print("\nDone.")
