import Mjolner_gavel as mj

print(mj.logo)

participant = {}

option = True

while option:
    name = input("Please Enter bidder name: ")
    bid = int(input("Please Enter bid: "))
    participant[name] = bid
    print("\n"*100)
    choice =input("Are there more bidders? (Y or N)").lower()
    if choice == "n":
        option = False
    
print(participant)

print(f"Auction winner is {max(participant, key = participant.get)} with bid amount ${max(participant.values())}")