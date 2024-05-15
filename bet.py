def bit_fun(name, amount):
    bit_info = {
        "Name": name,
        "Amount": amount,
    }
    bit_list.append(bit_info)


bit_list = []
highest_bit_amount = 0
highest_bet_person = ""
will_bit_continue = False

while not will_bit_continue:
    user_name = input("Enter the bidder's name: ")
    user_bit_amount = int(input("Enter the bid: "))
    bit_fun(user_name, user_bit_amount)

    another_bitter = input("Is there another person to bid? Type 'yes' or 'no': ")

    if another_bitter.lower() == "yes":
        continue
    else:
        for k in bit_list:
            if k["Amount"] > highest_bit_amount:
                highest_bit_amount = k["Amount"]
                highest_bet_person = k["Name"]
                will_bit_continue = True

print(f"The highest bid is {highest_bit_amount} and was won by {highest_bet_person}.")
