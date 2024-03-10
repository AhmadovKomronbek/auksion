from art import logo

auction_participants = {}

def find_biggest_price(data):
    highest_price = 0
    winner = ""

    for auctioner in data:
        if data[auctioner] > highest_price:
            highest_price = data[auctioner]
            winner = auctioner
    print(f"The winner is {winner}, The price is {highest_price}.")

auction_finished = False

print(logo)
while not auction_finished:
    name = input("What is your name: ")
    price = int(input("What is your price?:$ "))
    auction_participants[name] = price
    wanna_continue = input("Are there any auction participant? Type 'yes' or 'no'. \n").lower()
    if wanna_continue == 'no':
        auction_finished = True
        find_biggest_price(auction_participants)
        print(auction_participants)
    elif wanna_continue == 'yes':
        print(auction_participants)
        continue
    else:
        print("Program quited!")
        break