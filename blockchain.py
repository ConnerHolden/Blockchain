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
    user_choice = input("\n>> ").upper()
    return user_choice


def print_blockchain_elements():
    for block in blockchain:
        print(block)


# def verify_chain():
#     is_valid = True
#     for block_index in range(len(blockchain)):
#         if block_index == 0:
#             block_index += 1
#             continue
#         elif blockchain[block_index][0] == blockchain[block_index - 1]:
#             is_valid = True
#         else:
#             is_valid = False
#             break
#         block_index += 1
#     return is_valid


# def verify_chain():
#     block_index = 0
#     is_valid = True
#     for block in blockchain:
#         if block_index == 0:
#             block_index += 1
#             continue
#         elif block[0] == blockchain[block_index - 1]:
#             is_valid = True
#         else:
#             is_valid = False
#             break
#         block_index += 1
#     return is_valid


def verify_chain():
    for index, block in enumerate(blockchain):
        if index >= 1 and block[0] != blockchain[index - 1]:
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print("\n(A)dd new transaction.")
    print("(O)utput blockchain.")
    print("(H)ack.")
    print("(Q)uit.")
    user_choice = input_user_choice()
    if user_choice == "A":
        transaction_amount = input_transaction_value()
        add_value(transaction_amount, get_last_blockchain_value())
    elif user_choice == "O":
        print_blockchain_elements()
    elif user_choice == "H":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "Q":
        waiting_for_input = False
    else:
        print("\nInvalid choice.")
    if not verify_chain():
        print("Invalid blockchain!")
        print_blockchain_elements()
        break
else:
    print("\nUser left!")

print("\nDone.")
